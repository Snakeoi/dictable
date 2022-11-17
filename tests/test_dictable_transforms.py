from src.dictable.dictable import Dictable
import pytest


class TestDictableTransform:

    def setup(self):
        self.dt = Dictable(
            [{
                "name": "John",
                "age": 10
            }]
        )

    @pytest.mark.parametrize(
        "key, value, row",
        [
            ("name", "Jan", ["Jan", 10]),
            ("name", None, [None, 10]),
            ('age', None, ["John", None]),
            ("age", 12.0, ["John", 12.0]),
        ]
    )
    def test_change_values(self, key, value, row):
        self.dt.dictable[0][key] = value
        assert self.dt.table == [
            ['name', 'age'],
            row
        ]

    @pytest.mark.parametrize(
        "key, value, row",
        [
            ("a", "string", ["John", 10, "string"]),
            ("b", 1.1, ["John", 10, 1.1]),
            ('c', 12, ["John", 10, 12]),
            ("d", True, ["John", 10, True]),
            ("e", None, ["John", 10, None]),
        ]
    )
    def test_add_headers(self, key, value, row):
        self.dt.dictable[0][key] = value
        self.dt.dictable.append({
            "name": "Jane",
            "age": 10,
        })
        assert self.dt.table == [
            ['name', 'age', key],
            row,
            ['Jane', 10, None]
        ]
