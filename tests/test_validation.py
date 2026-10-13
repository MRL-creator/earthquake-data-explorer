"""Keep the independently calculated catalog example under the CI gate."""

from pathlib import Path
import runpy


def test_published_validation_example():
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "examples" / "validate.py"),
                   run_name="__main__")
