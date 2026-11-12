import subprocess
import sys
from pathlib import Path

import pytest

from find_num_by_binary_search import search_num, search_num_recursion


SEARCH_FUNCTIONS = [
    pytest.param(
        lambda numbers, target: search_num(numbers, target),
        id="iterative",
    ),
    pytest.param(
        lambda numbers, target: search_num_recursion(
            numbers, target, 0, len(numbers) - 1
        ),
        id="recursive",
    ),
]

def test_main_prints_sample_output():
    script = Path(__file__).with_name("find_num_by_binary_search.py")
    input_text = "5\n4 1 5 2 3\n5\n1 3 7 9 5\n"

    result = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout == "1\n1\n0\n0\n1\n"
    assert result.stderr == ""