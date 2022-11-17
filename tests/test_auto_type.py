from src.dictable.dictable import auto_type
import pytest

@pytest.mark.parametrize(
    "data, output",[
        ("0", 0),
        ("1", 1),
        ("10", 10),
        ("100", 100),
        ("0.1", 0.1),
        ("1.1", 1.1),
        ("True", True),
        ("False", False),
        ("", None),
    ]
)
def test_auto_type(data, output):
    assert auto_type(data) == output
