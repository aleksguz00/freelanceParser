from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def Freelance():
    options = webdriver.ChromeOptions()
    # set using device description and hide that it is a bot
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86-64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    # You need to change executable_path for your system, especially if you are using Linux
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Alexandr\\PycharmProjects\\freelance_parser\\chromedriver.exe",
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

        vacancies_list = driver.find_elements(By.CLASS_NAME, "project")

        to_day = datetime.now()
        file_name = f"{t.day}.{t.month}.{t.year}_{key_word}"
        with open(file=file, mode="w", encoding='utf8') as file:
            for vacancy in vacancies_list[:10]:
                title = vacancy.find_element(By.CLASS_NAME, "title").text
                price = vacancy.find_element(By.CLASS_NAME, "cost").text
                deadline = vacancy.find_element(By.CLASS_NAME, "term").text
                posted_time = vacancy.find_element(By.CLASS_NAME, "timeago").text
                # Old code
                # views = vacancy.find_element(By.XPATH, "//span[@title='Просмотров']")
                views = vacancy.find_element(By.CLASS_NAME, "view-count").get_attribute('title)
                # Old code
                # applied = vacancy.find_element(By.XPATH, "//span[@title='Отклики']")
                applied = vacancy.find_element(By.CLASS_NAME, "comments-count").text
                link = vacancy.find_element(By.CLASS_NAME, "description").get_attribute("href")

                # for each vacancy it creates a new text file and write down information in it

                file.write(f"{count}.{title}\nPrice: {price}\n{deadline}\nPosted: {posted_time}\nViews: {views}\nFeedback: {applied}\nLink: {link}\n{'-' * 60}\n")
      print("Done")
    except NoSuchElementException as exception
        print("Element not found and test failed")
        driver.quit()                                                                      
    finally:
        driver.close()
        driver.quit()
if __name__ == "__main__":
    Freelance()
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
                                                                                        
