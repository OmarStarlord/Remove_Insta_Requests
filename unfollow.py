from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

chromedriver_path = "C:\\Users\\{User}\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Import usernames from csv 
usernames = []
with open('usernames.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        usernames.append(row[0])

def remove_follow_request(driver, username):
    try:
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(5)  # Wait for the page to load

        try:
            # Updated XPath for "Requested" button
            requested_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, '_aaco') and text()='Requested']"))
            )
            print(f"Follow request found for {username}. Attempting to remove...")
            requested_button.click()  # Click on the "Requested" button
            time.sleep(2)

            # Updated XPath for "Unfollow" button
            unfollow_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(@class, '_a9--') and text()='Unfollow']"))
            )
            unfollow_button.click()  # Click on the "Unfollow" button to remove the follow request
            time.sleep(2)
            print(f"Follow request removed for {username}.")

        except Exception as e:
            print(f"No follow request found for {username}: {str(e)}")

    except Exception as e:
        print(f"Failed to process {username}: {str(e)}")

# Set up Chrome WebDriver
service = Service(chromedriver_path)
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram login page
driver.get("https://www.instagram.com/accounts/login/")

# Wait for manual login before proceeding
input("Please log in to Instagram and then press Enter to continue...")

# Iterate through the usernames and remove follow requests
for username in usernames:
    remove_follow_request(driver, username)
    time.sleep(5)

# Close the browser
driver.quit()
