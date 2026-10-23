"""Sinh slides/BreakBite_Lab2_Presentation.pptx (16 slide) theo phong cách app BreakBite.

Chạy từ gốc repo:  python slides/_build_deck.py      (cần python-pptx và Pillow)
Ảnh lấy từ assets/figma/final-ui-v2/. Màu theo token v2: nền #FAF8F5, cam #F69D39, nâu #622B14, viền #E4DFD8.
Bản 42 slide trước đó nằm ở archive/slides-cu/.
"""
import io
import os
import sys
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "figma", "final-ui-v2")
OUT = os.path.join(ROOT, "slides", "BreakBite_Lab2_Presentation.pptx")
GITHUB = "https://github.com/baonv0817/PRM323-Lab2-Group2"
FIGMA = "https://www.figma.com/design/5vloc9G7UcEI9NYJGpTqN0/PRM323--Copy-?node-id=1-260"

BG, CARD, BORDER = "FAF8F5", "FFFFFF", "E4DFD8"
ORANGE, ORANGE_D, SELECT = "F69D39", "B45309", "FFF1DE"
BROWN, MUTED, GREEN, RED = "622B14", "6B5F55", "15803D", "B91C1C"
HEAD, BODY = "Trebuchet MS", "Calibri"
TOTAL = 16

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


def sheet(s, name, x, y, h):
    path = os.path.join(IMG, name)
    iw, ih = Image.open(path).size
    w = h * iw / ih
    s.shapes.add_picture(path, E(x), E(y), E(w), E(h))
    return w


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


def content_slide(n, title, subtitle, icon_name, evidence):
    s = prs.slides.add_slide(BLANK)
    bg(s)
    icon(s, icon_name, 0.6, 0.42, 0.62)
    text(s, 1.4, 0.36, 11.2, 0.6, [(title, 28, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 1.4, 0.95, 11.2, 0.35, [(subtitle, 14, False, MUTED)])
    box(s, 1.4, 1.32, 0.9, 0.05, fill=ORANGE, line=None, radius=0.5)
    text(s, 0.6, 7.03, 9.5, 0.25, [("Minh chứng: " + evidence, 10, False, MUTED)])
    text(s, 10.6, 7.03, 2.1, 0.25, [(f"BreakBite · {n} / {TOTAL}", 10, False, MUTED)], align=PP_ALIGN.RIGHT)
    return s


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
tb = text(s, 0.8, 6.55, 6.5, 0.3, [("GitHub: github.com/baonv0817/PRM323-Lab2-Group2   ·   Figma: mở file thiết kế", 11, False, ORANGE_D)])
tb.text_frame.paragraphs[0].runs[0].hyperlink.address = GITHUB

# =============================================================== 2 · vấn đề và người dùng
s = content_slide(2, "Vấn đề và người dùng", "Sinh viên chỉ có 15 phút giữa hai slot", "schedule",
                  "ux/p0-problem-framing.md · ux/persona.md")
box(s, 0.6, 1.6, 7.5, 1.9)
text(s, 0.85, 1.75, 7.0, 1.7, [
    ("VẤN ĐỀ", 11, True, MUTED),
    ("Sinh viên có lịch học dày chỉ có khoảng 15 phút giữa hai slot, nhưng hàng chờ căn tin dồn đúng giờ nghỉ, "
     "nên họ bỏ bữa hoặc vào lớp trễ.", 17, False, BROWN),
    ("Làm sao để sinh viên có đồ ăn trong giờ nghỉ ngắn mà không phải xếp hàng?", 14, True, ORANGE_D),
], gap=6)
pains = [("schedule", "Hàng chờ đúng giờ nghỉ", "Bỏ bữa hoặc vào lớp trễ"),
         ("location", "Không biết trước", "Quán mở hay đóng, còn món, bao lâu xong"),
         ("offer", "Phí phát sinh", "Tổng tiền chỉ hiện ở bước cuối"),
         ("error", "Lỗi thanh toán", "Mất giỏ hàng khi mạng yếu")]
for i, (ic, head, sub) in enumerate(pains):
    x, y = 0.6 + (i % 2) * 3.8, 3.7 + (i // 2) * 1.5
    box(s, x, y, 3.7, 1.35)
    icon(s, ic, x + 0.2, y + 0.2, 0.55)
    text(s, x + 0.9, y + 0.2, 2.65, 1.1, [(head, 14, True, BROWN), (sub, 12, False, MUTED)])
box(s, 8.35, 1.6, 4.4, 5.2)
box(s, 8.6, 1.85, 0.8, 0.8, fill=ORANGE, line=None, shape=MSO_SHAPE.OVAL)
text(s, 8.6, 1.85, 0.8, 0.8, [("Q", 28, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
text(s, 9.6, 1.9, 3.0, 0.8, [("Nguyễn Minh Quân", 16, True, BROWN), ("20 tuổi · SV năm 2 · ở ký túc xá", 12, False, MUTED)])
chip(s, 8.6, 2.85, 1.2, "Persona chính", size=11, h=0.3)
text(s, 8.6, 3.35, 3.95, 2.0, [
    ("Học 3 slot mỗi ngày, nghỉ khoảng 15 phút", 13, False, BROWN),
    ("Android tầm trung, cầm máy một tay khi đi bộ", 13, False, BROWN),
    ("Mạng trong tòa nhà chập chờn", 13, False, BROWN),
    ("Mục tiêu: đặt xong dưới 35 giây, tối đa 8 chạm", 13, True, ORANGE_D),
], gap=5)
box(s, 8.6, 5.3, 3.9, 0.95, fill=SELECT, line=None)
text(s, 8.75, 5.38, 3.6, 0.85, [("“Thấy hàng dài là bỏ luôn, nhịn tới trưa.”", 13, True, BROWN),
                                 ("Phỏng vấn mô phỏng AI (SIM-A1)", 10, False, MUTED)])
text(s, 8.6, 6.35, 3.95, 0.4, [("Persona phụ: Trần Mỹ Linh · Cô Hạnh (nhân viên quầy)", 11, False, MUTED)])

# =============================================================== 3 · giải pháp
s = content_slide(3, "Giải pháp: BreakBite", "Đặt từ lớp, trả trước, ra Kiosk quét mã nhận món", "restaurant",
                  "README.md · ux/p0-problem-framing.md")
steps = [("cart", "1 · Đặt từ lớp", "Chọn món, tuỳ chỉnh, hẹn giờ nhận"),
         ("wallet", "2 · Trả trước", "MoMo, VNPAY-QR, thẻ hoặc tiền mặt; lỗi vẫn giữ giỏ hàng"),
         ("qr", "3 · Nhận bằng mã QR", "Ra Kiosk, quét mã, nhận món không xếp hàng")]
for i, (ic, head, sub) in enumerate(steps):
    x = 0.6 + i * 4.2
    box(s, x, 1.65, 3.85, 2.35)
    icon(s, ic, x + 0.3, 1.9, 0.95)
    text(s, x + 0.3, 3.0, 3.3, 0.95, [(head, 17, True, BROWN, HEAD), (sub, 13, False, MUTED)])
    if i < 2:
        text(s, x + 3.85, 2.45, 0.35, 0.5, [("›", 30, True, ORANGE)], align=PP_ALIGN.CENTER)
stats = [("30", "màn app khách", "S01–S30: đặt món, vòng đời đơn, tài khoản"),
         ("15", "màn app người bán", "K01–K15: nhận đơn, làm món, giao món, quản lý quầy"),
         ("3 chạm", "từ Trang chủ tới Theo dõi đơn", "Mục tiêu: dưới 35 giây, tối đa 8 chạm")]
for i, (big, label, sub) in enumerate(stats):
    x = 0.6 + i * 4.2
    box(s, x, 4.3, 3.85, 2.3, fill=SELECT, line=None)
    text(s, x + 0.3, 4.45, 3.3, 0.9, [(big, 40, True, ORANGE_D, HEAD)])
    text(s, x + 0.3, 5.35, 3.3, 1.2, [(label, 15, True, BROWN), (sub, 12, False, MUTED)])

# =============================================================== 4 · nghiên cứu
s = content_slide(4, "Nghiên cứu và quyết định", "Từ insight tới thiết kế, ghi rõ phần nào là dữ liệu thật", "person",
                  "ux/p1-research.md · ux/research.md · ux/survey/")
box(s, 0.6, 1.6, 4.1, 2.25)
text(s, 0.85, 1.75, 3.6, 1.2, [("Khảo sát Google Form", 15, True, BROWN), ("22 câu, RQ1–RQ5, mục tiêu từ 30 sinh viên", 12, False, MUTED)])
chip(s, 0.85, 3.2, 1.9, "Đang thu phản hồi", size=11, h=0.3)
box(s, 0.6, 4.05, 4.1, 2.25)
text(s, 0.85, 4.2, 3.6, 1.8, [("Dữ liệu mô phỏng", 15, True, BROWN),
                               ("5 phỏng vấn AI và 20 phản hồi mô phỏng, dùng để thử form và tạo giả thuyết, không phải bằng chứng", 12, False, MUTED)])
chip(s, 0.85, 5.65, 1.3, "Đã làm", size=11, h=0.3, fill="E8F5EC", color=GREEN, line=GREEN)
box(s, 4.95, 1.6, 7.8, 4.7)
text(s, 5.2, 1.75, 7.3, 0.35, [("INSIGHT → QUYẾT ĐỊNH THIẾT KẾ", 12, True, MUTED)])
rows = [("INS-01", "Hàng chờ giờ nghỉ", "Đặt trước và hẹn giờ nhận (S05)"),
        ("INS-02", "Cần biết trước", "Trạng thái quán và thời gian chờ (S02)"),
        ("INS-04", "Ngại phí ẩn", "Giá cộng dồn trên nút, tổng ở giỏ (S04, S05)"),
        ("INS-05", "Không muốn đăng ký", "Xem menu không cần tài khoản (S26 không bắt buộc)"),
        ("INS-06", "Lỗi thanh toán", "Màn phục hồi giữ giỏ hàng (S06-ERR)")]
for i, (code, need, design) in enumerate(rows):
    y = 2.2 + i * 0.8
    box(s, 5.2, y, 7.3, 0.7, fill=SELECT, line=None)
    text(s, 5.35, y, 0.9, 0.7, [(code, 12, True, ORANGE_D)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 6.3, y, 2.2, 0.7, [(need, 13, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 8.5, y, 3.9, 0.7, [(design, 12, False, MUTED)], anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.6, 6.45, 12.1, 0.4, [("Chưa làm: hỏi nhân viên quầy (RQ6) và usability test với người thật.", 12, True, ORANGE_D)])

# =============================================================== 5 · kiến trúc thông tin
s = content_slide(5, "Kiến trúc thông tin", "Thanh dưới 4 tab cho app khách, 4 tab cho app người bán", "location",
                  "ux/user-flow.md mục 1 · design/screens-s09-s30.md")
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
box(s, 0.6, 6.1, 12.1, 0.7, fill=SELECT, line=None)
text(s, 0.85, 6.1, 11.6, 0.7, [("App người bán (K01–K15): Đơn · Quét mã · Món · Quán, gồm nhận đơn, làm món, giao món, "
                                  "quản lý món và quán, thống kê ca, xử lý sự cố", 13, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)

# =============================================================== 6 · ba flow chính
s = content_slide(6, "Ba flow chính", "Mỗi flow có đầu vào, đầu ra và nhánh lỗi", "cart", "ux/user-flow.md mục 2")
flows = [("F1", "Đặt nhanh, nhận tại quầy",
          ["S02 chọn combo", "S04 topping, giá tự cộng", "S05 giỏ hàng, hẹn giờ", "S06 thanh toán", "S07 mã nhận #A-204"],
          "Có mã nhận đồ; dưới 35 giây, tối đa 8 chạm"),
         ("F2", "Tuỳ chỉnh món và mã giảm giá",
          ["S03 thực đơn", "S04 mức cay, topping", "S05 nhập mã", "Mã sai: báo lỗi, nhập lại", "S06 thanh toán"],
          "Thấy giảm giá và tổng tiền trước khi trả"),
         ("F3", "Lỗi thanh toán và phục hồi",
          ["S06 thanh toán MoMo lỗi", "S06-ERR: giỏ hàng vẫn được giữ", "Thử lại VNPAY-QR hoặc tiền mặt", "S07 / S07-CASH"],
          "Đơn được tạo, không phải đặt lại")]
for i, (code, title, steps_, out) in enumerate(flows):
    x = 0.6 + i * 4.1
    box(s, x, 1.6, 3.95, 4.35)
    chip(s, x + 0.25, 1.8, 0.6, code, size=12)
    text(s, x + 1.0, 1.8, 2.8, 0.45, [(title, 14, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    for k, st in enumerate(steps_):
        y = 2.5 + k * 0.62
        box(s, x + 0.25, y, 3.45, 0.5, fill=SELECT, line=None, radius=0.3)
        text(s, x + 0.4, y, 3.2, 0.5, [(st, 12, k == len(steps_) - 1, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 0.25, 5.45, 3.5, 0.5, [(out, 11, True, ORANGE_D)])
box(s, 0.6, 6.1, 12.1, 0.72, fill=SELECT, line=None)
text(s, 0.85, 6.1, 11.6, 0.72, [("Flow khác: sửa và huỷ đơn, lịch sử, yêu thích, tài khoản, thông báo và nhận món, quán đóng, "
                                  "đánh giá, hẹn giờ, mất mạng · Flow người bán: nhận đơn, làm món, quét mã giao món", 12, False, BROWN)],
     anchor=MSO_ANCHOR.MIDDLE)

# =============================================================== 7 · thiết kế với AI
s = content_slide(7, "Thiết kế với AI, quyết định bởi nhóm", "Mọi đề xuất của AI đều ghi Accept, Modify hoặc Reject", "check",
                  "ai/ai-design-log.md · design/design-decisions.md")
chain = ["Google Stitch tạo UI từ DESIGN.md", "AI phản biện: Nielsen, WCAG, persona", "Nhóm quyết định Accept, Modify, Reject", "Sửa trong Figma, đo lại"]
for i, c in enumerate(chain):
    x = 0.6 + i * 3.07
    box(s, x, 1.65, 2.8, 1.2, fill=CARD)
    text(s, x + 0.2, 1.65, 2.4, 1.2, [(c, 13, True, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    if i < 3:
        text(s, x + 2.8, 1.95, 0.27, 0.5, [("›", 24, True, ORANGE)], align=PP_ALIGN.CENTER)
dec = [("ACCEPT", GREEN, "E8F5EC", "Giá cộng dồn trên nút Thêm vào giỏ (S04)", "Người dùng thấy tổng tiền trước khi chốt"),
       ("MODIFY", ORANGE_D, SELECT, "Chữ nút đổi sang nâu #622B14", "Tương phản 5,23:1; chữ trắng trên cam chỉ 2,14:1"),
       ("REJECT", RED, "FCE8E8", "Bắt buộc đăng nhập để tích điểm", "Xem menu và đặt món không cần tài khoản (D12)")]
for i, (tag, col, fill, head, sub) in enumerate(dec):
    x = 0.6 + i * 4.1
    box(s, x, 3.2, 3.95, 2.75)
    chip(s, x + 0.25, 3.45, 1.1, tag, fill=fill, color=col, line=col, size=12)
    text(s, x + 0.25, 4.0, 3.45, 1.9, [(head, 15, True, BROWN), (sub, 12, False, MUTED)], gap=8)
box(s, 0.6, 6.1, 12.1, 0.7, fill=SELECT, line=None)
text(s, 0.85, 6.1, 11.6, 0.7, [("AI nêu số sai thì nhóm tự đo lại: tương phản chữ trắng trên cam thật là 2,14:1, không phải mức AI nêu.", 13, True, BROWN)],
     anchor=MSO_ANCHOR.MIDDLE)

# =============================================================== 8 · phản biện giao diện
s = content_slide(8, "Phản biện giao diện và bản v2", "Đo bản cũ, sửa, đo lại", "error", "ai/phan-bien-giao-dien/ · tests/audit/")
box(s, 0.6, 1.6, 7.0, 4.95)
table(s, 0.85, 1.85, 6.5, [["Chỉ số", "Bản cũ", "Bản v2"],
                           ["Cam đậm (trung bình S01–S08)", "5,9%", "4,3%"],
                           ["Họ cam–be: nền, thẻ, chip", "55,3%", "4,4%"],
                           ["Emoji trong chữ", "98 / 366", "0"],
                           ["Chữ dưới 14 sp", "86 dòng", "0*"],
                           ["Chữ thiếu tương phản", "8 chỗ", "0"],
                           ["Vùng bấm dưới 48 dp", "20 / 39", "0 / 217"]],
      [3.5, 1.5, 1.5], row_h=0.55, size=14)
text(s, 0.85, 5.9, 6.5, 0.5, [("* trừ nhãn thanh dưới 12 sp. Nền v2 là #FAF8F5 nên không còn tính vào họ cam–be.", 10, False, MUTED)])
box(s, 7.85, 1.6, 4.9, 4.95)
text(s, 8.1, 1.8, 4.4, 4.6, [
    ("LỖI CHÍNH ĐÃ SỬA", 12, True, MUTED),
    ("Quá cam: nền kem trung tính, cam chỉ cho một nút chính", 13, False, BROWN),
    ("Icon lộn xộn: bỏ emoji, dùng một bộ 27 icon vector", 13, False, BROWN),
    ("Giỏ hàng và thanh toán lặp: tách S05 và S06", 13, False, BROWN),
    ("Vùng bấm 48 dp, chữ 14 sp, chữ cam đủ 4,5:1", 13, False, BROWN),
    ("Báo cáo đo do công cụ AI viết nên không độc lập; phản biện của AI khác chưa chạy.", 11, True, ORANGE_D),
], gap=9)

# =============================================================== 9 · Final UI S01–S08
s = content_slide(9, "Final UI: luồng đặt món", "S01–S08 bản v2, một nút cam mỗi màn", "restaurant", "assets/figma/final-ui-v2/ · Figma Page 03")
labels = ["S01 Onboarding", "S02 Trang chủ", "S03 Thực đơn", "S04 Chi tiết món", "S05 Giỏ hàng", "S06 Thanh toán", "S07 Theo dõi", "S08 Đơn hàng"]
for i, (nm, lb) in enumerate(zip(["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08"], labels)):
    x = 0.62 + i * 1.53
    phone(s, nm + ".png", x, 1.65, 3.15)
    text(s, x - 0.05, 4.9, 1.5, 0.5, [(lb, 11, True, BROWN)], align=PP_ALIGN.LEFT)
box(s, 0.6, 5.65, 12.1, 1.1, fill=SELECT, line=None)
text(s, 0.85, 5.7, 11.6, 1.0, [("Trạng thái đi kèm: giỏ trống · mã sai · đang tải · lỗi thanh toán · trả tại quầy · chưa có đơn", 13, True, BROWN),
                                ("Nền kem trung tính, thẻ trắng, một bộ icon vector, vùng bấm từ 48 dp, chữ từ 14 sp", 12, False, MUTED)],
     anchor=MSO_ANCHOR.MIDDLE, gap=6)

# =============================================================== 10 · Final UI S09–S30
s = content_slide(10, "Final UI: vòng đời đơn và tài khoản", "S09–S30 bản v2", "receipt", "design/screens-s09-s30.md · assets/figma/final-ui-v2/")
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

# =============================================================== 11 · app người bán
s = content_slide(11, "App người bán: BreakBite Kiosk", "15 màn K01–K15 cho nhân viên quầy", "cafe", "design/kitchen-app.md · assets/figma/final-ui-v2/kitchen/")
box(s, 0.6, 1.6, 6.9, 3.0)
text(s, 0.85, 1.75, 6.4, 2.8, [
    ("MÀN KHÁCH ĐÃ HỨA, QUẦY PHẢI THỰC HIỆN", 11, True, MUTED),
    ("Đã nhận, Đang làm, Sẵn sàng: nhận đơn, làm món, báo sẵn sàng", 13, False, BROWN),
    ("Mã QR: quét mã, xác nhận giao; trả tại quầy thì thu tiền rồi giao", 13, False, BROWN),
    ("Tạm hết: đánh dấu hết món, thêm và sửa món", 13, False, BROWN),
    ("Quán đóng: bật hoặc tắt nhận đơn", 13, False, BROWN),
    ("Huỷ đơn, sự cố: từ chối đơn, hoàn tiền", 13, False, BROWN),
], gap=7)
box(s, 0.6, 4.8, 6.9, 1.95, fill=SELECT, line=None)
text(s, 0.85, 4.95, 6.4, 1.7, [
    ("Một nút cam mỗi màn; thanh toán luôn hiện trên thẻ đơn để biết đơn nào thu tiền mặt.", 13, True, BROWN),
    ("Bốn tab: Đơn, Quét mã, Món, Quán. Thống kê ca nằm trong tab Quán, xử lý sự cố mở từ tab Đơn.", 12, False, MUTED),
], gap=8)
sheet(s, "contact-sheet-kitchen.png", 7.8, 1.6, 4.9)

# =============================================================== 12 · design system
s = content_slide(12, "Design system", "Token màu, chữ, khoảng cách và component dùng chung cho hai app", "offer", "Figma Page 04, 05 · handoff/flutter-handoff.md mục 5")
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

# =============================================================== 13 · accessibility và responsive
s = content_slide(13, "Accessibility và responsive", "Đo bằng công cụ, không ước lượng bằng mắt", "check", "design/design-decisions.md · tests/audit/ · Figma Page 03")
stats = [("5,23:1", "chữ nút nâu trên cam", "ngưỡng WCAG 4,5:1"), ("48 dp", "vùng bấm nhỏ nhất", "0 / 217 vùng dưới 48 dp"),
         ("14 sp", "chữ nội dung nhỏ nhất", "nhãn thanh dưới 12 sp"), ("0", "emoji trong giao diện", "một bộ 27 icon vector")]
for i, (big, label, sub) in enumerate(stats):
    x = 0.6 + i * 3.07
    box(s, x, 1.6, 2.95, 1.75, fill=SELECT, line=None)
    text(s, x + 0.25, 1.7, 2.5, 0.7, [(big, 28, True, ORANGE_D, HEAD)])
    text(s, x + 0.25, 2.5, 2.5, 0.8, [(label, 13, True, BROWN), (sub, 11, False, MUTED)], gap=1)
box(s, 0.6, 3.6, 7.6, 3.25)
text(s, 0.85, 3.7, 7.0, 0.3, [("360 DP VÀ 412 DP", 11, True, MUTED)])
x = 0.9
for nm, hh in [("S02.png", 2.5), ("412/S02.png", 2.5), ("S05.png", 2.5), ("412/S05.png", 2.5)]:
    w = phone(s, nm, x, 4.1, hh)
    x += w + 0.18
text(s, 0.9, 6.65, 7.0, 0.25, [("S02 và S05: 360 dp, 412 dp", 10, False, MUTED)])
box(s, 8.45, 3.6, 4.3, 3.25)
text(s, 8.7, 3.75, 3.8, 3.0, [
    ("Tương phản đo bằng công thức WCAG, không có chữ nào dưới ngưỡng", 12, False, BROWN),
    ("Trạng thái luôn có chữ hoặc icon đi kèm màu", 12, False, BROWN),
    ("Bản 412 dp dựng bằng constraints, không cuộn ngang", 12, False, BROWN),
    ("Kiểm trên 114 khung bằng Figma Plugin API", 12, True, ORANGE_D),
], gap=9)

# =============================================================== 14 · prototype và kiểm thử
s = content_slide(14, "Prototype và kiểm thử", "Prototype nối cả hai app, có kiểm thử tự động", "qr", "tests/ · docs/test-reports/ · Figma Page 03")
box(s, 0.6, 1.6, 6.0, 4.5)
text(s, 0.85, 1.75, 5.5, 4.2, [
    ("PROTOTYPE FIGMA BẢN V2", 11, True, MUTED),
    ("217 vùng bấm trên 58 khung, 12 điểm bắt đầu", 14, True, BROWN),
    ("Dialog huỷ đơn và từ chối đơn dạng overlay", 13, False, BROWN),
    ("Màn đang tải tự chuyển sau 1,2 giây", 13, False, BROWN),
    ("Back đúng, không màn cụt, không màn mồ côi", 13, False, BROWN),
    ("Đi qua cả luồng khách và luồng người bán", 13, False, BROWN),
], gap=9)
box(s, 6.85, 1.6, 5.9, 4.5)
text(s, 7.1, 1.75, 5.4, 4.2, [
    ("KIỂM THỬ TỰ ĐỘNG · PLAYWRIGHT", 11, True, MUTED),
    ("Prototype bản cũ: 13 / 13 test đạt, bấm theo toạ độ vùng bấm", 13, False, BROWN),
    ("Đồ thị flow bản v2: 7 / 7 test đạt", 13, True, BROWN),
    ("Đặt đơn từ Trang chủ tới Theo dõi đơn: 3 chạm", 13, False, BROWN),
    ("Flow 3 có lối phục hồi về giỏ hàng và đơn tiền mặt", 13, False, BROWN),
], gap=9)
box(s, 0.6, 6.25, 12.15, 0.6, fill=SELECT, line=None)
text(s, 0.85, 6.25, 11.7, 0.6, [("Kiểm thử tự động chỉ chứng minh prototype đi đúng đường đã thiết kế; không thay usability test với người thật.", 12, True, BROWN)],
     anchor=MSO_ANCHOR.MIDDLE)

# =============================================================== 15 · handoff và quality gates
s = content_slide(15, "Bàn giao và Quality Gates", "Handoff cho Flutter; tự chấm theo sáu gate của môn", "wallet", "handoff/flutter-handoff.md · docs/quy-chuan-ux-ui.md · skills/")
box(s, 0.6, 1.6, 5.7, 5.2)
text(s, 0.85, 1.75, 5.2, 0.3, [("HANDOFF FLUTTER (KHÔNG VIẾT CODE)", 11, True, MUTED)])
table(s, 0.85, 2.15, 5.2, [["Figma", "Flutter"], ["color/primary", "ColorScheme.primary"], ["Chip", "ChoiceChip, 48 dp"], ["NavBar", "NavigationBar"],
                           ["Card/Food", "Card + ListTile"], ["IconButton", "IconButton 48 × 48"]], [2.3, 2.9], row_h=0.5, size=13)
text(s, 0.85, 5.3, 5.2, 1.4, [("6 mục cho mỗi màn (layout, component, state, tương tác, điều hướng, ràng buộc) cho S01–S30 và K01–K15.", 12, False, BROWN)])
box(s, 6.55, 1.6, 6.2, 5.2)
text(s, 6.8, 1.75, 5.7, 0.3, [("TỰ CHẤM THEO QUALITY GATES", 11, True, MUTED)])
gates = [("G0", "Problem", "Đạt", GREEN, "E8F5EC"), ("G1", "Research", "Có điều kiện", ORANGE_D, SELECT), ("G2", "UX Design", "5 / 6", ORANGE_D, SELECT),
         ("G3", "UI Concept", "Đạt", GREEN, "E8F5EC"), ("G4", "UI Design", "Có điều kiện", ORANGE_D, SELECT), ("G5", "Validation", "Chưa test người", RED, "FCE8E8")]
for i, (g, name, st, col, fill) in enumerate(gates):
    y = 2.2 + i * 0.62
    text(s, 6.8, y, 0.6, 0.5, [(g, 14, True, BROWN, HEAD)], anchor=MSO_ANCHOR.MIDDLE)
    text(s, 7.45, y, 2.0, 0.5, [(name, 13, False, BROWN)], anchor=MSO_ANCHOR.MIDDLE)
    chip(s, 9.6, y + 0.08, 2.0, st, fill=fill, color=col, line=col, size=11, h=0.34)
text(s, 6.8, 6.0, 5.7, 0.7, [("Gate và ngưỡng 80% là rubric nội bộ của môn, không phải chuẩn quốc tế. Bộ 13 skill trong thư mục skills/ chấm từng gate.", 11, False, MUTED)])

# =============================================================== 16 · tổng kết
s = content_slide(16, "Tổng kết", "Ăn kịp giờ nghỉ, không phải xếp hàng", "restaurant", "README.md · docs/tien-do/TIEN-DO.md")
cols = [("AI giúp", ["Sinh UI ban đầu nhanh (Stitch)", "Mô phỏng phỏng vấn để tạo giả thuyết", "Phản biện theo Nielsen và WCAG", "Ghi log, tổng hợp, soạn tài liệu"]),
        ("Nhóm vẫn phải", ["Xác định vấn đề, chọn persona có lý do", "Tự đo lại số liệu AI nêu", "Quyết định Accept, Modify, Reject", "Nói rõ phần nào là dữ liệu mô phỏng"]),
        ("Còn lại", ["Phản biện độc lập bằng AI khác", "Khảo sát thật từ 30 sinh viên", "Usability test 3–5 người", "Chạy Present trên prototype v2"])]
for i, (head, items) in enumerate(cols):
    x = 0.6 + i * 4.1
    box(s, x, 1.6, 3.95, 3.7)
    text(s, x + 0.25, 1.75, 3.5, 0.4, [(head, 16, True, ORANGE_D if i == 2 else BROWN, HEAD)])
    text(s, x + 0.25, 2.3, 3.5, 2.9, [(t, 13, False, BROWN) for t in items], gap=10)
box(s, 0.6, 5.5, 12.15, 1.3, fill=ORANGE, line=None, radius=0.1)
text(s, 0.6, 5.5, 12.15, 1.3, [("Cảm ơn thầy và các bạn", 26, True, BROWN, HEAD), ("Hỏi đáp · Demo Figma Present", 15, False, BROWN)],
     anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, gap=2)

prs.save(OUT)
print("slides:", len(prs.slides))
