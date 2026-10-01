"""KDP paperback cover size calculator for Chef Anto / Chef Dogs AI books.

Usage:
  python3 tools/kdp_cover.py --trim 8.5x11 --pages 50 --paper white
  python3 tools/kdp_cover.py --trim 6x9 --pages 120 --paper cream

Spine multipliers and page limits come from the KDP spec summary at
https://www.kdpeasy.com/blog/spine-width-calculator-guide (checked 2026-10-01).
Always confirm the final numbers with Amazon's own KDP cover calculator before upload.
"""
import argparse

SPINE_PER_PAGE = {  # inches per page
    "white": 0.002252,
    "cream": 0.0025,
    "standard-color": 0.002252,
    "premium-color": 0.002347,
}
MAX_PAGES = {"white": 800, "cream": 776}
MIN_PAGES = 24
MIN_PAGES_SPINE_TEXT = 80
BLEED = 0.125  # inches on every outside edge


def cover_size(trim_w, trim_h, pages, paper):
    if paper not in SPINE_PER_PAGE:
        raise ValueError(f"paper must be one of {sorted(SPINE_PER_PAGE)}")
    if pages < MIN_PAGES:
        raise ValueError(f"KDP paperbacks need at least {MIN_PAGES} pages")
    if pages > MAX_PAGES.get(paper, 10**6):
        raise ValueError(f"{paper} paper allows at most {MAX_PAGES[paper]} pages")
    if pages % 2:
        raise ValueError("page count must be even (pages are printed on both sides)")
    spine = pages * SPINE_PER_PAGE[paper]
    width = BLEED + trim_w + spine + trim_w + BLEED
    height = BLEED + trim_h + BLEED
    return {
        "spine_in": round(spine, 4),
        "cover_width_in": round(width, 4),
        "cover_height_in": round(height, 4),
        "spine_text_allowed": pages >= MIN_PAGES_SPINE_TEXT,
        "pixels_at_300dpi": (round(width * 300), round(height * 300)),
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--trim", required=True, help="e.g. 8.5x11 or 6x9 (inches)")
    ap.add_argument("--pages", type=int, required=True)
    ap.add_argument("--paper", default="white", choices=sorted(SPINE_PER_PAGE))
    a = ap.parse_args()
    w, h = (float(x) for x in a.trim.lower().split("x"))
    r = cover_size(w, h, a.pages, a.paper)
    print(f"Trim {w} x {h} in · {a.pages} pages · {a.paper} paper")
    print(f"Spine width:  {r['spine_in']} in")
    print(f"Full cover:   {r['cover_width_in']} x {r['cover_height_in']} in (with {BLEED} in bleed)")
    print(f"At 300 DPI:   {r['pixels_at_300dpi'][0]} x {r['pixels_at_300dpi'][1]} px")
    print(f"Spine text:   {'allowed' if r['spine_text_allowed'] else 'NOT allowed (under 80 pages, keep spine blank)'}")
