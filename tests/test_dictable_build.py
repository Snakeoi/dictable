from src.dictable.dictable import Dictable
import pytest


@pytest.mark.parametrize(
    "dictionary, headers, rows, table",
    [
        (
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "age": 22
                }
            ],
            ['first_name', 'last_name', 'age'],
            [
                ['John', 'Doe', 22]
            ],
            [
                ['first_name', 'last_name', 'age'],
                ['John', 'Doe', 22]
            ]
        ),
        (
            [
                {
                    "a": True,
                    "b": False,
                },
                {
                    "a": None,
                    "b": 15,
                },
                {
                    "a": "John",
                    "b": 1.22
                }
            ],
            ['a', 'b'],
            [
                [True, False],
                [None, 15],
                ["John", 1.22]
            ],
            [
                ["a", "b"],
                [True, False],
                [None, 15],
                ["John", 1.22]
            ]
        ),
        (
            [
                {
                    "a": True,
                    "b": True,
                },
                {
                    "b": True,
                    "c": True,
                },
                {
                    "a": True,
                    "c": True
                },
                {
                    "a": True
                },
                {
                    "b": True
                },
                {
                    "c": True
                }
            ],
            ['a', 'b', 'c'],
            [
                [True, True, None],
                [None, True, True],
                [True, None, True],
                [True, None, None],
                [None, True, None],
                [None, None, True]
            ],
            [
                ['a', 'b', 'c'],
                [True, True, None],
                [None, True, True],
                [True, None, True],
                [True, None, None],
                [None, True, None],
                [None, None, True]
            ]
        )
    ]
)
def test_dictable_builds_with_good_data(dictionary, headers, rows, table):
    dt = Dictable(dictionary)
    assert dt.dictable == dictionary
    assert dt.headers == headers
    assert dt.rows == rows
    assert dt.table == table
