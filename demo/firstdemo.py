from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://auto.51autogo.com:448/crm-admin/login.jsp#")
driver.find_element_by_name("username").send_keys("15129180359")
driver.find_element_by_name("password").send_keys("Lbb123456")
driver.find_element_by_name("capText").send_keys("IlXbPk4Q8FRNXurPd2onqQ==")
driver.find_element_by_xpath("//html/body/div/div/form/div[5]/a").click()

driver.close()
driver.quit()