from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# APP_URL = "https://www.eenadu.net/archivespage/districtnewsdetails/68463/529/n/2019-03-16"

driver = webdriver.Chrome("./chromedriver.exe")
driver.maximize_window()


print(headings_url("01-04-2019"))


def headings_url(date):
    #    pass date in dd-mm-yyyy format
    driver.get("https://www.eenadu.net/archivespage/more/{}".format(date))
    section = driver.find_element_by_tag_name(
        "main").find_elements_by_tag_name("section")[1]
    li_list = section.find_element_by_tag_name(
        "ul").find_elements_by_tag_name("li")
    urls = []
    for i in li_list:
        urls.append(i.find_element_by_tag_name("a").get_property("href"))
    return urls
