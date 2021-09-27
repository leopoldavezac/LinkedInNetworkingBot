from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

VERIFY_LOGIN_ID = "global-nav-search"
REMEMBER_PROMPT = 'remember-me-prompt__form-primary'

def login(driver:webdriver.Chrome, email_address:str, password:str):
 
  driver.get("https://www.linkedin.com/login")
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

  email_elem = driver.find_element_by_id("username")
  email_elem.send_keys(email_address)

  password_elem = driver.find_element_by_id("password")
  password_elem.send_keys(password)
  password_elem.submit()

  try:
    if driver.url == 'https://www.linkedin.com/checkpoint/lg/login-submit':
      remember = driver.find_element_by_id(REMEMBER_PROMPT)
      if remember:
        remember.submit()

    # WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, VERIFY_LOGIN_ID))) to be used in test login
  except: pass