from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

path_to_chrome_driver = "chromedriver.exe"

inv_link = input("Enter DuoLingo Invite Link: ")

friends = input("How many friends you want? ")

if len(friends) < 1:
    friends = 1

pword = "MyPassword123"


def create_account(how_many_times):
    for n in range(0, int(how_many_times)):
        print("Generating friends...")
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        driver = webdriver.Chrome(path_to_chrome_driver, options=options)
        second_driver = webdriver.Chrome(
            path_to_chrome_driver, options=options)
        age = str(randint(18, 30))
        driver.get(inv_link)

        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@data-test="language-card language-fr"]'))).click()
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Brain Training")]'))).click()
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@data-test="set-goal"]'))).click()
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[@data-test="create-profile"]'))).click()

        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Create account")]')))
        driver.find_element_by_xpath(
            '//*[@data-test="age-input"]').send_keys(age)
        second_driver.get("https://www.guerrillamail.com/inbox")
        page = second_driver.page_source
        soup = BeautifulSoup(page, "html.parser")
        email = soup.find(id="email-widget").text
        second_driver.close()
        driver.find_element_by_xpath(
            '//*[@data-test="email-input"]').send_keys(email)
        driver.find_element_by_xpath(
            '//*[@data-test="password-input"]').send_keys(pword)
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Create account")]'))).click()
        WebDriverWait(driver, 20).until(
            ec.element_to_be_clickable((By.XPATH, '//*[contains(text(), "YES, PLEASE")]'))).click()

        driver.quit()
        print("Done with Number:", n)


create_account(int(friends))
print("Have fun with your new friends")
