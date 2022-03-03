import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import form_data
from form_service import FormService


def main():
    
    service = Service(ChromeDriverManager(version='98.0.4758.102').install())
    options = webdriver.ChromeOptions()
    options.add_argument("-incognito")
    #options.add_argument("--headless")
    #options.add_argument("disable-gpu")

    web_driver = webdriver.Chrome(service=service, options=options)
    web_driver.get(url=form_data.short_google_url)
        
    toggles = web_driver.find_elements(by=By.CLASS_NAME, value="docssharedWizToggleLabeledContainer")
    text_fields = web_driver.find_elements(by=By.XPATH, value="//input[@type='text']")
    text_fields = [text_fields[1], text_fields[2]]
    submit = web_driver.find_element(by=By.XPATH, value="//span[contains(.,'Отправить')]")


    form_service = FormService(# service=service, 
                                # web_driver=web_driver,
                                toggles=toggles,
                                text_fields=text_fields,
                                submit=submit)

    form_service.get_random_answers()
    # form_service.test()
    # time.sleep(60)
    # submit.click()
    time.sleep(10)
    web_driver.close()


if __name__ == "__main__": main()