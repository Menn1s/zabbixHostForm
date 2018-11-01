import selenium
from selenium import webdriver

#Use Chrome as the browser
driver = webdriver.Firefox()

#Open the web form
driver.get('http://172.16.98.230/zabbix/index.php')


#Select the host entry box
name_box = driver.find_element_by_id('name')
#Get the hostname from the user
name_box.send_keys(input("Enter username: "))
