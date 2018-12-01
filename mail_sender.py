from selenium import webdriver
import time

username = 'username@gmail.com' # your Gmail account
password = 'your_password'      # your account's password

# list of dictionaries with the name and email address of the recipients
users = [
  {'name': 'Tom', 'email': 'Tom@fakemail.com'},
  {'name': 'Jhon', 'email': 'Jhon@gmail.com'},
  {'name': 'Felix', 'email': 'felix@testing.com'},
  {'name': 'Camila', 'email': 'camila@hotmail.com'},
  {'name': 'Brenda', 'email': 'brenda@yahoo.com'}
]

url = 'https://www.gmail.com/' # the URL to open in the browser

driver = webdriver.Chrome('./chromedriver') # Chrome driver

driver.get(url) # opens Gmail in your browser

driver.find_element_by_id('identifierId').send_keys(username) # enters your user name in the login page
driver.find_element_by_class_name('RveJvd').click() # clicks the login button
time.sleep(2)
driver.find_element_by_xpath('//*[@name="password"]').send_keys(password) # enters your password in the password field
driver.find_element_by_class_name('RveJvd').click()
time.sleep(4)


# this function opens the compose window in Gmail and fills the to, the subject and the message and finally sends the message
def send_message(name, to_address):
  driver.find_element_by_css_selector('.z0>.L3').click()
  time.sleep(4)
  driver.find_element_by_class_name('vO').send_keys(to_address)
  driver.find_element_by_xpath('//*[@name="subjectbox"]').send_keys(f"Hello {name}, this is a test message sent using python")
  driver.find_element_by_class_name('Am').send_keys(f"Hello {name}, if you have received this message is because the python scirpt works :)")
  driver.find_element_by_class_name('aoO').click()
  time.sleep(5)

# loop through each contact and sends the message
for i in range(len(users)):
  send_message(users[i]['name'], users[i]['email'])
  print(f"Message sent to {users[i]['name']}")
  time.sleep(2)

print("All messages has been successfully sent :)")


