from setuptools import setup, find_packages


setup(
    name="baidu",
    version="0.0.1",
    description="",
    url="",
    packages=find_packages(),
    install_requires=[
        'selenium',
        'requests',
        'pyvirtualdisplay',
    ],
    test_suite="tests",
    entry_point={
      "console_scripts": [
          "baidu=baidu.cli:main",
      ]
    },

)