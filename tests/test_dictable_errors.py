from src.dictable.dictable import Dictable, DictableError
import pytest

@pytest.mark.parametrize(
    "data", [
        ("string"),
        (10),
        (1.1),
        (True),
        (False),
        (None)
    ]
)
@pytest.mark.exception
def test_dictable_if_object_is_not_list(data):
    with pytest.raises(DictableError):
        assert Dictable(data)

@pytest.mark.parametrize(
    "data", [
        (["string"]),
        ([10]),
        ([1.1]),
        ([True]),
        ([False]),
        ([None])
    ]
)
@pytest.mark.exception
def test_dictable_if_list_contains_not_dict(data):
    with pytest.raises(DictableError):
        assert Dictable(data)