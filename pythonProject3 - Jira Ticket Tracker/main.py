from selenium import webdriver
import time as t
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

#open chrome
driver = webdriver.Chrome()

#login to jira
driver.get('https://jira.mspbots.ai/')
login_element = driver.find_element('name','os_username')
login_element.send_keys('nathan.bustamante')
login_element = driver.find_element('name','os_password')
login_element.send_keys('4lKPB#K87t')
login_element.submit()

t.sleep(10)
driver.get('https://jira.mspbots.ai/projects/ON/queues')

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'element-id'))
#     )
#     print 'element is ready!'
# except TimeoutError:
#     print'Took Too long!'

while True:
    pass



driver.quit()