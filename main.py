"""One-line cat joke entry for make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes a single joke about cats, one line, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt for local testing).
Standard library only, deterministic, no network.
"""

import os

JOKE = (
    "My cat ignores me all day, then at 3 a.m. sits on my chest "
    "and stares like a landlord come to collect the rent."
)


def main() -> None:
    # Gate self-check: entry must be 1-200 chars, a single line,
    # non-whitespace, with no trailing newline.
    assert 1 <= len(JOKE) <= 200, f"entry length {len(JOKE)} outside 1-200"
    assert "\n" not in JOKE and "\r" not in JOKE, "entry must be one line"
    assert JOKE.strip() == JOKE, "entry must not start/end with whitespace"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)  # no trailing newline


if __name__ == "__main__":
    main()
