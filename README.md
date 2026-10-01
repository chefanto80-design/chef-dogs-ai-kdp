# Chef Dogs AI · KDP Books 🐾📚

**Chef Anto's Amazon KDP publishing project: a bilingual children's coloring book starring her dogs as chef characters, plus two cookbooks, and a tested cover-size calculator to get the print files right.**
Built by Chef Anto (Antoanela Alexander), Miami. Brand site: [pets.chefanto.com](https://pets.chefanto.com)

## The books
| Title | What it is | Status |
|---|---|---|
| Chef Dogs AI coloring book | Bilingual English–Romanian coloring book with Gia, Luna and Piko | Artwork exists; interior and cover not in this repo yet |
| "7 Days, 7 Meals, With What We Have" | Human cookbook: a week of zero-waste meals | Planned |
| Dog cookbook | Recipes for dogs, with a vet-safety page and a Pawsome Chef QR code | Planned |

**Characters:** Gia and Luna (the Chef Dogs AI universe, started February 2025), plus Piko.

**Money ladder:** free lead magnet → KDP books → app subscriptions → pop-up dinners → Dream House membership.

## The tool: KDP cover calculator
KDP rejects covers that are even a little the wrong size. [`tools/kdp_cover.py`](tools/kdp_cover.py) works out the spine width and full wrap-around cover size from trim size, page count and paper type.

```bash
python3 tools/kdp_cover.py --trim 8.5x11 --pages 50 --paper white
```
Real output:
```
Trim 8.5 x 11.0 in · 50 pages · white paper
Spine width:  0.1126 in
Full cover:   17.3626 x 11.25 in (with 0.125 in bleed)
At 300 DPI:   5209 x 3375 px
Spine text:   NOT allowed (under 80 pages, keep spine blank)
```

Rules built in (from a KDP spec summary, checked 2026-10-01, [source](https://www.kdpeasy.com/blog/spine-width-calculator-guide)):
- Spine per page: white 0.002252", cream 0.0025", standard color 0.002252", premium color 0.002347"
- Bleed 0.125" on every outside edge
- 24-page minimum; max 800 (white) / 776 (cream)
- Spine text only at 80+ pages
- Even page count (KDP pads odd files with a blank page; the tool asks you to decide)

**Always confirm the final size with Amazon's own KDP cover calculator before uploading.**

## Files
| Path | What it is |
|---|---|
| [`tools/kdp_cover.py`](tools/kdp_cover.py) | Cover and spine calculator |
| [`tests/test_kdp_cover.py`](tests/test_kdp_cover.py) | 7 unit tests |

## Test results (only tests actually run, 2026-10-01)
| # | Test | Result |
|---|---|---|
| 1 | `python3 -m unittest discover tests` | ✅ **7/7 passed** |
| 2 | Coloring-book example run (8.5×11, 50 pages, white) | ✅ Output above, matches the hand math: 50 × 0.002252 = 0.1126"; 0.125 + 8.5 + 0.1126 + 8.5 + 0.125 = 17.3626" |

The unit tests cover: an 8.5×11 coloring book, a 6×9 cookbook on cream paper (0.3" spine, 12.55" × 9.25", 3765 × 2775 px), the 80-page spine-text boundary, and rejecting too few pages, too many cream pages, odd page counts and unknown paper.

**Not tested yet:** no file has been uploaded to KDP. The calculator has not been compared with Amazon's official calculator. The book manuscripts and artwork are not in this repo; add them to `books/` when ready.

---
Chef Anto 🌿🤓❤️
