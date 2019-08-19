from selenium import webdriver


def get_driver():
  return webdriver.Chrome(r'C:\luxmed-automation\chromedriver.exe')


