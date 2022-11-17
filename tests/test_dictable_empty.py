from src.dictable.dictable import Dictable


class TestDictableEmpty:

    def setup(self):
        self.dt = Dictable([])

    def test_empty_dictable_dictable(self):
        assert self.dt.dictable == []

    def test_empty_dictable_headers(self):
        assert self.dt.headers == []

    def test_empty_dictable_rows(self):
        assert self.dt.rows == []

    def test_empty_dictable_table(self):
        assert self.dt.table == []
