import selenium
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Set up the credentials for the Sheets API
credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=credentials)

# Define the spreadsheet properties
spreadsheet = {
    'properties': {
        'title': 'My New Spreadsheet'
    }
}

try:
    # Create the spreadsheet
    spreadsheet = service.spreadsheets().create(body=spreadsheet, fields='spreadsheetId').execute()
    print(f'Spreadsheet ID: {spreadsheet["spreadsheetId"]}')
except HttpError as error:
    print(f'An error occurred: {error}')



print("Done")
exit()
      
# Set up the ChromeDriver with Selenium
options = Options()
driver = webdriver.Chrome(options=options)

# Navigate to the page
url = 'https://cf.ncsbe.gov/CFDocLkup/DocumentResult/?year=2022&reports=%27SO%27'
driver.get(url)

# Find the table element and get all the rows
table = driver.find_element(By.ID, "gridDocumentResults")
rows = table.find_elements(By.XPATH,'//tr')

# Loop through the rows and print out the data in each cell
for row in rows:
    cells = row.find_elements(By.XPATH,'.//td')
    for cell in cells:
        print(cell.text)

# Close the browser window
driver.quit()