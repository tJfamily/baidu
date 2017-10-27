import pytest

from baidu.products.bdproducts import BDProducts


@pytest.fixture(scope="function")
def bdps(driver_mock):
    return BDProducts(driver_mock)