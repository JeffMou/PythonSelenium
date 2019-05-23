from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.get("https://ueditor.baidu.com/website/onlinedemo.html")
insert_table = driver.find_element_by_id("edui249_button_body")
insert_table.click()

table = driver.find_element_by_xpath("//div[@id='edui250']//div//div[2]")
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(table, 88,88).click().perform()

driver.switch_to_frame("ueditor_0")
my_table = driver.find_element_by_xpath("//tbody")
trs = my_table.find_elements_by_tag_name("tr")
for tr in trs:
    tds = tr.find_elements_by_tag_name("td")
    for td in tds:
        td.click()
        action_chains = ActionChains(driver)
        action_chains.send_keys("test").perform()

driver.switch_to_default_content()
driver.quit()

