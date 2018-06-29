import pytest
class Test_01():
    def test_001(self):
        print("我是1")

    @pytest.mark.xfail(True, reason="预期失败")
    def test_002(self):
        print("我是2")
        raise 0

    def test_003(self):
        print("我是3")