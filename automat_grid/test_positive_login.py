from selenium.webdriver.common.by import By

def test_positive_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Enter correct username and password
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    
    #Verify success login page
    assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url, "Wrong login URL"
    
    post_title = driver.find_element(By.CLASS_NAME,"post-title")
    assert "Logged In Successfully" in post_title.text, "New page contains unexpected text"
    
    assert driver.find_element(By.CLASS_NAME,"wp-block-button").is_displayed(), "Logout button isn't displayed"
