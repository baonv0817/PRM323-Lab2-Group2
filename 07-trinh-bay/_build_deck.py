"""Sinh 07-trinh-bay/BreakBite_Lab2_Presentation.pptx (33 slide) theo thứ tự quy trình thiết kế P0 → P5.

Chạy từ gốc repo:  python 07-trinh-bay/_build_deck.py [đường dẫn file ra]      (cần python-pptx và Pillow)
Ảnh lấy từ assets/figma/final-ui-v2/, assets/figma/boards/, assets/concepts/. Màu theo token v2:
nền #FAF8F5, cam #F69D39, nâu #622B14, viền #E4DFD8. Các bản deck cũ có trong lịch sử Git.
"""
import io
import os
import sys
import tempfile
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "figma", "final-ui-v2")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "07-trinh-bay", "BreakBite_Lab2_Presentation.pptx")
GITHUB = "https://github.com/baonv0817/PRM323-Lab2-Group2"

BG, CARD, BORDER = "FAF8F5", "FFFFFF", "E4DFD8"
ORANGE, ORANGE_D, SELECT = "F69D39", "B45309", "FFF1DE"
BROWN, MUTED, GREEN, RED = "622B14", "6B5F55", "15803D", "B91C1C"
GREEN_BG, RED_BG = "E8F5EC", "FCE8E8"
HEAD, BODY = "Segoe UI", "Calibri"
TOTAL = 33

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
BLANK = prs.slide_layouts[6]


def E(x):
    return Emu(int(x * 914400))


def rgb(h):
    return RGBColor.from_string(h)


def bg(slide, color=BG):
    f = slide.background.fill
    f.solid()
    f.fore_color.rgb = rgb(color)


def box(s, x, y, w, h, fill=CARD, line=BORDER, radius=0.04, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    sh = s.shapes.add_shape(shape, E(x), E(y), E(w), E(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = radius
    sh.shadow.inherit = False
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = rgb(line)
        sh.line.width = Emu(9525)
    return sh


def text(s, x, y, w, h, items, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT, gap=3):
    """items: [(text, size, bold, color)] hoặc [(text, size, bold, color, font)]."""
    tb = s.shapes.add_textbox(E(x), E(y), E(w), E(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    for i, it in enumerate(items):
        t, size, bold, color = it[:4]
        font = it[4] if len(it) > 4 else BODY
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(gap)
        r = p.add_run()
        r.text = t
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.name = font
        r.font.color.rgb = rgb(color)
    return tb


def chip(s, x, y, w, label, fill=SELECT, color=ORANGE_D, line=ORANGE, size=12, h=0.34):
    box(s, x, y, w, h, fill=fill, line=line, radius=0.5)
    text(s, x, y, w, h, [(label, size, True, color)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)


def circle_png(path):
    im = Image.open(path).convert("RGBA")
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, im.size[0] - 1, im.size[1] - 1), fill=255)
    im.putalpha(mask)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    buf.seek(0)
    return buf


def rounded_png(path, radius_ratio=0.07):
    im = Image.open(path).convert("RGBA")
    r = int(im.size[0] * radius_ratio)
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.size[0] - 1, im.size[1] - 1), radius=r, fill=255)
    im.putalpha(mask)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    buf.seek(0)
    return buf


def icon(s, name, x, y, d):
    s.shapes.add_picture(circle_png(os.path.join(IMG, "icons", name + ".png")), E(x), E(y), E(d), E(d))


def phone(s, name, x, y, h):
    path = os.path.join(IMG, name)
    iw, ih = Image.open(path).size
    w = h * iw / ih
    box(s, x, y, w, h, fill=CARD, line=BORDER, radius=0.07)
    s.shapes.add_picture(rounded_png(path), E(x), E(y), E(w), E(h))
    return w


def pic(s, path, x, y, w=None, h=None):
    iw, ih = Image.open(path).size
    if w is None:
        w = h * iw / ih
    else:
        h = w * ih / iw
    s.shapes.add_picture(path, E(x), E(y), E(w), E(h))
    return w, h


def sheet(s, name, x, y, h):
    return pic(s, os.path.join(IMG, name), x, y, h=h)


def cover(s, path, x, y, w, h):
    """Cắt ảnh theo tỉ lệ w:h, giữ phần trên trái, rồi đặt vào khung bo góc."""
    im = Image.open(path).convert("RGB")
    r = w / h
    cw, ch = im.size
    if cw / ch > r:
        im = im.crop((0, 0, int(ch * r), ch))
    else:
        im = im.crop((0, 0, cw, int(cw / r)))
    box(s, x, y, w, h, fill=CARD, line=BORDER, radius=0.04)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    buf.seek(0)
    tmp = os.path.join(tempfile.gettempdir(), "bb_cover.png")
    with open(tmp, "wb") as f:
        f.write(buf.read())
    s.shapes.add_picture(rounded_png(tmp, 0.03), E(x), E(y), E(w), E(h))


def gray_phone(s, name, x, y, h):
    """Wireframe xám: ảnh Figma v2 chuyển xám, giảm tương phản."""
    im = Image.open(os.path.join(IMG, name)).convert("L").point(lambda v: int(255 - (255 - v) * 0.55)).convert("RGB")
    tmp = os.path.join(tempfile.gettempdir(), "bb_gray_" + name.replace("/", "_"))
    im.save(tmp)
    iw, ih = im.size
    w = h * iw / ih
    box(s, x, y, w, h, fill=CARD, line="9A9A9A", radius=0.07)
    s.shapes.add_picture(rounded_png(tmp), E(x), E(y), E(w), E(h))
    return w


def arrow_row(s, x, y, h, steps_, labels, gap=1.2, label_size=9):
    """Hàng storyboard: ảnh màn hình, mũi tên và nhãn hành động giữa hai màn."""
    for k, nm in enumerate(steps_):
        w = phone(s, nm + ".png", x, y, h)
        if k < len(steps_) - 1:
            err = labels[k + 1].startswith("!")
            lab = labels[k + 1].lstrip("!")
            col = RED if err else ORANGE
            text(s, x + w, y + h / 2 - 0.42, gap, 0.4, [(lab, label_size, True, RED if err else ORANGE_D)], anchor=MSO_ANCHOR.BOTTOM, align=PP_ALIGN.CENTER)
            text(s, x + w, y + h / 2 - 0.2, gap, 0.4, [("→", 22, True, col)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
            x += w + gap
    return x


def table(s, x, y, w, rows, col_w, row_h=0.42, size=13):
    t = s.shapes.add_table(len(rows), len(rows[0]), E(x), E(y), E(w), E(row_h * len(rows))).table
    for j, cw in enumerate(col_w):
        t.columns[j].width = E(cw)
    for i, row in enumerate(rows):
        t.rows[i].height = E(row_h)
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.fill.solid()
            c.fill.fore_color.rgb = rgb(BROWN if i == 0 else (CARD if i % 2 else SELECT))
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.margin_left = c.margin_right = E(0.1)
            r = c.text_frame.paragraphs[0].add_run()
            r.text = val
            r.font.size = Pt(size)
            r.font.bold = i == 0 or j == 0
            r.font.name = BODY
            r.font.color.rgb = rgb(CARD if i == 0 else BROWN)
    return t


COUNTER = [0]


def content_slide(title, subtitle, icon_name, evidence, phase=None):
    COUNTER[0] += 1
    n = COUNTER[0] + 1  # slide 1 là bìa
    s = prs.slides.add_slide(BLANK)
    bg(s)
    icon(s, icon_name, 0.6, 0.42, 0.62)
    text(s, 1.4, 0.36, 9.2, 0.6, [(title, 28, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 1.4, 0.95, 9.2, 0.35, [(subtitle, 14, False, MUTED)])
    box(s, 1.4, 1.32, 0.9, 0.05, fill=ORANGE, line=None, radius=0.5)
    if phase:
        chip(s, 10.75, 0.5, 2.0, phase, size=12, h=0.38)
    text(s, 0.6, 7.03, 9.5, 0.25, [("Minh chứng: " + evidence, 10, False, MUTED)])
    text(s, 10.6, 7.03, 2.1, 0.25, [(f"BreakBite · {n} / {TOTAL}", 10, False, MUTED)], align=PP_ALIGN.RIGHT)
    return s


def bullets_card(s, x, y, w, h, head, lines, size=13, gap=8, fill=CARD, line=BORDER):
    box(s, x, y, w, h, fill=fill, line=line)
    items = [(head, 11, True, MUTED)] + [(t, size, False, BROWN) for t in lines]
    text(s, x + 0.25, y + 0.15, w - 0.5, h - 0.3, items, gap=gap)


def band(s, y, msg, h=0.7, size=13, bold=True, fill=SELECT):
    box(s, 0.6, y, 12.15, h, fill=fill, line=None)
    text(s, 0.85, y, 11.65, h, [(msg, size, bold, BROWN)], anchor=MSO_ANCHOR.MIDDLE)


# =============================================================== 1 · bìa
s = prs.slides.add_slide(BLANK)
bg(s)
box(s, 7.45, 0.75, 6.1, 6.1, fill=SELECT, line=None, shape=MSO_SHAPE.OVAL)
phone(s, "S05.png", 7.75, 2.55, 3.7)
phone(s, "S07.png", 11.0, 2.55, 3.7)
phone(s, "S02.png", 9.35, 1.35, 4.6)
icon(s, "restaurant", 0.8, 0.8, 0.9)
text(s, 0.8, 1.85, 6.6, 1.3, [("BreakBite", 72, True, BROWN, HEAD)])
text(s, 0.8, 3.2, 6.4, 0.6, [("Đặt món trước, nhận tại quầy.", 28, True, ORANGE_D, HEAD)])
text(s, 0.8, 3.85, 6.4, 0.8, [("Ăn kịp trong 15 phút giữa hai slot, không phải xếp hàng.", 18, False, MUTED)])
chip(s, 0.8, 4.75, 2.35, "App khách · 30 màn", size=13, h=0.4)
chip(s, 3.3, 4.75, 2.6, "App người bán · 15 màn", size=13, h=0.4)
text(s, 0.8, 5.45, 6.5, 1.5, [
    ("PRM323 · Lab 2 · Nhóm 2 · SE1919", 14, True, BROWN),
    ("Nguyễn Viết Bảo (SE183398) · Đỗ Hoàng Gia Bảo (SE193119) · Nguyễn Quốc Hoàng Pháp (SE190175) · "
     "Nguyễn Hoàng An (SE193905) · Nguyễn Thành Danh (SE193274)", 11, False, MUTED),
])
tb = text(s, 0.8, 6.55, 6.5, 0.3, [("GitHub: github.com/baonv0817/PRM323-Lab2-Group2", 11, False, ORANGE_D)])
tb.text_frame.paragraphs[0].runs[0].hyperlink.address = GITHUB

# =============================================================== 2 · quy trình
s = content_slide("Quy trình thiết kế P0 → P5", "Mỗi phase có sản phẩm kiểm chứng được và một gate; trình bày theo đúng thứ tự này", "check",
                  "00-quy-trinh/01-QUY-TRINH-UIUX.md · prm393-material.web.app/quality-gates")
phases = [("P0", "Ideas", "G0", "Vấn đề, hướng giải pháp, phạm vi MVP", "Đạt 6/6", GREEN, GREEN_BG),
          ("P1", "Research", "G1", "Kế hoạch, khảo sát, insight", "Có điều kiện", ORANGE_D, SELECT),
          ("P2", "UX Design", "G2", "Persona, story, IA, flow, wireframe", "5 / 6", ORANGE_D, SELECT),
          ("P3", "UI Concept", "G3", "Stitch, 3 hướng visual, style guide", "Đạt", GREEN, GREEN_BG),
          ("P4", "UI Design", "G4", "Final UI, trạng thái, prototype", "Có điều kiện", ORANGE_D, SELECT),
          ("P5", "Validation", "G5", "Kiểm thử, handoff Flutter", "Chưa test người", RED, RED_BG)]
for i, (p, name, g, out, st, col, fill) in enumerate(phases):
    x = 0.6 + i * 2.05
    box(s, x, 1.7, 1.95, 3.3)
    box(s, x + 0.2, 1.9, 0.75, 0.75, fill=ORANGE, line=None, shape=MSO_SHAPE.OVAL)
    text(s, x + 0.2, 1.9, 0.75, 0.75, [(p, 18, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    text(s, x + 0.2, 2.8, 1.6, 0.4, [(name, 15, True, BROWN, HEAD)])
    text(s, x + 0.2, 3.2, 1.6, 1.2, [(out, 11, False, MUTED)])
    chip(s, x + 0.2, 4.45, 1.55, f"{g} · {st}", fill=fill, color=col, line=col, size=10, h=0.3)
bullets_card(s, 0.6, 5.2, 5.9, 1.6, "CÔNG CỤ", ["Google Stitch tạo UI; Gemini và Claude phản biện; Figma dựng, Playwright kiểm thử prototype"], size=13)
bullets_card(s, 6.85, 5.2, 5.9, 1.6, "QUY TẮC", ["AI không thay phỏng vấn, usability test hay quyết định; phần chưa có bằng chứng ghi rõ là giả định"], size=13)

# =============================================================== 3 · P0 vấn đề
s = content_slide("Vấn đề cần giải quyết", "Ai gặp khó khăn gì, trong bối cảnh nào, hậu quả gì", "schedule",
                  "01-P0-y-tuong/01-p0-problem-framing.md mục 1", "P0 · Ideas")
box(s, 0.6, 1.6, 12.15, 1.7)
text(s, 0.85, 1.72, 11.65, 1.5, [
    ("PROBLEM STATEMENT", 11, True, MUTED),
    ("Sinh viên học trên campus có lịch học dày thường không mua kịp đồ ăn trong 15 phút nghỉ giữa hai slot, vì xếp hàng ở căn tin dồn "
     "đúng giờ nghỉ chung và tốn gần hết thời gian, nên họ bỏ bữa hoặc vào lớp trễ.", 17, False, BROWN),
    ("Làm sao để sinh viên có đồ ăn trong giờ nghỉ ngắn mà không phải xếp hàng?", 14, True, ORANGE_D),
], gap=6)
pains = [("schedule", "Hàng chờ đúng giờ nghỉ", "Xếp hàng gần hết 15 phút nghỉ, bỏ bữa hoặc vào lớp trễ"),
         ("location", "Không biết trước", "Quán mở hay đóng, còn món, bao lâu xong"),
         ("offer", "Phí phát sinh", "Tổng tiền chỉ hiện ở bước cuối"),
         ("error", "Lỗi thanh toán", "Mất giỏ hàng khi mạng yếu")]
for i, (ic, head, sub) in enumerate(pains):
    x = 0.6 + i * 3.07
    box(s, x, 3.5, 2.95, 1.7)
    icon(s, ic, x + 0.25, 3.7, 0.6)
    text(s, x + 0.25, 4.4, 2.5, 0.8, [(head, 14, True, BROWN), (sub, 12, False, MUTED)])
box(s, 0.6, 5.4, 5.95, 1.4, fill=SELECT, line=None)
text(s, 0.85, 5.5, 5.5, 1.3, [("CHỈ SỐ THÀNH CÔNG", 11, True, MUTED), ("Đặt xong một đơn dưới 35 giây, tối đa 8 chạm (Flow 1)", 14, True, BROWN),
                               ("Kết quả (giả thuyết): giảm số lần bỏ mua vì hàng chờ", 12, False, MUTED)], gap=5)
box(s, 6.8, 5.4, 5.95, 1.4, fill=SELECT, line=None)
text(s, 7.05, 5.5, 5.5, 1.3, [("AI PHẢN BIỆN (D18)", 11, True, MUTED), ("Problem statement cũ chứa giải pháp, nên chỉ mô tả vấn đề và thêm câu How might we", 13, True, BROWN),
                               ("Quyết định: Modify", 12, False, MUTED)], gap=5)

# =============================================================== 4 · P0 hướng giải pháp
s = content_slide("Các hướng đã cân nhắc", "Chấm Impact × Feasibility rồi chọn có lý do", "offer", "01-P0-y-tuong/01-p0-problem-framing.md mục 2", "P0 · Ideas")
box(s, 0.6, 1.6, 12.15, 3.55)
table(s, 0.85, 1.8, 11.65, [["Hướng", "Impact", "Feasibility", "Điểm", "Lý do"],
                            ["A · App đặt trước, nhận tại quầy", "5", "4", "20", "Gỡ cả thời gian lẫn thông tin; khớp yêu cầu app mobile"],
                            ["B · Web đặt món qua QR", "4", "3", "12", "Không cần cài app nhưng không khớp yêu cầu app mobile"],
                            ["C · Hàng chờ ảo + màn hình gọi số", "3", "3", "9", "Bớt đứng xếp hàng nhưng không rút ngắn thời gian chờ"],
                            ["D · Chatbot Zalo / Messenger", "2", "2", "4", "Khó tuỳ chỉnh topping và hiện trạng thái đơn"]],
      [3.7, 1.0, 1.2, 0.9, 4.85], row_h=0.62, size=13)
box(s, 0.6, 5.35, 5.95, 1.45, fill=GREEN_BG, line=GREEN)
text(s, 0.85, 5.45, 5.5, 1.3, [("CHỌN A", 12, True, GREEN), ("Giữ B làm phương án dự phòng cho rủi ro sinh viên ngại cài app (R2).", 13, False, BROWN)], gap=5)
box(s, 6.8, 5.35, 5.95, 1.45, fill=RED_BG, line=RED)
text(s, 7.05, 5.45, 5.5, 1.3, [("D20 · REJECT chuyển sang web QR", 12, True, RED), ("AI đề xuất, nhóm từ chối vì đề bắt buộc app mobile 360 × 800 dp và handoff Flutter.", 13, False, BROWN)], gap=5)

# =============================================================== 5 · P0 giả định, rủi ro, MVP
s = content_slide("Giả định, rủi ro và phạm vi MVP", "Phân biệt dữ kiện, giả thuyết và điều chưa biết", "location",
                  "01-P0-y-tuong/01-p0-problem-framing.md mục 3–5", "P0 · Ideas")
box(s, 0.6, 1.6, 7.0, 5.2)
table(s, 0.8, 1.75, 6.6, [["ID", "Giả định cần kiểm", "Kiểm bằng"],
                          ["H1", "Giờ nghỉ giữa hai slot ≤ 15 phút", "Khảo sát"],
                          ["H2", "Hàng chờ làm sinh viên bỏ mua", "Khảo sát"],
                          ["H3", "Biết trước trạng thái quán quyết định việc đặt", "Khảo sát"],
                          ["H4", "Sinh viên chấp nhận cài app riêng của quán", "Khảo sát"],
                          ["H5", "Khi thanh toán lỗi, muốn trả tiền mặt", "Phỏng vấn"],
                          ["H6", "Quầy cần mã lớn và QR để trả món nhanh", "Hỏi nhân viên quầy"],
                          ["H7", "Bếp làm kịp đơn dồn vào giờ nghỉ", "Hỏi chủ quán"]],
      [0.6, 4.2, 1.8], row_h=0.5, size=12)
text(s, 0.8, 5.95, 6.6, 0.8, [("Rủi ro: R1 persona chưa kiểm chứng · R2 ngại cài app · R3 bếp quá tải · R4 thanh toán lỗi khi mạng yếu", 11, False, MUTED)])
bullets_card(s, 7.85, 1.6, 4.9, 2.55, "TRONG PHẠM VI", ["App khách S01–S30, app người bán K01–K15", "Nhận tại quầy; QR, ví, tiền mặt", "Light theme, 360 × 800 dp, kiểm 412 dp"], size=13, gap=6)
bullets_card(s, 7.85, 4.35, 4.9, 2.45, "NGOÀI PHẠM VI", ["Giao hàng tận nơi", "Đăng nhập tích điểm, dark mode", "Thiết kế tablet, code Flutter"], size=13, gap=6, fill=SELECT, line=SELECT)

# =============================================================== 6 · P1 kế hoạch nghiên cứu
s = content_slide("Kế hoạch nghiên cứu", "Sáu câu hỏi nghiên cứu và cách trả lời", "person", "02-P1-nghien-cuu/01-p1-research.md mục 1–2", "P1 · Research")
rqs = ["RQ1 · Giữa hai slot thật sự có bao nhiêu phút?", "RQ2 · Hàng chờ dài bao lâu, có làm bỏ mua không?", "RQ3 · Cần biết gì trước khi quyết định mua?",
       "RQ4 · Có chịu cài app riêng của quán không?", "RQ5 · Khi thanh toán lỗi, đã làm gì?", "RQ6 · Quầy có làm kịp đơn dồn giờ nghỉ không?"]
box(s, 0.6, 1.6, 6.4, 5.2)
text(s, 0.85, 1.75, 5.9, 0.3, [("06 CÂU HỎI NGHIÊN CỨU", 11, True, MUTED)])
for i, r in enumerate(rqs):
    y = 2.2 + i * 0.7
    box(s, 0.85, y, 5.9, 0.6, fill=SELECT, line=None, radius=0.3)
    text(s, 1.05, y, 5.6, 0.6, [(r, 13, False, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
methods = [("Khảo sát Google Form", "22 câu cho RQ1–RQ5, mục tiêu từ 30 sinh viên", "Đang thu phản hồi", ORANGE_D, SELECT),
           ("Phỏng vấn mô phỏng AI", "5 hồ sơ sinh viên để tạo giả thuyết", "Đã làm", GREEN, GREEN_BG),
           ("Hỏi nhân viên quầy, chủ quán", "RQ6: quầy, bếp, đơn dồn giờ nghỉ", "Kế hoạch, chưa làm", RED, RED_BG)]
for i, (head, sub, st, col, fill) in enumerate(methods):
    y = 1.6 + i * 1.78
    box(s, 7.25, y, 5.5, 1.62)
    text(s, 7.5, y + 0.15, 3.1, 1.4, [(head, 14, True, BROWN), (sub, 12, False, MUTED)], gap=4)
    chip(s, 10.6, y + 0.2, 1.95, st, fill=fill, color=col, line=col, size=11, h=0.32)

# =============================================================== 7 · P1 kết quả
s = content_slide("Kết quả nghiên cứu hiện có", "Toàn bộ là dữ liệu mô phỏng AI, dùng để thử form và tạo giả thuyết", "receipt",
                  "02-P1-nghien-cuu/02-research.md · 02-P1-nghien-cuu/04-ai-persona-interviews.md · 02-P1-nghien-cuu/khao-sat/", "P1 · Research")
text(s, 0.6, 1.55, 12.1, 0.3, [("PHỎNG VẤN MÔ PHỎNG AI · 5 NHÂN VẬT (SIM-A1…A5)", 11, True, MUTED)])
for i, (big, label) in enumerate([("4 / 5", "muốn biết trước trạng thái quán"), ("3 / 5", "từng bỏ mua vì hàng chờ"), ("1 / 5", "là nguồn duy nhất của insight lỗi thanh toán")]):
    x = 0.6 + i * 4.1
    box(s, x, 1.9, 3.95, 1.55, fill=SELECT, line=None)
    text(s, x + 0.3, 2.0, 1.6, 1.3, [(big, 34, True, ORANGE_D, HEAD)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 1.95, 2.0, 1.9, 1.3, [(label, 13, False, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.6, 3.7, 12.1, 0.3, [("KHẢO SÁT GOOGLE FORM · CHẠY THỬ 20 PHẢN HỒI MÔ PHỎNG (SIM-S01…S20)", 11, True, MUTED)])
for i, (big, label) in enumerate([("4,5 / 5", "mức quan trọng của thời gian chờ (H3)"), ("0 / 20", "biết trước phải chờ bao lâu"), ("9 / 20", "ngại cài vì phải đăng ký tài khoản")]):
    x = 0.6 + i * 4.1
    box(s, x, 4.05, 3.95, 1.55, fill=SELECT, line=None)
    text(s, x + 0.3, 4.15, 1.9, 1.3, [(big, 30, True, ORANGE_D, HEAD)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 2.2, 4.15, 1.6, 1.3, [(label, 12, False, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
band(s, 5.85, "Không dùng các số này làm bằng chứng hay khẳng định tỉ lệ. Khảo sát thật đang thu phản hồi và sẽ thay phần này.", h=0.9)

# =============================================================== 8 · P1 insight → quyết định
s = content_slide("Insight → quyết định thiết kế", "Mỗi quyết định nối về một insight có mã", "check", "02-P1-nghien-cuu/01-p1-research.md mục 3 · 03-P2-ux-design/02-persona-mapping.xlsx", "P1 · Research")
box(s, 0.6, 1.6, 12.15, 4.6)
rows = [("INS-01", "Hàng chờ giờ nghỉ", "SIM-A1, A2, A5", "Đặt trước và hẹn giờ nhận (S05)"),
        ("INS-02", "Cần biết trước", "SIM-A1, A3, A4, A5", "Trạng thái quán và thời gian chờ (S02)"),
        ("INS-04", "Ngại phí ẩn", "SIM-A1, A2", "Giá cộng dồn trên nút, tổng ở giỏ (S04, S05)"),
        ("INS-05", "Không muốn đăng ký", "SIM-A1, A3", "Xem menu không cần tài khoản (D12, S26 không bắt buộc)"),
        ("INS-06", "Lỗi thanh toán", "SIM-A5 (1 nguồn)", "Màn phục hồi giữ giỏ hàng (S06-ERR)"),
        ("Hành vi", "Thao tác một tay", "SIM-A1, A5", "Nút chính ở nửa dưới, vùng bấm từ 48 dp")]
text(s, 0.9, 1.75, 2, 0.3, [("INSIGHT", 11, True, MUTED)])
text(s, 3.3, 1.75, 2.5, 0.3, [("BẰNG CHỨNG", 11, True, MUTED)])
text(s, 6.0, 1.75, 4, 0.3, [("QUYẾT ĐỊNH THIẾT KẾ", 11, True, MUTED)])
for i, (code, need, ev, design) in enumerate(rows):
    y = 2.1 + i * 0.67
    box(s, 0.85, y, 11.65, 0.58, fill=SELECT, line=None, radius=0.3)
    text(s, 1.0, y, 0.9, 0.58, [(code, 12, True, ORANGE_D)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 1.95, y, 1.9, 0.58, [(need, 13, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 3.9, y, 1.9, 0.58, [(ev, 11, False, MUTED)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 6.0, y, 6.4, 0.58, [(design, 13, False, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
band(s, 6.35, "Độ tin cậy thấp vì nguồn là mô phỏng; mỗi insight đã gắn nhãn Assumed trong tài liệu.", h=0.5, size=12)

# =============================================================== 9 · P2 persona
s = content_slide("Persona", "Một persona chính, hai persona phụ và một nhóm không nhắm tới", "person", "03-P2-ux-design/01-persona.md (12 trường lõi)", "P2 · UX Design")
personas = [("Q", "Nguyễn Minh Quân", "20 tuổi · SV năm 2 · học trên campus", "PRIMARY", ["Học nhiều slot liền, nghỉ 15 phút giữa hai slot", "Android, cầm máy một tay, mạng chập chờn"], "Đặt xong dưới 35 giây, tối đa 8 chạm"),
            ("L", "Trần Mỹ Linh", "19 tuổi · SV năm 1 Thiết kế · đi xe buýt", "SECONDARY", ["Ngân sách khoảng 40.000đ mỗi ngày", "iPhone cũ, ví MoMo, dùng hai tay"], "Thấy tổng tiền thật trước khi trả"),
            ("H", "Cô Hạnh", "Khoảng 40 tuổi · nhân viên quầy Kiosk", "SUPPORTING", ["Vừa nấu vừa trả món, tay bận", "Không dùng app khách"], "Trả một món đặt trước trong khoảng 30 giây"),
            ("T", "Tuấn và Hà", "SV năm 3–4 · ít lên trường", "ANTI-PERSONA", ["Mua ở trường rất ít, mang cơm", "Không muốn tải thêm app"], "Không nhắm tới; ghi thành rủi ro R2")]
for i, (ch, name, role, tag, lines, goal) in enumerate(personas):
    x = 0.6 + i * 3.07
    box(s, x, 1.6, 2.95, 4.5)
    box(s, x + 0.25, 1.85, 0.7, 0.7, fill=ORANGE if i < 3 else BORDER, line=None, shape=MSO_SHAPE.OVAL)
    text(s, x + 0.25, 1.85, 0.7, 0.7, [(ch, 22, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    chip(s, x + 1.05, 2.0, 1.7, tag, size=10, h=0.3)
    text(s, x + 0.25, 2.75, 2.5, 3.3, [(name, 15, True, BROWN), (role, 11, False, MUTED)] + [(l, 12, False, BROWN) for l in lines] + [("Mục tiêu: " + goal, 12, True, ORANGE_D)], gap=7)
band(s, 6.25, "Persona là proto-persona, dựng từ quan sát của nhóm và dữ liệu mô phỏng; mỗi trường gắn nhãn bằng chứng.", h=0.6, size=12)

# =============================================================== 10 · P2 user story
s = content_slide("User story chính", "12 story, mỗi story có tiêu chí chấp nhận đo được", "cart", "03-P2-ux-design/03-p2-ux-design.md mục 3", "P2 · UX Design")
box(s, 0.6, 1.6, 12.15, 4.7)
table(s, 0.8, 1.75, 11.75, [["ID", "Persona", "Tôi muốn", "Tiêu chí chấp nhận"],
                            ["US01", "P01", "Đặt và trả tiền trước khi xuống quầy", "Từ S02 tới mã nhận đồ ở S07 trong tối đa 8 chạm"],
                            ["US03", "P01", "Thấy quán mở hay tạm dừng nhận đơn", "Badge icon và chữ ở S02; quán đóng thì tắt nút đặt"],
                            ["US05", "P01", "Bấm mọi nút chính bằng ngón cái", "Nút chính ở nửa dưới; vùng chạm từ 48 × 48 dp"],
                            ["US06", "P01", "Giữ giỏ hàng khi thanh toán lỗi", "S06-ERR giữ giỏ; có Thử lại và Trả tiền mặt"],
                            ["US08", "P02", "Thấy giá cộng dồn và tổng tiền ở giỏ", "Giá trên nút ở S04 cập nhật ngay; S05 hiện tổng"],
                            ["US10", "P03", "Đọc nhanh mã nhận và trạng thái trả tiền", "S07 có mã lớn, QR, badge Đã thanh toán / Trả tại quầy"]],
      [0.8, 1.0, 4.3, 5.65], row_h=0.62, size=12)
band(s, 6.45, "Chuỗi truy vết: Insight → Need → User story → Flow → Screen → Test (03-P2-ux-design/02-persona-mapping.xlsx).", h=0.45, size=12)

# =============================================================== 11 · P2 kiến trúc thông tin
s = content_slide("Kiến trúc thông tin", "Thanh dưới 4 tab cho app khách, 4 tab cho app người bán", "location",
                  "03-P2-ux-design/04-user-flow.md mục 1 · 05-P4-ui-design/02-screens-s09-s30.md", "P2 · UX Design")
box(s, 5.4, 1.55, 2.5, 0.5, fill=ORANGE, line=None, radius=0.5)
text(s, 5.4, 1.55, 2.5, 0.5, [("S01 Onboarding · lần đầu", 13, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
tabs = [("Trang chủ · S02", ["S04 Chi tiết món", "S05 Giỏ hàng", "S06 Thanh toán", "S07 Theo dõi đơn", "S14 Đặt lại nhanh",
                              "S19 Thông báo", "S21 Quán đóng", "S25 Hẹn giờ", "S27 Chọn kiosk", "S28 Tìm kiếm"]),
        ("Thực đơn · S03", ["S04 Chi tiết món", "S22 Món hết, gợi ý thay", "S28 Tìm kiếm", "S29 Mã giảm giá"]),
        ("Đơn hàng · S08", ["S07 Theo dõi đơn", "S09 Sửa đơn", "S10 Đơn đã huỷ", "S11 Lịch sử", "S12 Chi tiết đơn",
                             "S20 Nhận món (QR)", "S23 Đánh giá", "S24 Báo sự cố"]),
        ("Cá nhân · S15", ["S16 Hồ sơ", "S17 Phương thức thanh toán", "S18 Cài đặt thông báo", "S13 Món yêu thích", "S26 Đăng nhập"])]
for i, (head, kids) in enumerate(tabs):
    x = 0.6 + i * 3.07
    box(s, x, 2.3, 2.95, 3.65)
    box(s, x, 2.3, 2.95, 0.55, fill=SELECT, line=None)
    text(s, x, 2.3, 2.95, 0.55, [(head, 14, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    text(s, x + 0.2, 3.0, 2.6, 2.9, [(k, 12, False, MUTED) for k in kids], gap=2)
band(s, 6.1, "App người bán (K01–K15): Đơn · Quét mã · Món · Quán, gồm nhận đơn, làm món, giao món, quản lý món và quán, thống kê ca, xử lý sự cố")

# =============================================================== 12 · P2 ba flow chính
s = content_slide("Ba flow chính", "Mỗi flow có đầu vào, đầu ra và nhánh lỗi; ảnh là màn Figma thật", "cart", "03-P2-ux-design/04-user-flow.md mục 2 · Figma Page 01 (UF · F1–F3)", "P2 · UX Design")
flows = [("F1", "Đặt nhanh, nhận tại quầy", "Dưới 35 giây, tối đa 8 chạm",
          ["S02", "S04", "S05", "S06", "S07"], ["", "Chạm combo", "Thêm vào giỏ", "Thanh toán", "Xác nhận"]),
         ("F2", "Tuỳ chỉnh món và mã giảm giá", "Mã sai báo lỗi ngay tại giỏ hàng",
          ["S03", "S04", "S05", "S29", "S05-VOUCHER-ERR"], ["", "Chọn món", "Thêm vào giỏ", "Nhập mã", "!Mã hết hạn"]),
         ("F3", "Lỗi thanh toán và phục hồi", "Giỏ hàng được giữ, đơn vẫn được tạo",
          ["S06-ERR", "S07-CASH", "S07-DIALOG", "S10"], ["", "!Tiền mặt", "Huỷ đơn", "Xác nhận huỷ"])]
for i, (code, title, out, scr, labs) in enumerate(flows):
    y = 1.55 + i * 1.52
    box(s, 0.6, y, 12.15, 1.42)
    chip(s, 0.8, y + 0.15, 0.6, code, size=12)
    text(s, 0.8, y + 0.55, 2.5, 0.5, [(title, 13, True, BROWN)])
    text(s, 0.8, y + 1.0, 2.5, 0.4, [(out, 10, True, ORANGE_D)])
    arrow_row(s, 3.55, y + 0.07, 1.28, scr, labs, gap=1.3)
band(s, 6.2, "Flow F4–F13, đăng nhập và ba flow người bán nằm ở Figma Page 01, mỗi flow có điểm chạm, nhánh lỗi, đầu vào và đầu ra.", h=0.6, size=12, bold=False)

# =============================================================== 13 · P2 wireframe
s = content_slide("Wireframe và flow mở rộng", "Chốt bố cục bằng khung xám trước khi chọn màu", "receipt", "Figma Page 02 · Figma Page 02 (WF v2)", "P2 · UX Design")
x = 0.62
for nm in ["S02", "S03", "S04", "S05", "S06", "S07", "S08", "S15"]:
    w = gray_phone(s, nm + ".png", x, 1.55, 3.0)
    x += w + 0.1
box(s, 0.6, 4.75, 5.95, 1.3)
text(s, 0.8, 4.85, 5.6, 1.15, [("WIREFRAME · FIGMA PAGE 02", 11, True, MUTED),
                               ("Khung xám cho cả S01–S30 và app người bán, không màu, chỉ thứ bậc khối và một nút chính", 12, False, BROWN)], gap=4)
box(s, 6.8, 4.75, 5.95, 1.3)
text(s, 7.0, 4.85, 5.6, 1.15, [("FLOW MỞ RỘNG · FIGMA PAGE 01", 11, True, MUTED),
                               ("F4–F13: sửa và huỷ đơn, lịch sử, yêu thích, hồ sơ, thông báo, quán đóng, món hết, đánh giá, mất mạng, đang tải", 12, False, BROWN)], gap=4)
band(s, 6.2, "Walkthrough hiện do AI thực hiện; nhóm chưa đi thử luồng với người thật.", h=0.6, size=12)

# =============================================================== 14 · P3 Stitch
s = content_slide("Tạo giao diện với Google Stitch", "Brief có cấu trúc, không gõ prompt tự do", "restaurant", "04-P3-ui-concept/01-DESIGN.md · 08-ai-log/01-ai-design-log.md mục 2", "P3 · UI Concept")
steps = [("DESIGN.md", "Persona, màu, chữ, nguyên tắc thiết kế (DP1–DP8) viết trước khi mở Stitch"),
         ("Prompt gửi Stitch", "Vai trò nhà thiết kế sản phẩm, app đặt món cho sinh viên chỉ có 15 phút, light theme"),
         ("Bốn màn ban đầu", "Trang chủ, chi tiết món, giỏ hàng, theo dõi đơn"),
         ("Nhật ký", "Prompt nguyên văn và ảnh lưu trong ai-design-log.md và assets/stitch/")]
for i, (head, sub) in enumerate(steps):
    x = 0.6 + i * 3.07
    box(s, x, 1.7, 2.95, 2.4)
    chip(s, x + 0.25, 1.9, 0.5, str(i + 1), size=12)
    text(s, x + 0.25, 2.4, 2.5, 1.6, [(head, 15, True, BROWN, HEAD), (sub, 12, False, MUTED)], gap=5)
box(s, 0.6, 4.35, 12.15, 2.4, fill=SELECT, line=None)
text(s, 0.85, 4.5, 11.65, 2.2, [
    ("VÌ SAO CÓ BRIEF TRƯỚC", 11, True, MUTED),
    ("Prompt nêu ràng buộc thật: người dùng một tay, giờ nghỉ 15 phút, chữ tối thiểu 14 sp, vùng chạm 48 dp, tương phản 4,5:1.", 14, False, BROWN),
    ("Kết quả của AI là bản nháp để phản biện, không phải thiết kế cuối.", 14, True, ORANGE_D),
], gap=9)

# =============================================================== 15 · P3 ba hướng visual
s = content_slide("Ba hướng visual cho màn Trang chủ", "So sánh cùng nội dung, cùng khung 360 × 800", "offer", "04-P3-ui-concept/02-p3-ui-concept-style-guide.md mục 1", "P3 · UI Concept")
pic(s, os.path.join(ROOT, "assets", "concepts", "concept-board-breakbite.png"), 1.6, 1.6, h=4.25)
box(s, 8.55, 1.6, 4.2, 3.0)
table(s, 8.7, 1.75, 3.9, [["Tiêu chí", "A", "B", "C"], ["Đọc ngoài nắng", "4", "5", "2"], ["Quét nhanh", "3", "5", "2"], ["Chọn bằng ảnh", "5", "1", "4"],
                          ["Trạng thái quán", "3", "5", "3"], ["Thương hiệu", "5", "2", "3"], ["Light theme", "5", "5", "1"], ["Tổng", "25", "23", "15"]],
      [1.9, 0.67, 0.67, 0.66], row_h=0.34, size=11)
box(s, 8.55, 4.75, 4.2, 1.1, fill=GREEN_BG, line=GREEN)
text(s, 8.75, 4.83, 3.8, 1.0, [("D33 · MODIFY", 11, True, GREEN), ("Chọn A, mượn khối trạng thái quán và banner nhỏ của B", 12, False, BROWN)], gap=3)
box(s, 0.6, 5.95, 7.7, 0.85, fill=RED_BG, line=RED)
text(s, 0.85, 5.95, 7.3, 0.85, [("D34 · REJECT concept C: nền tối đọc kém ngoài nắng, banner che món, đề bắt buộc light theme", 12, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
text(s, 8.55, 5.95, 4.2, 0.85, [("A là Stitch; B và C do AI dựng bằng HTML, ghi rõ nguồn (D35).", 11, False, MUTED)], anchor=MSO_ANCHOR.MIDDLE)

# =============================================================== 16 · P3 AI phản biện và vòng lặp
s = content_slide("AI phản biện và ba vòng tinh chỉnh", "Đánh giá theo 10 heuristic của Nielsen, WCAG và persona", "error", "08-ai-log/01-ai-design-log.md mục 3–4", "P3 · UI Concept")
its = [("I01", "CTA khó đọc, bị chìm", "Chữ trắng trên cam tương phản thấp, nút chính yếu về thị giác", "Đổi chữ nút sang nâu; tăng phân cấp CTA"),
       ("I02", "Thiếu giỏ trống, dễ xoá nhầm", "Không có trạng thái rỗng, xoá món không có lối quay lại", "Thêm màn giỏ trống và xác nhận khi xoá"),
       ("I03", "Lỗi thanh toán là ngõ cụt", "Báo lỗi nhưng không có đường đi tiếp, giỏ có thể mất", "Thêm màn phục hồi: giữ giỏ, thử lại, trả tiền mặt")]
for i, (code, head, issue, fix) in enumerate(its):
    x = 0.6 + i * 4.1
    box(s, x, 1.6, 3.95, 3.85)
    chip(s, x + 0.25, 1.8, 0.7, code, size=12)
    text(s, x + 0.25, 2.3, 3.45, 3.1, [(head, 15, True, BROWN, HEAD), ("Vấn đề: " + issue, 12, False, MUTED), ("Sửa: " + fix, 12, True, ORANGE_D)], gap=8)
band(s, 5.65, "Gemini phản biện (tóm tắt), Claude phản biện (nguyên văn, Phụ lục A); nhóm tự đo lại số liệu AI nêu.", h=0.65, size=12)
band(s, 6.4, "Chữ trắng trên cam đo thật 2,14:1, không phải mức AI nêu; chữ nút nâu đạt 5,23:1.", h=0.45, size=12, fill=CARD)

# =============================================================== 17 · P3 quyết định
s = content_slide("Quyết định Accept, Modify, Reject", "Mọi đề xuất của AI đều ghi quyết định và lý do trong nhật ký", "check", "08-ai-log/01-ai-design-log.md · 05-P4-ui-design/05-design-decisions.md", "P3 · UI Concept")
cols = [("ACCEPT", GREEN, GREEN_BG, ["Giá cộng dồn trên nút Thêm vào giỏ (S04)", "D19 · thêm chỉ số kết quả vào P0", "D21 · thêm giả định về năng lực bếp"]),
        ("MODIFY", ORANGE_D, SELECT, ["Chữ nút đổi sang nâu #622B14, tương phản 5,23:1", "D18 · bỏ giải pháp khỏi problem statement", "D33 · chọn concept A, mượn khối trạng thái của B"]),
        ("REJECT", RED, RED_BG, ["D20 · chuyển sang web QR (đề bắt buộc app mobile)", "D34 · concept C nền tối (đề bắt buộc light theme)", "Bắt buộc đăng nhập để tích điểm (D12)"])]
for i, (tag, col, fill, items_) in enumerate(cols):
    x = 0.6 + i * 4.1
    box(s, x, 1.6, 3.95, 4.3)
    chip(s, x + 0.25, 1.8, 1.2, tag, fill=fill, color=col, line=col, size=12)
    text(s, x + 0.25, 2.4, 3.45, 3.4, [(t, 13, False, BROWN) for t in items_], gap=14)
band(s, 6.1, "Hơn 40 quyết định (D01–D43), mỗi quyết định có căn cứ: persona, heuristic hoặc ràng buộc của đề.", h=0.7, size=13)

# =============================================================== 18 · P3 style guide
s = content_slide("App Style Guide", "Token màu, chữ, khoảng cách và component dùng chung cho hai app", "offer", "04-P3-ui-concept/01-DESIGN.md · Figma Page 04, 05", "P3 · UI Concept")
box(s, 0.6, 1.6, 7.2, 5.2)
text(s, 0.85, 1.75, 6.7, 0.35, [("MÀU", 11, True, MUTED)])
sw = [("#F69D39", "primary", ORANGE), ("#622B14", "chữ, trên cam", BROWN), ("#B45309", "chữ nhấn", ORANGE_D), ("#15803D", "thành công", GREEN),
      ("#B91C1C", "lỗi", RED), ("#FAF8F5", "nền", BG), ("#FFFFFF", "thẻ", CARD), ("#E4DFD8", "viền", BORDER), ("#FFF1DE", "đang chọn", SELECT), ("#6B5F55", "chữ phụ", MUTED)]
for i, (hx, role, col) in enumerate(sw):
    x, y = 0.85 + (i % 5) * 1.3, 2.2 + (i // 5) * 1.6
    box(s, x, y, 1.15, 0.85, fill=col, line=BORDER, radius=0.15)
    text(s, x, y + 0.92, 1.2, 0.55, [(hx, 11, True, BROWN), (role, 10, False, MUTED)], gap=0)
text(s, 0.85, 5.55, 6.7, 1.1, [("Cam chỉ cho một nút chính mỗi màn và trạng thái đang chọn. Nền và thẻ là các tông trung tính ấm.", 12, False, MUTED)])
box(s, 8.05, 1.6, 4.7, 5.2)
text(s, 8.3, 1.75, 4.2, 2.4, [
    ("CHỮ · Nunito", 11, True, MUTED),
    ("Display 24 sp · Bold", 17, True, BROWN, HEAD),
    ("Headline 20 sp · Bold", 15, True, BROWN, HEAD),
    ("Title 16 sp · SemiBold", 13, True, BROWN),
    ("Body 14 sp · Regular", 12, False, BROWN),
    ("Lưới 4 dp · lề 16 dp · bo góc 8, 12, 16, 24", 11, False, MUTED),
], gap=5)
text(s, 8.3, 4.2, 4.2, 0.3, [("ICON · 27 icon vector một nét", 11, True, MUTED)])
for i, nm in enumerate(["restaurant", "cafe", "receipt", "qr", "location", "schedule"]):
    icon(s, nm, 8.3 + i * 0.68, 4.6, 0.55)
text(s, 8.3, 5.4, 4.2, 1.3, [("Component: Chip, NavBar, Card/Food, IconButton, Button, Dialog, có variant theo trạng thái.", 12, False, MUTED)])

# =============================================================== 19 · P4 phản biện giao diện → v2
s = content_slide("Phản biện giao diện và bản v2", "Đo bản cũ, sửa, đo lại", "error", "05-P4-ui-design/06-phan-bien-giao-dien/ · tests/audit/", "P4 · UI Design")
box(s, 0.6, 1.6, 7.0, 4.95)
table(s, 0.85, 1.85, 6.5, [["Chỉ số", "Bản cũ", "Bản v2"],
                           ["Cam đậm (trung bình S01–S08)", "5,9%", "4,3%"],
                           ["Họ cam–be: nền, thẻ, chip", "55,3%", "4,4%"],
                           ["Emoji trong chữ", "98 / 366", "0"],
                           ["Chữ dưới 14 sp", "86 dòng", "0*"],
                           ["Chữ thiếu tương phản", "8 chỗ", "0"],
                           ["Vùng bấm dưới 48 dp", "20 / 39", "0 / 262"]],
      [3.5, 1.5, 1.5], row_h=0.55, size=14)
text(s, 0.85, 5.9, 6.5, 0.5, [("* trừ nhãn thanh dưới 12 sp. Nền v2 là #FAF8F5 nên không còn tính vào họ cam–be.", 10, False, MUTED)])
bullets_card(s, 7.85, 1.6, 4.9, 4.95, "LỖI CHÍNH ĐÃ SỬA", ["Quá cam: nền kem trung tính, cam chỉ cho một nút chính", "Icon lộn xộn: bỏ emoji, dùng một bộ 27 icon vector",
                                                              "Giỏ hàng và thanh toán lặp: tách S05 và S06", "Vùng bấm 48 dp, chữ 14 sp, chữ cam đủ 4,5:1",
                                                              "Báo cáo đo do công cụ AI viết nên không độc lập; phản biện của AI khác chưa chạy."], size=13, gap=9)

# =============================================================== 20 · P4 Final UI S01–S08
s = content_slide("Final UI: luồng đặt món", "S01–S08 bản v2, một nút cam mỗi màn", "restaurant", "assets/figma/final-ui-v2/ · Figma Page 03", "P4 · UI Design")
labels = ["S01 Onboarding", "S02 Trang chủ", "S03 Thực đơn", "S04 Chi tiết món", "S05 Giỏ hàng", "S06 Thanh toán", "S07 Theo dõi", "S08 Đơn hàng"]
for i, (nm, lb) in enumerate(zip(["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08"], labels)):
    x = 0.62 + i * 1.53
    phone(s, nm + ".png", x, 1.65, 3.15)
    text(s, x - 0.05, 4.9, 1.5, 0.5, [(lb, 11, True, BROWN)])
box(s, 0.6, 5.65, 12.1, 1.1, fill=SELECT, line=None)
text(s, 0.85, 5.7, 11.6, 1.0, [("Nền kem trung tính, thẻ trắng, một bộ icon vector, vùng bấm từ 48 dp, chữ từ 14 sp", 13, True, BROWN),
                                ("Màn lõi của ba flow chính; mỗi màn có trạng thái rỗng, lỗi hoặc đang tải đi kèm", 12, False, MUTED)],
     anchor=MSO_ANCHOR.MIDDLE, gap=6)

# =============================================================== 21 · P4 trạng thái hệ thống
s = content_slide("Trạng thái hệ thống", "Phản hồi rõ ràng và luôn có hướng xử lý tiếp", "check", "assets/figma/final-ui-v2/ · Figma Page 03", "P4 · UI Design")
states = [("EMPTY", "S05-EMPTY", "Giỏ hàng trống, gợi ý món", "S05-EMPTY.png", ORANGE_D),
          ("LOADING", "S06-LOADING", "Đang kết nối cổng thanh toán", "S06-LOADING.png", BROWN),
          ("ERROR", "S06-ERR", "Thanh toán lỗi, giỏ hàng vẫn được giữ", "S06-ERR.png", RED),
          ("SUCCESS", "S07", "Đã nhận đơn, mã QR và 4 bước", "S07.png", GREEN)]
for i, (tag, code, desc, fn, col) in enumerate(states):
    x = 0.6 + i * 3.07
    box(s, x, 1.6, 2.95, 5.2)
    text(s, x, 1.7, 2.95, 0.4, [(tag, 16, True, col, HEAD)], align=PP_ALIGN.CENTER)
    text(s, x + 0.15, 2.1, 2.65, 0.55, [(code + " · " + desc, 11, False, MUTED)], align=PP_ALIGN.CENTER)
    phone(s, fn, x + 0.57, 2.75, 3.85 * 1.0)

# =============================================================== 22 · P4 Final UI S09–S30
s = content_slide("Final UI: vòng đời đơn và tài khoản", "S09–S30 bản v2", "receipt", "05-P4-ui-design/02-screens-s09-s30.md · assets/figma/final-ui-v2/", "P4 · UI Design")
sheet(s, "contact-sheet-s09-s25.png", 0.6, 1.6, 4.4)
sheet(s, "contact-sheet-s26-s30.png", 4.85, 1.6, 4.4)
box(s, 9.2, 1.6, 3.55, 4.4)
text(s, 9.4, 1.75, 3.2, 4.2, [
    ("S09–S14", 13, True, ORANGE_D), ("Sửa và huỷ đơn, lịch sử, yêu thích, đặt lại", 12, False, BROWN),
    ("S15–S20", 13, True, ORANGE_D), ("Tài khoản, thông báo, nhận món bằng QR", 12, False, BROWN),
    ("S21–S25", 13, True, ORANGE_D), ("Quán đóng, món hết, đánh giá, báo sự cố, hẹn giờ", 12, False, BROWN),
    ("S26–S30", 13, True, ORANGE_D), ("Đăng nhập, chọn kiosk, tìm kiếm, mã giảm giá, mất mạng", 12, False, BROWN),
], gap=4)
text(s, 0.6, 6.15, 12.1, 0.6, [("Tìm kiếm trống, mã hết hạn, lỗi mạng và trạng thái tải đều có màn riêng; đăng nhập không bắt buộc.", 12, False, MUTED)])

# =============================================================== 23 · P4 app người bán
s = content_slide("App người bán: BreakBite Kiosk", "15 màn K01–K15 cho nhân viên quầy", "cafe", "05-P4-ui-design/03-kitchen-app.md · assets/figma/final-ui-v2/kitchen/", "P4 · UI Design")
bullets_card(s, 0.6, 1.6, 6.9, 3.0, "MÀN KHÁCH ĐÃ HỨA, QUẦY PHẢI THỰC HIỆN", [
    "Đã nhận, Đang làm, Sẵn sàng: nhận đơn, làm món, báo sẵn sàng", "Mã QR: quét mã, xác nhận giao; trả tại quầy thì thu tiền rồi giao",
    "Tạm hết: đánh dấu hết món, thêm và sửa món", "Quán đóng: bật hoặc tắt nhận đơn", "Huỷ đơn, sự cố: từ chối đơn, hoàn tiền"], size=13, gap=7)
box(s, 0.6, 4.8, 6.9, 1.95, fill=SELECT, line=None)
text(s, 0.85, 4.95, 6.4, 1.7, [
    ("Một nút cam mỗi màn; thanh toán luôn hiện trên thẻ đơn để biết đơn nào thu tiền mặt.", 13, True, BROWN),
    ("Bốn tab: Đơn, Quét mã, Món, Quán. Thống kê ca nằm trong tab Quán, xử lý sự cố mở từ tab Đơn.", 12, False, MUTED)], gap=8)
sheet(s, "contact-sheet-kitchen.png", 7.8, 1.6, 4.9)

# =============================================================== 24–25 · P4 ánh xạ pain point → màn hình
PAINS = [
    ("P1", "Hàng chờ đúng giờ nghỉ", "Đặt từ lớp, hẹn giờ nhận, nhận bằng mã QR, không xếp hàng", ["S02", "S25", "S07", "S20"]),
    ("P2", "Không biết quán còn mở, còn món, bao lâu xong", "Trạng thái quán và món hiện ngay, gợi ý món thay, giờ dự kiến sẵn sàng", ["S21", "S22", "S05", "S19"]),
    ("P3", "Ngại phí ẩn, tổng tiền chỉ hiện ở bước cuối", "Giá cộng dồn trên nút, tổng chi tiết từ giỏ, mã giảm giá rõ ràng", ["S04", "S05", "S29", "S06"]),
    ("P4", "Lỗi thanh toán làm mất giỏ hàng", "Giữ giỏ hàng, thử lại hoặc trả tiền mặt tại Kiosk, báo mất kết nối", ["S06-ERR", "S07-CASH", "S30", "S05"]),
    ("P5", "Nút nhỏ, khó bấm một tay khi đi bộ", "Vùng bấm từ 48 dp, nút chính ở đáy màn, một nút cam mỗi màn", ["S02", "S04", "S05", "S08"]),
    ("P6", "Người bán: khách đứng chờ kiểm tra chuyển khoản, huỷ khi món đã nấu", "Đơn đã thanh toán hiện sẵn, quét QR giao món, hộp thoại từ chối đơn", ["kitchen/K02", "kitchen/K03", "kitchen/K05", "kitchen/K12"]),
]
for part, (title, sub, rows_) in enumerate([("Ánh xạ pain point → màn hình (1/2)", "Pain point của khách và màn hình xử lý", PAINS[:3]),
                                           ("Ánh xạ pain point → màn hình (2/2)", "Lỗi thanh toán, thao tác một tay và phía người bán", PAINS[3:])]):
    s = content_slide(title, sub, "check", "03-P2-ux-design/05-anh-xa-painpoint-man-hinh.md · Figma Page 01 (MAP)", "P4 · UI Design")
    text(s, 0.75, 1.5, 3.2, 0.3, [("PAIN POINT", 11, True, MUTED)])
    text(s, 4.2, 1.5, 3.2, 0.3, [("GIẢI PHÁP THIẾT KẾ", 11, True, MUTED)])
    text(s, 7.75, 1.5, 3.2, 0.3, [("MÀN HÌNH GIẢI QUYẾT", 11, True, MUTED)])
    for i, (code, pain, sol, scr) in enumerate(rows_):
        y = 1.8 + i * 1.55
        seller = code == "P6"
        box(s, 0.6, y, 12.15, 1.45)
        box(s, 0.75, y + 0.1, 3.25, 1.25, fill=BROWN if seller else SELECT, line=None, radius=0.1)
        chip(s, 0.9, y + 0.18, 0.55, code, size=11, h=0.3)
        text(s, 0.9, y + 0.52, 2.95, 0.8, [(pain, 12, True, CARD if seller else BROWN)])
        text(s, 4.5, y + 0.1, 2.95, 1.25, [(sol, 12, False, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
        text(s, 4.1, y + 0.45, 0.35, 0.5, [("→", 18, True, ORANGE)])
        x = 7.75
        for nm in scr:
            iw_, ih_ = Image.open(os.path.join(IMG, nm + ".png")).size
            hh = min(1.1, 1.7 * ih_ / iw_)
            w = phone(s, nm + ".png", x, y + 0.05 + (1.1 - hh) / 2, hh)
            text(s, x - 0.15, y + 1.17, w + 0.3, 0.25, [(nm.split("/")[-1], 9, True, MUTED)], align=PP_ALIGN.CENTER)
            x += w + 0.75
    if part == 1:
        band(s, 6.5, "Nguồn pain point: 03-P2-ux-design/01-persona.md và 02-P1-nghien-cuu/02-research.md; dữ liệu persona là giả định, chờ khảo sát thật.", h=0.38, size=11, bold=False)

# =============================================================== 26 · P4 sáu page Figma
s = content_slide("Bản vẽ trong Figma", "Sáu page, từ user flow tới prototype chạy được", "location", "Figma PRM323 (bản copy) · assets/figma/boards/", "P4 · UI Design")
BO = os.path.join(ROOT, "assets", "figma", "boards")
cells = [("Page 01 · User flow", "Storyboard F1–F13, đăng nhập, người bán, bảng ánh xạ pain point", os.path.join(BO, "user-flow-f1.png")),
         ("Page 02 · Wireframe", "Khung xám cho S01–S30 và K01–K15", os.path.join(BO, "wireframe-s01-s30.png")),
         ("Page 03 · Final UI", "64 màn v2, bản 360 và 412 dp", os.path.join(IMG, "contact-sheet-s01-s08.png")),
         ("Page 04 · Design system", "Token màu, chữ, khoảng cách, bo góc, 27 icon", os.path.join(BO, "design-system.png")),
         ("Page 05 · Component", "Chip, NavBar, Card, nút; mọi variant", os.path.join(BO, "components.png")),
         ("Page 06 · Prototype", "64 màn nối liên kết, 19 điểm bắt đầu để Present", os.path.join(BO, "prototype-index.png"))]
for i, (head_, desc, path) in enumerate(cells):
    x, y = 0.6 + (i % 3) * 4.1, 1.55 + (i // 3) * 2.62
    cover(s, path, x, y, 3.95, 1.95)
    text(s, x, y + 2.0, 3.95, 0.6, [(head_, 13, True, BROWN), (desc, 11, False, MUTED)], gap=0)

# =============================================================== 27 · P4 component và responsive
s = content_slide("Component và responsive", "Một thư viện component, bản 360 dp và 412 dp cho mỗi màn", "wallet", "Figma Page 05 · assets/figma/final-ui-v2/412/", "P4 · UI Design")
box(s, 0.6, 1.6, 4.6, 5.2)
text(s, 0.85, 1.75, 4.1, 5.0, [
    ("COMPONENT CÓ VARIANT", 11, True, MUTED),
    ("Button: mặc định, nhấn, vô hiệu, đang tải", 13, False, BROWN),
    ("Chip: mặc định, đang chọn", 13, False, BROWN),
    ("Card/Food: món, đồ uống, hết hàng", 13, False, BROWN),
    ("NavBar: 4 tab, tab đang chọn", 13, False, BROWN),
    ("IconButton 48 × 48, Dialog, TextField", 13, False, BROWN),
    ("Màn dùng instance và token, không hard-code màu", 12, True, ORANGE_D),
], gap=10)
box(s, 5.45, 1.6, 7.3, 5.2)
text(s, 5.7, 1.75, 6.8, 0.3, [("360 DP VÀ 412 DP", 11, True, MUTED)])
x = 5.75
for nm, hh in [("S02.png", 3.5), ("412/S02.png", 3.5), ("S05.png", 3.5), ("412/S05.png", 3.5)]:
    w = phone(s, nm, x, 2.2, hh)
    x += w + 0.14
text(s, 5.7, 5.85, 6.8, 0.9, [("S02 và S05 ở 360 dp rồi 412 dp. Bản 412 dp dựng bằng constraints nên nội dung co giãn, không cuộn ngang.", 12, False, MUTED)])

# =============================================================== 25 · P4 prototype
s = content_slide("Prototype Figma", "Nối cả hai app, chạy từng flow bằng Present trên Page 06", "qr", "Figma Page 03, 06 · tests/figma-proto/hotspots-v2.json", "P4 · UI Design")
bullets_card(s, 0.6, 1.6, 5.9, 3.3, "PROTOTYPE BẢN V2", ["Hơn 260 vùng bấm trên 64 khung, 19 điểm bắt đầu", "Dialog huỷ đơn và từ chối đơn dạng overlay",
                                                         "Thêm vào giỏ, chọn phương thức, cổng thanh toán thành công hoặc bị từ chối", "Back đúng, không màn cụt, không màn mồ côi"], size=13, gap=9)
box(s, 6.75, 1.6, 6.0, 3.3)
text(s, 7.0, 1.75, 5.5, 3.1, [("ĐIỂM BẮT ĐẦU KHI DEMO", 11, True, MUTED),
                               ("F1 · S02 đặt nhanh từ Trang chủ", 13, False, BROWN), ("F2 · S03 tuỳ chỉnh và mã giảm giá", 13, False, BROWN),
                               ("F3 · S06-ERR lỗi thanh toán", 13, False, BROWN), ("F4 · S08 sửa và huỷ đơn", 13, False, BROWN),
                               ("K1 · K01 người bán nhận đơn và chuẩn bị", 13, False, BROWN)], gap=7)
band(s, 5.1, "Demo: chạm + → Xem giỏ → Tiếp tục thanh toán → chọn phương thức → xác nhận → cổng thanh toán → mã nhận #A-204; rồi mở app người bán nhận đơn đó.", h=0.8, size=13)
band(s, 6.05, "Thử link Figma bằng cửa sổ chưa đăng nhập trước khi trình bày.", h=0.6, size=12, bold=False, fill=CARD)

# =============================================================== 26 · P5 accessibility
s = content_slide("Accessibility", "Đo bằng công cụ, không ước lượng bằng mắt", "check", "05-P4-ui-design/05-design-decisions.md · tests/audit/", "P5 · Validation")
stats = [("5,23:1", "chữ nút nâu trên cam", "ngưỡng WCAG 4,5:1"), ("48 dp", "vùng bấm nhỏ nhất", "0 / 262 vùng dưới 48 dp"),
         ("14 sp", "chữ nội dung nhỏ nhất", "nhãn thanh dưới 12 sp"), ("0", "emoji trong giao diện", "một bộ 27 icon vector")]
for i, (big, label, sub) in enumerate(stats):
    x = 0.6 + i * 3.07
    box(s, x, 1.6, 2.95, 2.0, fill=SELECT, line=None)
    text(s, x + 0.25, 1.75, 2.5, 0.8, [(big, 30, True, ORANGE_D, HEAD)])
    text(s, x + 0.25, 2.65, 2.5, 0.9, [(label, 13, True, BROWN), (sub, 11, False, MUTED)], gap=2)
bullets_card(s, 0.6, 3.85, 7.4, 2.95, "CÁCH KIỂM", ["Tương phản tính bằng công thức WCAG 2.2 trên giá trị màu thật", "Trạng thái luôn có chữ hoặc icon đi kèm màu",
                                                    "Chữ và vùng bấm kiểm trên 114 khung bằng Figma Plugin API", "Không có chữ nào thiếu tương phản"], size=13, gap=8)
box(s, 8.25, 3.85, 4.5, 2.95, fill=SELECT, line=None)
text(s, 8.5, 4.0, 4.0, 2.7, [("CHƯA KIỂM", 11, True, MUTED), ("Trình đọc màn hình, cỡ chữ hệ thống lớn, người dùng thật khiếm thị", 13, False, BROWN)], gap=8)

# =============================================================== 27 · P5 kiểm thử
s = content_slide("Kiểm thử", "Playwright cho prototype; usability test với người thật đã có kế hoạch", "receipt", "tests/ · 06-P5-kiem-thu-ban-giao/", "P5 · Validation")
bullets_card(s, 0.6, 1.6, 5.9, 3.5, "KIỂM THỬ TỰ ĐỘNG · PLAYWRIGHT", ["Bản cũ: 13 / 13 test đạt, bấm theo toạ độ vùng bấm", "Đồ thị flow bản v2: 10 / 10 test đạt",
                                                                   "Đặt đơn từ Trang chủ tới Theo dõi đơn: 5 chạm, qua giỏ và cổng thanh toán", "Flow 3 có lối phục hồi về giỏ hàng"], size=13, gap=9)
box(s, 6.75, 1.6, 6.0, 3.5)
text(s, 7.0, 1.75, 5.5, 3.3, [("USABILITY TEST · KẾ HOẠCH (CHƯA CHẠY)", 11, True, MUTED),
                               ("T1 Đặt Combo Tacos, lấy sau 10 phút", 12, False, BROWN), ("T2 Chọn cay, topping, nhập mã giảm giá", 12, False, BROWN),
                               ("T3 Thanh toán MoMo lỗi, hoàn tất bằng cách khác", 12, False, BROWN), ("T4 Tìm lại đơn cũ và đặt lại", 12, False, BROWN),
                               ("T5 Đổi giờ nhận của đơn đang làm", 12, False, BROWN)], gap=7)
band(s, 5.3, "Đo: tỉ lệ hoàn thành, thời gian, số chạm, lỗi, điểm dễ dùng; 3–5 sinh viên, không hướng dẫn từng bước.", h=0.7, size=13)
band(s, 6.15, "Kiểm thử tự động chỉ chứng minh prototype đi đúng đường đã thiết kế; không thay usability test.", h=0.6, size=12, fill=RED_BG)

# =============================================================== 28 · P5 handoff
s = content_slide("Bàn giao cho Flutter", "Đặc tả đủ để lập trình viên dựng giao diện, không viết code", "wallet", "06-P5-kiem-thu-ban-giao/03-flutter-handoff.md", "P5 · Validation")
box(s, 0.6, 1.6, 5.9, 5.2)
text(s, 0.85, 1.75, 5.4, 0.3, [("TOKEN VÀ COMPONENT → FLUTTER", 11, True, MUTED)])
table(s, 0.85, 2.15, 5.4, [["Figma", "Flutter"], ["color/primary", "ColorScheme.primary"], ["color/v2-selected", "secondaryContainer"], ["Chip", "ChoiceChip, 48 dp"],
                           ["NavBar", "NavigationBar"], ["Card/Food", "Card + ListTile"], ["IconButton", "IconButton 48 × 48"]], [2.5, 2.9], row_h=0.5, size=13)
bullets_card(s, 6.75, 1.6, 6.0, 3.1, "SÁU MỤC CHO MỖI MÀN (S01–S30, K01–K15)", ["Layout · Components · States", "Tương tác · Điều hướng · Ràng buộc"], size=14, gap=10)
box(s, 6.75, 4.9, 6.0, 1.9, fill=SELECT, line=None)
text(s, 7.0, 5.05, 5.5, 1.7, [("HÀNH VI MÀN RỘNG", 11, True, MUTED), ("Từ 600 dp: NavigationRail, lưới 2–3 cột; từ 412 dp: Fill container", 13, False, BROWN)], gap=8)

# =============================================================== 29 · P5 Quality Gates
s = content_slide("Tự chấm theo Quality Gates", "Sáu gate của môn; kết quả tự chấm, chờ reviewer duyệt", "check", "00-quy-trinh/03-quy-chuan-ux-ui.md · skills/ · README.md mục 7", "P5 · Validation")
box(s, 0.6, 1.6, 7.7, 5.2)
gates = [("G0", "Problem", "Đạt 6/6", GREEN, GREEN_BG, "Problem statement, giả định, kế hoạch kiểm chứng"),
         ("G1", "Research", "Có điều kiện", ORANGE_D, SELECT, "Chưa có phản hồi khảo sát thật"),
         ("G2", "UX Design", "5 / 6", ORANGE_D, SELECT, "Chưa walkthrough với người thật"),
         ("G3", "UI Concept", "Đạt", GREEN, GREEN_BG, "Có 3 hướng, style guide, bản 412 dp"),
         ("G4", "UI Design", "Có điều kiện", ORANGE_D, SELECT, "Prototype v2 chưa chạy Present"),
         ("G5", "Validation", "Chưa test người", RED, RED_BG, "Cần usability test và xác nhận của dev")]
for i, (g, name, st, col, fill, note) in enumerate(gates):
    y = 1.8 + i * 0.82
    text(s, 0.85, y, 0.6, 0.6, [(g, 15, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 1.5, y, 1.5, 0.6, [(name, 13, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    chip(s, 3.0, y + 0.13, 1.85, st, fill=fill, color=col, line=col, size=11, h=0.34)
    text(s, 5.0, y, 3.15, 0.6, [(note, 11, False, MUTED)], anchor=MSO_ANCHOR.MIDDLE)
bullets_card(s, 8.55, 1.6, 4.2, 2.6, "THANG ĐIỂM", ["80% trở lên và mọi Critical đạt: Đạt", "70–79%: Cần cải thiện", "Dưới 70%: Cần làm lại", "Critical trượt: chưa qua"], size=12, gap=6)
box(s, 8.55, 4.4, 4.2, 2.4, fill=SELECT, line=None)
text(s, 8.8, 4.55, 3.7, 2.2, [("LƯU Ý", 11, True, MUTED), ("Gate và ngưỡng 80% là rubric nội bộ của môn, không phải chuẩn quốc tế. Contrast dựa trên WCAG 2.2. Bộ 13 skill trong thư mục skills/ chấm từng gate.", 12, False, BROWN)], gap=8)

# =============================================================== 30 · tổng kết
s = content_slide("Tổng kết", "Ăn kịp giờ nghỉ, không phải xếp hàng", "restaurant", "README.md · README.md mục 7")
cols = [("AI giúp", ["Sinh UI ban đầu nhanh (Stitch)", "Mô phỏng phỏng vấn để tạo giả thuyết", "Phản biện theo Nielsen và WCAG", "Ghi log, tổng hợp, soạn tài liệu"]),
        ("Nhóm vẫn phải", ["Xác định vấn đề, chọn persona có lý do", "Tự đo lại số liệu AI nêu", "Quyết định Accept, Modify, Reject", "Nói rõ phần nào là dữ liệu mô phỏng"]),
        ("Còn lại", ["Phản biện độc lập bằng AI khác", "Khảo sát thật từ 30 sinh viên", "Usability test 3–5 người", "Chạy Present trên prototype (Page 06)"])]
for i, (head, items) in enumerate(cols):
    x = 0.6 + i * 4.1
    box(s, x, 1.6, 3.95, 3.7)
    text(s, x + 0.25, 1.75, 3.5, 0.4, [(head, 16, True, ORANGE_D if i == 2 else BROWN, HEAD)])
    text(s, x + 0.25, 2.3, 3.5, 2.9, [(t, 13, False, BROWN) for t in items], gap=10)
box(s, 0.6, 5.5, 12.15, 1.3, fill=ORANGE, line=None, radius=0.1)
text(s, 0.6, 5.5, 12.15, 1.3, [("Cảm ơn thầy và các bạn", 26, True, BROWN, HEAD), ("Hỏi đáp · Demo Figma Present", 15, False, BROWN)],
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, gap=2)

assert len(prs.slides) == TOTAL, len(prs.slides)
prs.save(OUT)
print("slides:", len(prs.slides))
