from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

try:
    driver.get('https://www.cslb.ca.gov/OnlineServices/CheckLicenseII/CheckLicense.aspx')

    wait = WebDriverWait(driver, 5)  # Increased wait time

    input_field = driver.find_element(By.NAME, "ctl00$MainContent$LicNo")
    input_field.send_keys("890895")

    button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'SearchButton')))  # Adjust selector as needed
    button.click()
    time.sleep(5) 

    button = wait.until(EC.element_to_be_clickable((By.ID, 'MainContent_SalespersonLink')))  # Adjust selector as needed
    button.click()
    time.sleep(5) 
    

    while True:
        
        for i in range(25):
            nameString = "MainContent_dlHisList_hlName_"+str(i)
            button = wait.until(EC.element_to_be_clickable((By.ID, nameString)))  # Adjust selector as needed
            button.click()
            time.sleep(5) 

            nameElement = driver.find_element(By.ID, "MainContent_HISName")
            name = nameElement.text
            addressElement = driver.find_element(By.ID, "MainContent_Address1")
            address = addressElement.text
            cityElement = driver.find_element(By.ID, "MainContent_CityStateZip")
            city = cityElement.text
            phoneElement = driver.find_element(By.ID, "MainContent_PhoneNumber")
            phone = phoneElement.text
            HISElement = driver.find_element(By.ID, "MainContent_HIS_No")
            HIS = HISElement.text
            issueElement = driver.find_element(By.ID, "MainContent_issueDate")
            issue = issueElement.text
            expiraElement = driver.find_element(By.ID, "MainContent_expirationDate")
            expira = expiraElement.text
            with open('output.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                
                # Write new rows to the file
                writer.writerows([[name, address, city, phone, HIS, issue, expira]])
            driver.back()
        nextButton = driver.find_element("id", "MainContent_btnNext")
        is_disabled = nextButton.get_attribute("disabled")
        if is_disabled:
            break
        nextButton.click()
        time.sleep(5)
        

finally:
    # Close the WebDriver
    driver.quit()