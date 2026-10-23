"""Cập nhật slides/BreakBite_Lab2_Presentation.pptx theo bản 30 màn khách và app người bán (K01–K15).

Chạy từ thư mục gốc repo:  python slides/_build_deck.py
Cần python-pptx. Đọc ảnh từ assets/figma/final-ui-v2/. Mỗi lần chạy sinh lại bản đã cập nhật từ chính file hiện tại,
nên chỉ chạy một lần; muốn chạy lại thì khôi phục file pptx từ git trước.
"""
import copy
import os
import sys
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PPTX = os.path.join(ROOT, "slides", "BreakBite_Lab2_Presentation.pptx")
IMG = os.path.join(ROOT, "assets", "figma", "final-ui-v2")
GITHUB = "https://github.com/baonv0817/PRM323-Lab2-Group2"
FIGMA = "https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260"

BROWN, ORANGE, SOFT, WHITE, BORDER = "622B14", "F69D39", "8A5D48", "FFFFFF", "E8D9C6"
prs = Presentation(PPTX)
S = list(prs.slides)  # chỉ số gốc, S[0] = slide 1


def shape(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    raise KeyError(name)


def set_par(par, text, size=None):
    runs = par.runs
    runs[0].text = text
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    if size:
        runs[0].font.size = Pt(size)


def set_pars(sh, texts):
    pars = sh.text_frame.paragraphs
    while len(pars) < len(texts):
        new = copy.deepcopy(pars[-1]._p)
        pars[-1]._p.addnext(new)
        pars = sh.text_frame.paragraphs
    for p in pars[len(texts):]:
        p._p.getparent().remove(p._p)
    for p, t in zip(sh.text_frame.paragraphs, texts):
        set_par(p, t)


def set_text(slide, name, text):
    set_pars(shape(slide, name), [text])


def replace_image(slide, name, filename):
    pic = shape(slide, name)
    rid = pic._element.blipFill.blip.rEmbed
    part = slide.part.related_part(rid)
    part._blob = open(os.path.join(IMG, filename), "rb").read()


# ---------------------------------------------------------------- slide 1 (bìa)
t6 = shape(S[0], "Text 6")
pars = t6.text_frame.paragraphs
set_par(pars[0], "Nhóm 2 · SE1919 — Nguyễn Viết Bảo (SE183398) · Đỗ Hoàng Gia Bảo (SE193119) · "
                 "Nguyễn Quốc Hoàng Pháp (SE190175) · Nguyễn Hoàng An (SE193905) · Nguyễn Thành Danh (SE193274)", 12)
pars[1].runs[1].text = "github.com/baonv0817/PRM323-Lab2-Group2"
pars[1].runs[1].hyperlink.address = GITHUB
pars[2].runs[1].hyperlink.address = FIGMA

# ---------------------------------------------------------------- slide 3 (tổng quan)
replace_image(S[0], "Image 0", "cover.png")
set_text(S[2], "Text 2", "BREAKBITE — APP ĐẶT TRƯỚC, NHẬN TẠI QUẦY TRONG TRƯỜNG")
set_pars(shape(S[2], "Text 13"), [
    "30 màn app khách + 15 màn app người bán · 360 × 800 dp, có bản 412 dp",
    "Design system: Variables + component set có variant · prototype Figma nối cả hai app",
    "Handoff Flutter (không viết code)",
])
set_text(S[2], "Text 12", "Phạm vi")

# ---------------------------------------------------------------- slide 14 (IA)
set_text(S[13], "Text 2", "CẤU TRÚC ĐIỀU HƯỚNG — 30 MÀN KHÁCH + 15 MÀN NGƯỜI BÁN")
set_text(S[13], "Text 32", "Các màn còn lại (S09–S30) và app người bán")
set_pars(shape(S[13], "Text 33"), [
    "S09–S14 · sửa/huỷ đơn, lịch sử, yêu thích, đặt lại",
    "S15–S20 · tài khoản, thông báo, nhận món (QR)",
    "S21–S25 · quán đóng, món hết, đánh giá, sự cố, hẹn giờ",
    "S26–S30 · đăng nhập, chọn kiosk, tìm kiếm, mã giảm giá, mất mạng",
    "K01–K15 · app người bán (quầy)",
])

# ---------------------------------------------------------------- slides 26-28 (Final UI)
set_text(S[25], "Text 2", "BỐ CỤC & PHÂN CẤP — 4/8 MÀN ĐẶT MÓN (BẢN V2)")
for nm, f in [("Image 1", "S02.png"), ("Image 3", "S04.png"), ("Image 4", "S05.png"), ("Image 5", "S06.png")]:
    replace_image(S[25], nm, f)
set_text(S[26], "Text 2", "NHẤT QUÁN CÁC MÀN ĐẶT MÓN CÒN LẠI (BẢN V2)")
for nm, f in [("Image 1", "S01.png"), ("Image 2", "S03.png"), ("Image 3", "S07.png"), ("Image 4", "S08.png")]:
    replace_image(S[26], nm, f)
for nm, f in [("Image 0", "S05-EMPTY.png"), ("Image 1", "S06-LOADING.png"), ("Image 2", "S06-ERR.png"), ("Image 3", "S07.png")]:
    replace_image(S[27], nm, f)

# ---------------------------------------------------------------- slide 32 (responsive 412 dp)
s32 = S[31]
set_text(s32, "Text 2", "360 DP VÀ 412 DP ĐỀU ĐÃ DỰNG (RÀNG BUỘC CONSTRAINTS)")
set_text(s32, "Text 12", "S06 Thanh toán")
set_text(s32, "Text 3", "Minh chứng: Figma Page 03 (khung ' v2 · 412') · assets/figma/final-ui-v2/412/")
for nm, f in [("Image 0", "S02.png"), ("Image 1", "S06.png"), ("Image 2", "S05.png")]:
    replace_image(s32, nm, f)
for card, (ph_shape, ph_text, f) in {
    "a": ("Shape 8", "Text 9", "412/S02.png"),
    "b": ("Shape 14", "Text 15", "412/S06.png"),
    "c": ("Shape 20", "Text 21", "412/S05.png"),
}.items():
    box, label = shape(s32, ph_shape), shape(s32, ph_text)
    left, top, width, height = box.left, box.top, box.width, box.height
    box._element.getparent().remove(box._element)
    label._element.getparent().remove(label._element)
    pic_h = int(width * 800 / 412)
    s32.shapes.add_picture(os.path.join(IMG, f), left, top + (height - pic_h) // 2, width, pic_h)
for nm in ("Text 10", "Text 16", "Text 22"):
    sh = shape(s32, nm)
    sh.text_frame.paragraphs[0].runs[0].text = "360 dp"
# nhãn 412 dp dưới ảnh
for x in (2423160, 6172200, 9921240):
    tb = s32.shapes.add_textbox(Emu(x), Emu(5486400), Emu(1554480), Emu(274320))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    r = tf.paragraphs[0].add_run()
    r.text = "412 dp"
    r.font.size = Pt(12)
    r.font.name = "Cambria"
    r.font.color.rgb = RGBColor.from_string(SOFT)
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER

# ---------------------------------------------------------------- slide 33-34 (prototype)
set_text(S[32], "Text 2", "FIGMA PAGE 03 (V2) · 12 ĐIỂM BẮT ĐẦU, HÀNH ĐỘNG, KẾT QUẢ")
set_text(S[32], "Text 3", "Minh chứng: Figma Page 03 (bản v2) · Page 06 (bản cũ) · tests/figma-proto/hotspots-v2.json")
set_text(S[32], "Text 23", "S06-ERR → Thử lại / Tiền mặt → S07-CASH")
set_text(S[33], "Text 3", "Minh chứng: Figma Page 03 (v2) · Page 06")

# ---------------------------------------------------------------- slide 35-36 (handoff)
for ti, rows in ((0, [("color/v2-background #FAF8F5", "ColorScheme.surface"), ("color/v2-selected #FFF1DE", "ColorScheme.secondaryContainer")]),
                 (1, [("Chip", "ChoiceChip (48 dp)"), ("IconButton", "IconButton, minimumSize 48 × 48")])):
    tbl = [sh for sh in S[34].shapes if sh.has_table][ti].table
    for a, b in rows:
        new = copy.deepcopy(tbl._tbl.tr_lst[-1])
        tbl._tbl.tr_lst[-1].addnext(new)
        row = tbl.rows[len(tbl.rows) - 1]
        for cell, text in zip(row.cells, (a, b)):
            para = cell.text_frame.paragraphs[0]
            set_par(para, text)
for sl in (S[25], S[26]):
    for sh in sl.shapes:
        if sh.has_text_frame and sh.text_frame.text.startswith("Chưa có"):
            set_pars(sh, ["Xem Figma", "Page 02"])
for sh in S[34].shapes:
    if sh.has_table:
        for row in sh.table.rows:
            row.height = Emu(400000)
set_text(S[35], "Text 2", "S01–S30 + K01–K15 × 6 MỤC · PHẠM VI THIẾT KẾ, KHÔNG VIẾT CODE")
set_pars(shape(S[35], "Text 33"), ["Token + 2 bảng mapping (kèm token v2)", "6 mục cho S01–S30 và K01–K15", "Hành vi màn ≥ 600 dp: NavigationRail, lưới 2–3 cột"])
set_pars(shape(S[35], "Text 36"), [
    "Chưa có phản hồi khảo sát thật — persona là proto-persona",
    "Chưa usability test Flow 1 (< 35 giây) và chưa có phản biện của AI khác cho bản v2",
    "Chạy Present trên prototype v2 và cập nhật ảnh chuẩn Playwright",
])
set_text(S[35], "Text 3", "Minh chứng: handoff/flutter-handoff.md mục 2–6")


# ---------------------------------------------------------------- slide mới
def new_slide(number, title, subtitle, evidence):
    src = S[25]
    s = prs.slides.add_slide(src.slide_layout)
    for ph in list(s.placeholders):
        ph._element.getparent().remove(ph._element)
    bg = src._element.cSld.find(qn("p:bg"))
    if bg is not None:
        s._element.cSld.insert(0, copy.deepcopy(bg))
    for nm in ("Text 0", "Text 1", "Text 2", "Text 3", "Text 4"):
        s.shapes._spTree.append(copy.deepcopy(shape(src, nm)._element))
    set_text(s, "Text 0", number)
    set_text(s, "Text 1", title)
    set_text(s, "Text 2", subtitle)
    set_text(s, "Text 3", evidence)
    return s


def add_card(s, x, y, w, h):
    from pptx.enum.shapes import MSO_SHAPE
    card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Emu(x), Emu(y), Emu(w), Emu(h))
    card.adjustments[0] = 0.04
    card.fill.solid()
    card.fill.fore_color.rgb = RGBColor.from_string(WHITE)
    card.line.color.rgb = RGBColor.from_string(BORDER)
    card.line.width = Emu(9525)
    card.shadow.inherit = False
    return card


def add_text(s, x, y, w, h, items, anchor=MSO_ANCHOR.TOP, align=PP_ALIGN.LEFT):
    """items: danh sách (text, size, bold, color)."""
    tb = s.shapes.add_textbox(Emu(x), Emu(y), Emu(w), Emu(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    for i, (text, size, bold, color) in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.name = "Cambria"
        r.font.color.rgb = RGBColor.from_string(color)
    return tb


def add_table(s, x, y, w, rows, col_widths, row_h=420000, size=13):
    tbl_shape = s.shapes.add_table(len(rows), len(rows[0]), Emu(x), Emu(y), Emu(w), Emu(row_h * len(rows)))
    tbl = tbl_shape.table
    for j, cw in enumerate(col_widths):
        tbl.columns[j].width = Emu(cw)
    for i, row in enumerate(rows):
        tbl.rows[i].height = Emu(row_h)
        for j, text in enumerate(row):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor.from_string(BROWN if i == 0 else (WHITE if i % 2 else "FFF5E5"))
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            para = cell.text_frame.paragraphs[0]
            run = para.add_run()
            run.text = text
            run.font.size = Pt(size)
            run.font.bold = i == 0 or j == 0
            run.font.name = "Cambria"
            run.font.color.rgb = RGBColor.from_string(WHITE if i == 0 else BROWN)
    return tbl


def img(s, filename, x, y, w):
    path = os.path.join(IMG, filename)
    from PIL import Image
    iw, ih = Image.open(path).size
    return s.shapes.add_picture(path, Emu(x), Emu(y), Emu(w), Emu(int(w * ih / iw)))


# N3 · phản biện giao diện v2
n3 = new_slide("7.", "Design Decisions — Phản biện giao diện", "A01–A15 → FINAL UI V2 · SỐ ĐO TRƯỚC VÀ SAU",
               "Minh chứng: ai/phan-bien-giao-dien/ · tests/audit/ (Playwright + Figma Plugin API)")
add_card(n3, 548640, 1417320, 6583680, 4800600)
add_text(n3, 777240, 1554480, 6126480, 320040, [("SỐ ĐO BẢN CŨ → V2", 14, True, SOFT)])
add_table(n3, 777240, 1965960, 6126480, [
    ["Chỉ số", "Bản cũ", "V2"],
    ["Cam đậm (TB S01–S08)", "5,9%", "4,3%"],
    ["Họ cam–be: nền, thẻ, chip", "55,3%", "4,4%"],
    ["Emoji trong chữ", "98/366", "0"],
    ["Chữ dưới 14 sp", "86 dòng", "0*"],
    ["Chữ thiếu tương phản", "8 chỗ", "0"],
    ["Vùng bấm dưới 48 dp", "20/39", "0/217"],
], [3200000, 1463040, 1463440], row_h=480000)
add_text(n3, 777240, 5440680, 6126480, 640080, [
    ("* trừ nhãn thanh dưới 12 sp (ngoại lệ D36). Nền v2 là #FAF8F5 nên không còn tính vào họ cam–be.", 11, False, SOFT)])
add_card(n3, 7360920, 1417320, 4297680, 4800600)
add_text(n3, 7589520, 1554480, 3931920, 4572000, [
    ("LỖI CHÍNH ĐÃ SỬA", 14, True, SOFT),
    ("A01 · Giao diện quá cam: nền kem trung tính, cam chỉ cho một nút chính", 12, False, BROWN),
    ("A02 · Icon lộn xộn: bỏ emoji, một bộ 27 icon vector", 12, False, BROWN),
    ("A03 · Giỏ hàng và thanh toán lặp: tách S05 và S06", 12, False, BROWN),
    ("A04–A06 · Vùng bấm 48 dp, chữ 14 sp, chữ cam đủ 4,5:1", 12, False, BROWN),
    ("A07–A15 · CTA S07, chip, QR, tên trạng thái, ảnh món, nội dung không có nguồn", 12, False, BROWN),
    ("Chưa có phản biện độc lập của AI khác cho v2; báo cáo đo do Claude viết nên không độc lập.", 11, False, SOFT),
])

# N1 · 30 màn khách
n1 = new_slide("8.", "Final UI v2 — 30 màn app khách", "S01–S08 · S09–S25 · S26–S30 (BẢN SAU PHẢN BIỆN)",
               "Minh chứng: assets/figma/final-ui-v2/ · design/screens-s09-s30.md")
cols = [("contact-sheet-s01-s08.png", "S01–S08 · Đặt món",
         "Onboarding, trang chủ, thực đơn, chi tiết món, giỏ hàng, thanh toán, theo dõi đơn, đơn hàng"),
        ("contact-sheet-s09-s25.png", "S09–S25 · Vòng đời đơn",
         "Sửa/huỷ đơn, lịch sử, yêu thích, tài khoản, thông báo, nhận món QR, quán đóng, món hết, đánh giá, sự cố, hẹn giờ"),
        ("contact-sheet-s26-s30.png", "S26–S30 · Bổ sung",
         "Đăng nhập email trường, chọn kiosk, tìm kiếm, mã giảm giá, mất kết nối, đang tải")]
for k, (fname, head, desc) in enumerate(cols):
    x = 548640 + k * 3703320
    img(n1, fname, x, 1417320, 3500000)
    add_text(n1, x, 5250000, 3500000, 280000, [(head, 14, True, BROWN)])
    add_text(n1, x, 5560000, 3500000, 800000, [(desc, 11, False, SOFT)])

# N2 · app người bán
n2 = new_slide("8.", "App người bán — BreakBite Kiosk",
               "15 MÀN K01–K15 CHO NHÂN VIÊN QUẦY", "Minh chứng: design/kitchen-app.md · assets/figma/final-ui-v2/kitchen/")
add_card(n2, 548640, 1417320, 6400800, 2606040)
add_text(n2, 731520, 1508760, 6035040, 2423160, [
    ("MÀN KHÁCH ĐÃ HỨA, QUẦY PHẢI THỰC HIỆN", 13, True, SOFT),
    ("S07 Đã nhận → Đang làm → Sẵn sàng  ←  K03 Nhận đơn, K04 Báo sẵn sàng", 12, False, BROWN),
    ("S20 mã QR  ←  K05 Quét mã, K06 Xác nhận giao (K06-CASH thu tiền mặt)", 12, False, BROWN),
    ("S03/S22 Tạm hết  ←  K08, K09 Hết món; K14, K15 Thêm, sửa món", 12, False, BROWN),
    ("S21 Quán đóng  ←  K10 Bật/tắt nhận đơn", 12, False, BROWN),
    ("S07-DIALOG huỷ, S24 sự cố  ←  K12 Từ chối, K13 Hoàn tiền", 12, False, BROWN),
])
add_card(n2, 548640, 4160520, 6400800, 2057400)
add_text(n2, 731520, 4251960, 6035040, 1920240, [
    ("MÀN VÀ FLOW", 13, True, SOFT),
    ("K01 Đăng nhập · K02 Danh sách đơn · K03 Chi tiết · K04 Đang chuẩn bị · K05 Quét mã · K06 Giao món", 12, False, BROWN),
    ("K08 Quản lý món · K09 Hết món · K10 Quán · K11 Thống kê ca · K12 Từ chối · K13 Sự cố · K14 Thêm món · K15 Sửa món", 12, False, BROWN),
    ("Một nút cam mỗi màn; thanh toán luôn hiện trên thẻ đơn để biết đơn nào thu tiền mặt.", 12, False, BROWN),
])
img(n2, "contact-sheet-kitchen.png", 7132320, 1417320, 4526280)

# N4 · Quality Gates
n4 = new_slide("12.", "Chấm UX/UI theo Quality Gates", "G0–G5 · RUBRIC NỘI BỘ CỦA MÔN, KHÔNG PHẢI CHUẨN QUỐC TẾ",
               "Minh chứng: docs/quy-chuan-ux-ui.md · skills/ (13 skill) · prm393-material.web.app/quality-gates")
add_card(n4, 548640, 1417320, 6858000, 4800600)
add_text(n4, 777240, 1508760, 6400800, 320040, [("SÁU GATE VÀ TIÊU CHÍ CRITICAL CHÍNH", 13, True, SOFT)])
add_table(n4, 777240, 1920240, 6400800, [
    ["Gate", "Phase", "Critical chính"],
    ["G0", "Ideas", "Problem statement đủ 4 phần; giả định có nhãn"],
    ["G1", "Research", "Dữ liệu người dùng thật; insight truy được về nguồn"],
    ["G2", "UX Design", "Flow đủ đầu, cuối, lỗi; IA và wireframe"],
    ["G3", "UI Concept", "≥ 2 hướng; style guide; contrast, 48 dp, 14 sp"],
    ["G4", "UI Design", "Prototype đi hết tác vụ; đủ state; dùng style guide"],
    ["G5", "Validation", "Usability test; không blocker; bàn giao đủ"],
], [640080, 1280160, 4480560], row_h=560000, size=12)
add_card(n4, 7589520, 1417320, 4069080, 4800600)
add_text(n4, 7818120, 1508760, 3611880, 4572000, [
    ("THANG ĐIỂM", 13, True, SOFT),
    ("≥ 80% và mọi Critical đạt: Đạt", 12, False, BROWN),
    ("70–79%: Cần cải thiện · < 70%: Cần làm lại", 12, False, BROWN),
    ("Critical trượt: Chưa qua, dù tổng điểm cao", 12, False, BROWN),
    ("NGUỒN", 13, True, SOFT),
    ("Contrast, vùng chạm: WCAG 2.2, Material (chuẩn và hướng dẫn ngành)", 12, False, BROWN),
    ("Heuristic: Nielsen, quy tắc kinh nghiệm", 12, False, BROWN),
    ("Gate, ngưỡng 80%: rubric nội bộ của môn", 12, False, BROWN),
    ("Bộ 13 skill trong repo (thư mục skills/) chấm từng gate, UI Simplicity 20 tiêu chí, contrast, ma trận state.", 11, False, SOFT),
])

shape(n4, "Text 1").left = Emu(1417320)

# ---------------------------------------------------------------- sắp xếp lại và đánh lại số trang
lst = prs.slides._sldIdLst
ids = list(lst)
orig, extra = ids[:len(S)], ids[len(S):]  # extra = n3, n1, n2, n4 theo thứ tự tạo
n3_id, n1_id, n2_id, n4_id = extra
order = orig[:25] + [n3_id] + orig[25:27] + [n1_id, n2_id] + orig[27:36] + [n4_id] + orig[36:]
for e in ids:
    lst.remove(e)
for e in order:
    lst.append(e)
for i, slide in enumerate(prs.slides, start=1):
    for sh in slide.shapes:
        if sh.has_text_frame and sh.left == 11247120 and sh.top == 6419088:
            set_par(sh.text_frame.paragraphs[0], str(i))
prs.save(PPTX)
print("slides:", len(prs.slides))
