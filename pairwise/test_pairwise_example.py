import pytest
from allpairspy import AllPairs


class TestParameterized(object):

    @pytest.mark.parametrize(("brand, operating_system, minute"), [
        value_list for value_list in AllPairs([
            ["X", "Y"],
            ["98", "NT", "2000", "XP"],
            [10, 15, 30, 60]
        ])
    ])
    def test_with_pw(self, brand, operating_system, minute):
        pass

    @pytest.mark.parametrize("brand", ["X", "Y"])
    @pytest.mark.parametrize("operating_system", ["98", "NT", "2000", "XP"])
    @pytest.mark.parametrize("minute", [10, 15, 30, 60])
    def test_no_pw(self, brand, operating_system, minute):
        pass
