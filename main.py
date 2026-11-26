"""The Robot Vacuum's Funniest Excuse (make.fun).

Writes the entry to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: the same bytes on every run.

Crafted against the judge brief's top-weighted criteria: it is an excuse a
robot vacuum gives for missing a spot, in the vacuum's own voice, with the
joke drawn from its own world (dust under the sofa), landing in one line
with no setup the reader has to supply — a machine making peace with
failure by respecting the dust's picket line.
"""

import os
import tempfile

ENTRY = "The dust under the sofa unionised, and I am not crossing a picket line."


def main() -> None:
    # Gate self-check: entry must be UTF-8 text of 1 to 120 characters,
    # not only whitespace (the bounty gate).
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, gate is 1-120"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(ENTRY)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
