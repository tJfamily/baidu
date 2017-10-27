import pdb
import logging
import argparse

from selenium import webdriver

from baidu.products.bdproducts import BDProducts


def get_args():
    """
    Get the arguments to be used in the main entry point. Project, List
    Projects, Project Name, and Smoke are the current argument options.
    :return:
    """
    paser = argparse.ArgumentParser()
    paser.add_argument(
        '--products', type=str, default=None,
        help=''' Run Products'''
    )
    args = paser.parse_args()

    return args


def main():
    """
    Main entry point for the Dream Automated testing tool
    """
    args = get_args()
    with webdriver.Chrome() as driver:
        if args.products:
            BDProducts(driver)
        else:
            driver.close()


if __name__=="__main__":
    main()
