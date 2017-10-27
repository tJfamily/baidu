# Standard Imports
from unittest import mock

# Third Party Imports
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver_mock():
    """ Return a mock selenium driver object
    """
    return mock.create_autospec(webdriver.Chrome)