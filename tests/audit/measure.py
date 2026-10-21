"""Đo từ ảnh chụp prototype (ai/phan-bien-giao-dien/anh/) và hotspots.json.

Chạy:  python tests/audit/measure.py   (cần Pillow)
       python tests/audit/measure.py v2   (đo ảnh Final UI v2 ở assets/figma/final-ui-v2/ và hotspots-v2.json)
- Tỉ lệ điểm ảnh theo nhóm màu: cam đậm (nút, banner, chữ cam), kem/be (nền, thẻ đào), trắng, nâu đậm, màu khác.
- Vùng bấm nhỏ hơn 48 dp (đọc từ hotspots.json).
"""
import colorsys, json, os, sys
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
V2 = len(sys.argv) > 1 and sys.argv[1] == "v2"
SHOTS = os.path.join(HERE, "..", "..", "assets", "figma", "final-ui-v2") if V2 else os.path.join(HERE, "..", "..", "ai", "phan-bien-giao-dien", "anh")
CORE = ("S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08")


def shares(path):
    im = Image.open(path).convert("RGB")
    w, h = im.size
    px = list(im.resize((w // 2, h // 2)).getdata())
    n = len(px)
    c = dict(cam=0, kem=0, trang=0, nau=0, khac=0)
    for r, g, b in px:
        hh, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        hd = hh * 360
        if r > 248 and g > 248 and b > 248: c["trang"] += 1
        elif s > 0.55 and 18 <= hd <= 42 and v > 0.55: c["cam"] += 1
        elif 18 <= hd <= 45 and 0.06 < s <= 0.55 and v > 0.85: c["kem"] += 1
        elif v < 0.40: c["nau"] += 1
        elif s > 0.35: c["khac"] += 1
    return {k: round(100 * v / n, 1) for k, v in c.items()}


rows = {}
for f in sorted(os.listdir(SHOTS)):
    if f.endswith(".png") and not f.startswith("_"):
        rows[f[:-4]] = shares(os.path.join(SHOTS, f))
print("màn | cam đậm % | kem/be % | trắng % | nâu đậm % | màu khác %")
for k, v in rows.items():
    print(k, v["cam"], v["kem"], v["trang"], v["nau"], v["khac"], sep=" | ")
core = [rows[k] for k in CORE if k in rows]
if core:
    avg = lambda key: round(sum(r[key] for r in core) / len(core), 1)
    print(f"TB {len(core)} màn lõi: cam đậm {avg('cam')}% · kem/be {avg('kem')}% · trắng {avg('trang')}% · màu khác {avg('khac')}%")

data = json.load(open(os.path.join(HERE, "..", "figma-proto", "hotspots-v2.json" if V2 else "hotspots.json"), encoding="utf-8"))
small, total = [], 0
for frame, v in data["frames"].items():
    for h in v["hotspots"]:
        if h.get("name") == "(frame)" or h.get("trigger") == "timeout": continue
        total += 1
        if h["w"] < 48 or h["h"] < 48: small.append((frame, h.get("name", h.get("dest")), h["w"], h["h"]))
print(f"\nvùng bấm < 48 dp: {len(small)}/{total}")
for s in small: print(*s, sep=" | ")
