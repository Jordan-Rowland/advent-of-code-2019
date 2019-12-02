from day2 import *


class TestDay2:
    def test1(self):
        assert opcodes([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]

    def test2(self):
        assert opcodes([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]

    def test3(self):
        assert opcodes([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]

    def test4(self):
        assert opcodes([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_noun_verb(self):
        assert noun_verb(19690720) == # Answer hidden
