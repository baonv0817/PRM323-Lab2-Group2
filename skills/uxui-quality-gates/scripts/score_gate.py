#!/usr/bin/env python3
"""Tính kết luận Quality Gate G0–G5 từ file JSON chấm điểm.

Dùng:  python score_gate.py audit.json
Quy tắc: pass=1, partial=0.5, fail=0, na=bỏ khỏi mẫu. Critical chỉ đạt khi pass.
>=80% và không Critical trượt: Đạt · 70-79%: Cần cải thiện · <70%: Cần làm lại · Critical trượt: Chưa qua.
Gate chỉ mở khi gate trước Đạt.
"""
import json
import sys

POINTS = {"pass": 1.0, "partial": 0.5, "fail": 0.0}


def grade(criteria):
    counted = [c for c in criteria if c.get("status") != "na"]
    if not counted:
        return None
    score = sum(POINTS[c["status"]] for c in counted)
    pct = 100 * score / len(counted)
    critical_failed = [c["id"] for c in counted if c.get("critical") and c["status"] != "pass"]
    if critical_failed:
        verdict = "Chưa qua (Critical)" if pct >= 70 else "Cần làm lại"
    elif pct >= 80:
        verdict = "Đạt"
    elif pct >= 70:
        verdict = "Cần cải thiện"
    else:
        verdict = "Cần làm lại"
    return pct, verdict, critical_failed


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    prev_ok = True
    print(f"Hệ thống: {data.get('system', '?')}")
    print("Gate | % | Critical trượt | Kết luận")
    for gate in sorted(data["gates"]):
        g = data["gates"][gate]
        result = grade(g["criteria"])
        if result is None:
            print(f"{gate} | - | - | Không có tiêu chí")
            prev_ok = False
            continue
        pct, verdict, crit = result
        if not prev_ok and verdict == "Đạt":
            verdict = "Đạt điểm nhưng bị chặn: gate trước chưa Approved"
        print(f"{gate} | {pct:.0f}% | {', '.join(crit) or '-'} | {verdict}")
        prev_ok = prev_ok and verdict == "Đạt"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1])
