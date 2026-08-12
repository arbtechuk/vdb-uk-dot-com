#!/usr/bin/env python3
"""Regression check for the homepage's curated case-study selection."""

from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE = ROOT / "src" / "index.html"

EXPECTED = [
    ("/case-studies/orbio-earth.html", "Orbio.earth"),
    ("/case-studies/treeconomy.html", "Treeconomy"),
    ("/case-studies/npk-recovery-braingraph.html", "NPK Recovery / Braingraph"),
    ("/case-studies/lga-funding-analysis.html", "Local Government Association"),
]


class SelectedCaseStudiesParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_grid = False
        self.grid_depth = 0
        self.current_href: str | None = None
        self.current_text: list[str] = []
        self.cards: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        if tag == "div" and "projects__grid" in classes:
            self.in_grid = True
            self.grid_depth = 1
            return
        if not self.in_grid:
            return
        if tag == "div":
            self.grid_depth += 1
        if tag == "a" and "project-card" in classes:
            self.current_href = values.get("href") or ""
            self.current_text = []

    def handle_data(self, data: str) -> None:
        if self.current_href is not None:
            self.current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if not self.in_grid:
            return
        if tag == "a" and self.current_href is not None:
            text = " ".join(" ".join(self.current_text).split())
            self.cards.append((self.current_href, text))
            self.current_href = None
            self.current_text = []
        if tag == "div":
            self.grid_depth -= 1
            if self.grid_depth == 0:
                self.in_grid = False


def main() -> None:
    parser = SelectedCaseStudiesParser()
    parser.feed(HOMEPAGE.read_text(encoding="utf-8"))

    actual_hrefs = [href for href, _ in parser.cards]
    expected_hrefs = [href for href, _ in EXPECTED]
    assert actual_hrefs == expected_hrefs, (
        "Homepage selected case studies must be exactly the four newly approved records "
        f"in the requested order. Expected {expected_hrefs}, got {actual_hrefs}."
    )

    for (href, expected_name), (_, card_text) in zip(EXPECTED, parser.cards, strict=True):
        assert expected_name in card_text, f"{href} must visibly identify {expected_name!r}."
        target = ROOT / "src" / href.lstrip("/")
        assert target.is_file(), f"Homepage card target does not exist: {target}"

    print("homepage selected case studies: ok")


if __name__ == "__main__":
    main()
