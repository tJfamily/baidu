def test_base_init(bdps):
    assert hasattr(bdps.homepage, 'driver')


def test_gotoHomepage(bdps):
    bdps.homepage.gotoHomepage()
    assert bdps.homepage.driver.get.called