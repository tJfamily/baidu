from baidu.products.nuomi import NuomiPage


def test_get_nuomi_logo(driver_mock):
    nmpage = NuomiPage(driver_mock)
    driver_mock.find_element_by_css_selector.return_value.get_attribute.return_value = "test"
    assert nmpage.get_nuomi_logo() == "test"


def test_search_by_words_nuomi(bdps, driver_mock):
    bdps.nuomipage.search_by_words_nuomi("cake")
    bdps.nuomipage.driver.find_element_by_css_selector.return_value.send_keys.assert_called_once_with("cake")
    assert bdps.nuomipage.driver.find_element_by_css_selector.return_value.submit.called
    assert driver_mock.find_element_by_css_selector.called
