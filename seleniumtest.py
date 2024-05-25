from selenium import webdriver
#set chromodriver.exe path
driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
#launch URL
driver.get("https://accounts.google.com/")
#identify element
m = driver.find_element("link text","Help")
m.click()
#obtain parent window handle
p= driver.window_handles[0]
#obtain browser tab window
c = driver.window_handles[1]
#switch to tab browser
driver.switch_to.window(c)
print("Page title :")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
# driver.switch_to.window(p)
# print("Current page title:")
# print(driver.title)
#close browser parent window
# driver.quit()