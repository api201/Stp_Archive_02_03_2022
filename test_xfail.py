import pytest

#@pytest.mark.xfail(condition=False, reason = "This is bug")
#@pytest.mark.xfail(condition=False, reason = "STRING")
@pytest.mark.xfail(strict=True)
#@pytest.mark.xfail(condition=True)
def test_succeed():
    assert True

@pytest.mark.xfail
def test_not_succeed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False