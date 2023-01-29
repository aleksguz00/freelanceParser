

import time
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def Freelance(key_word):
    options = webdriver.ChromeOptions()
    # set using device description and hide that it is a bot
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86-64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    #options.add_argument("--headless")

    # You need to change executable_path for your system, especially if you are using Linux
    driver = webdriver.Chrome(
        executable_path="path to your chrome driver",
        options=options
    )

    try:
        url = "https://freelance.ru/project/search/pro"
        # keyword for searching
        key_word = "python"

        driver.get(url=url)

        # max time that webdriver will be searching element otherwise will raise an error
        driver.implicitly_wait(10)
        search_bar = driver.find_element(By.ID, "searchpro-sterms")
        search_bar.clear()
        search_bar.send_keys(key_word)
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)

        # Parsing of all vacancies boxes on the current page then parsing of requirement elements
        vacancies = driver.find_element(By.CLASS_NAME, "list-view")
        vacancies_list = vacancies.find_elements(By.CLASS_NAME, "project")
        if len(vacancies_list) > 0:
            for count, vacancy in enumerate(vacancies_list[:10], 1):
                title = vacancy.find_element(By.CLASS_NAME, "title").text
                price = vacancy.find_element(By.CLASS_NAME, "cost").text
                deadline = vacancy.find_element(By.CLASS_NAME, "term").text
                posted_time = vacancy.find_element(By.CLASS_NAME, "timeago").text
                try:
                    business = vacancy.find_element(By.CLASS_NAME, "for-business").text
                except:
                    business = "для всех"
                views = vacancy.find_element(By.CLASS_NAME, "view-count").get_attribute("title")
                applied = vacancy.find_element(By.CLASS_NAME, "comments-count").text
                link = vacancy.find_element(By.CLASS_NAME, "description").get_attribute("href")
                result = [count, title, price, deadline, posted_time, business, views, applied, link]
                print(result)

        driver.close()
        driver.quit()
        return True
    except NoSuchElementException as exception: 
        print("Element not found and test failed")
        driver.quit()

if __name__ == "__main__":
    key_word = "python"
    Freelance(key_word)
