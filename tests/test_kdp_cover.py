"""Unit tests for tools/kdp_cover.py. Run: python3 -m unittest discover tests"""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "tools"))
from kdp_cover import cover_size  # noqa: E402


class TestCover(unittest.TestCase):
    def test_coloring_book_8_5x11_50_pages_white(self):
        r = cover_size(8.5, 11, 50, "white")
        self.assertAlmostEqual(r["spine_in"], 0.1126, places=4)       # 50 × 0.002252
        self.assertAlmostEqual(r["cover_width_in"], 17.3626, places=4)  # 0.125+8.5+0.1126+8.5+0.125
        self.assertAlmostEqual(r["cover_height_in"], 11.25, places=4)
        self.assertFalse(r["spine_text_allowed"])

    def test_cookbook_6x9_120_pages_cream(self):
        r = cover_size(6, 9, 120, "cream")
        self.assertAlmostEqual(r["spine_in"], 0.3, places=4)           # 120 × 0.0025
        self.assertAlmostEqual(r["cover_width_in"], 12.55, places=4)
        self.assertTrue(r["spine_text_allowed"])
        self.assertEqual(r["pixels_at_300dpi"], (3765, 2775))

    def test_spine_text_boundary_80_pages(self):
        self.assertFalse(cover_size(6, 9, 78, "white")["spine_text_allowed"])
        self.assertTrue(cover_size(6, 9, 80, "white")["spine_text_allowed"])

    def test_rejects_too_few_pages(self):
        with self.assertRaises(ValueError):
            cover_size(8.5, 11, 22, "white")

    def test_rejects_too_many_cream_pages(self):
        with self.assertRaises(ValueError):
            cover_size(6, 9, 778, "cream")

    def test_rejects_odd_page_count(self):
        with self.assertRaises(ValueError):
            cover_size(6, 9, 101, "white")

    def test_rejects_unknown_paper(self):
        with self.assertRaises(ValueError):
            cover_size(6, 9, 100, "glossy")


if __name__ == "__main__":
    unittest.main()
