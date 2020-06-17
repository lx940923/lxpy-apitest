
def test_version():
    from lxpy_api import __version__
    assert isinstance(__version__,str)