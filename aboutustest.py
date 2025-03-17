from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1️⃣ Setup WebDriver
driver = webdriver.Chrome()

try:
    # 2️⃣ Open the About Us page
    driver.get("http://127.0.0.1:5000/about")  # Change if needed
    driver.maximize_window()
    time.sleep(2)  # Wait for elements to load

    # 3️⃣ Verify Page Title
    expected_title = "login and registration form"
    assert driver.title == expected_title, f"❌ Title Mismatch! Expected: {expected_title}, Found: {driver.title}"
    print("✅ Page Title Verified!")

    # 4️⃣ Verify Navigation Bar Links
    expected_links = ["/home", "/login", "/about", "/services", "/contact"]
    nav_links = driver.find_elements(By.CSS_SELECTOR, ".navbar a")
    found_links = [link.get_attribute("href") for link in nav_links]

    for link in expected_links:
        assert any(link in found for found in found_links), f"❌ Missing Nav Link: {link}"
    print("✅ Navigation Links Verified!")

    # 5️⃣ Verify About Us Section
    about_heading = driver.find_element(By.TAG_NAME, "h1").text
    assert about_heading == "About Us", f"❌ Incorrect heading! Found: {about_heading}"
    print("✅ About Us Heading Verified!")

    # 6️⃣ Verify Read More Button
    read_more_btn = driver.find_element(By.CSS_SELECTOR, ".button a")
    assert read_more_btn.get_attribute("href").endswith("/services"), "❌ Read More button link incorrect!"
    print("✅ Read More Button Verified!")

    # 7️⃣ Verify Social Media Icons
    social_icons = driver.find_elements(By.CSS_SELECTOR, ".social a i")
    expected_classes = ["bxl-facebook", "bxl-twitter", "bxl-instagram"]
    for expected_class in expected_classes:
        assert any(expected_class in icon.get_attribute("class") for icon in social_icons), f"❌ Missing: {expected_class}"
    print("✅ Social Media Icons Verified!")

    # 8️⃣ Verify Image Section
    image = driver.find_element(By.CSS_SELECTOR, ".image-section img")
    assert image.get_attribute("src").endswith("abt.jpg"), "❌ About Us Image not found!"
    print("✅ About Us Image Verified!")

    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY!")

except AssertionError as e:
    print(e)

finally:
    # 9️⃣ Close Browser
    driver.quit()