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
action_chains = ActionChains(driver)
my_table = driver.find_elements_by_xpath("//tbody//tr")
for i in range(len(my_table)):
    cells = my_table[i].find_elements_by_tag_name("td")
    for j in range(len(cells)):
        cells[j].click()
        action_chains = ActionChains(driver)
        action_chains.send_keys("test").perform()

driver.switch_to_default_content()
driver.quit()
