from selenium import webdriver
from selenium.webdriver.common.keys import Keys

APP_URL = "https://www.eenadu.net/archivespage/districtnewsdetails/68463/529/n/2019-03-16"

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()

