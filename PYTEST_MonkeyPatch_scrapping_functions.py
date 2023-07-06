#import pandas as pd
import pytest
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from scrapping_project_py import create_dataframe
from scrapping_project_py import read_csv
from scrapping_project_py import get_driver
from scrapping_project_py import save_screenshot

def test_read_csv(monkey_patch):
    expected = "my fake reader"
    monkey_patch.setattr('read_csv.pd.read_csv',expected)
    actual = read_csv()
    assert actual == expected

def test_save_screenshot(monkeypatch):
    expected = 'my test screenshot'
    monkeypatch.setattr(save_screenshot.driver.save_screenshot, expected)
    actual = get_driver()
    assert actual == expected     

def test_create_df(monkeypatch):
    expected = 'my test df'

    def patch_df(columns):
        return columns
    
    def sub_function(columns):
        return expected

    monkeypatch.setattr(create_dataframe.pd.DataFrame, sub_function)
    actual = create_dataframe()
    assert actual == expected

def test_get_driver(moneky_patch):
    expected = 'my fake driver'
    moneky_patch.setattr('get_driver.webdriver.Chrome', expected)
    actual = get_driver()
    assert actual == expected
   

