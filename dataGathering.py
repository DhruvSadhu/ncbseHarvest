import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# # Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# # Navigate to the website
driver.get("https://cf.ncsbe.gov/CFDocLkup/DocumentResult/?year=2023&reports=%27SO%27")

# # Wait for the table to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "gridDocumentResults")))

# #store the table
table = driver.find_element(By.ID, "gridDocumentResults")
#store the table
tableHead = table.find_element(By.CSS_SELECTOR, "thead")

# print each  column header
thList = tableHead.find_elements(By.CSS_SELECTOR, "th")
for th in thList:
    print(th.text)

tBody = table.find_element(By.CSS_SELECTOR, "tbody")
tRows = tBody.find_elements(By.CSS_SELECTOR, "tr")
for row in tRows:
    rowDatas = row.find_elements(By.CSS_SELECTOR, "td")
    for data in rowDatas:
        print(data.text, end=" ")
    print("")

