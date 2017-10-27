from abc import ABCMeta, abstractmethod


class BDbase(metaclass=ABCMeta):
    """
    Initialize a base class to inherit by every page
    """
    def __init__(self, driver):
        self.driver = driver

    @property
    @abstractmethod
    def PAGE_IDENTIFIER(self):
        """
        This property must be specified on every page
        """
        pass

    def gotoHomepage(self):
        self.driver.get("http://www.baidu.com")

    def getCurrentUrl(self):
        return self.driver.current_url
