from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver
driver = webdriver.Chrome()

# Open the login page
driver.get("http://127.0.0.1:5000/login")  # Change if needed
driver.maximize_window()

# Locate the username and password input fields
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

# Enter test credentials
username_field.send_keys("testuser")
password_field.send_keys("testpassword")

# Submit the form
password_field.send_keys(Keys.RETURN)

# Wait for the response
time.sleep(3)

# ✅ Alternative 1: Check for dashboard-specific elements
try:
    driver.find_element(By.CLASS_NAME, "dashboard-container")  # Example dashboard element
    print("✅ Login Successful: Test Passed")
except:
    try:
        error_message = driver.find_element(By.CLASS_NAME, "error")
        print("❌ Login Failed:", error_message.text)
    except:
        print("⚠ Could not determine login success or failure.")

# Close the browser
driver.quit()