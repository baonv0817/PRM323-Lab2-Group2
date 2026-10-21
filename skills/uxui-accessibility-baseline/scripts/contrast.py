#!/usr/bin/env python3
"""Tính tỉ lệ tương phản WCAG 2.2.

  python contrast.py "#622B14" "#F69D39"
  python contrast.py "#B45309" "#FFF5E5" --large
  python contrast.py --pairs pairs.csv      # cột: fg,bg,nhãn,large(0/1)

Ngưỡng: chữ thường 4.5:1, chữ lớn và UI indicator 3:1.
"""
import csv
import sys


def _hex(c):
    c = c.strip().lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    return tuple(int(c[i:i + 2], 16) / 255 for i in (0, 2, 4))


def _lin(v):
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (_lin(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    a, b = luminance(_hex(fg)), luminance(_hex(bg))
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def verdict(r, large):
    need = 3.0 if large else 4.5
    return ("ĐẠT" if r >= need else "TRƯỢT"), need


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) >= 3 and argv[1] == "--pairs":
        print("nhãn | fg | bg | tỉ lệ | ngưỡng | kết quả")
        for row in csv.reader(open(argv[2], encoding="utf-8")):
            if not row or row[0].startswith("#fg") or row[0] == "fg":
                continue
            fg, bg = row[0], row[1]
            label = row[2] if len(row) > 2 else ""
            large = len(row) > 3 and row[3].strip() == "1"
            r = ratio(fg, bg)
            v, need = verdict(r, large)
            print(f"{label} | {fg} | {bg} | {r:.2f}:1 | {need}:1 | {v}")
        return
    if len(argv) < 3:
        sys.exit(__doc__)
    r = ratio(argv[1], argv[2])
    large = "--large" in argv
    v, need = verdict(r, large)
    print(f"{argv[1]} trên {argv[2]}: {r:.2f}:1 (ngưỡng {need}:1) -> {v}")


if __name__ == "__main__":
    main(sys.argv)
