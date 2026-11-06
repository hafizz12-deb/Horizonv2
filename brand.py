#!/usr/bin/env python3
"""Apply Horizon Custom's dark-teal / mint identity to a pinned Horizon Android checkout."""
from pathlib import Path
import argparse

REPLACEMENTS = {
    "crates/horizon-theme/src/night.rs": [
        ("sky: [0x07061a, 0x140f38, 0x2a1656, 0x5b2a78, 0xb0477d, 0xf08a5d],",
         "sky: [0x07131d, 0x0b2631, 0x10434b, 0x17615e, 0x238575, 0x66c7a6],"),
        ("page: 0x0e0b26,", "page: 0x07141c,"),
        ("side: 0x0a0820,", "side: 0x050f16,"),
        ("card: 0x15112e,", "card: 0x0d202a,"),
        ("card_hi: 0x231c4a,", "card_hi: 0x153542,"),
        ("stroke: 0xb9acff,", "stroke: 0x8bdcc8,"),
        ("muted: 0xa59fc6,", "muted: 0xb6b0d4,"),
        ("accent: 0x7656fa,", "accent: 0x187f69,"),
        ("accent_hi: 0xa08cff,", "accent_hi: 0x55d6b0,"),
        ("on_accent: 0xffffff,", "on_accent: 0xffffff,"),
        ("sky: [0xc9d3f2, 0xdcd8f3, 0xead5ec, 0xf5d3d8, 0xf9d6bd, 0xfbe4c6],",
         "sky: [0xd6f2eb, 0xc4e8e0, 0xa8ddd0, 0x89cdbb, 0x6eb5a2, 0x4d958c],"),
        ("page: 0xe9e6f6,", "page: 0xe6f5f0,"),
        ("side: 0xe1ddf1,", "side: 0xd9eee7,"),
        ("card: 0xfdfcff,", "card: 0xf7fffc,"),
        ("stroke: 0x3b2f78,", "stroke: 0x286c5e,"),
        ("accent: 0x5b3fd6,", "accent: 0x176b59,"),
        ("accent_hi: 0x5333c9,", "accent_hi: 0x145b4c,"),
    ],
    "packaging/android/AndroidManifest.xml": [
        ('android:label="Horizon Android"', 'android:label="Horizon Custom"'),
    ],
    "packaging/android/res/values/styles.xml": [
        ("#9a86ff", "#55d6b0"),
    ],
}

def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(
            f"Brand patch stopped safely: {path}: expected exactly one match, found {count}"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    args = parser.parse_args()
    root = args.source.resolve()
    for relative, pairs in REPLACEMENTS.items():
        path = root / relative
        if not path.is_file():
            raise SystemExit(f"Expected upstream file is missing: {relative}")
        for old, new in pairs:
            replace_once(path, old, new)
    print("Horizon Custom branding applied.")

if __name__ == "__main__":
    main()
