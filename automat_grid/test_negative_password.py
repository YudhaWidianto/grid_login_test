from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_negative_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # Enter incorrect password
    driver.find_element(By.ID,"username").send_keys("student")
    driver.find_element(By.ID,"password").send_keys("incorrectPassword")
    driver.find_element(By.ID,"submit").click()
    
    #Verify error message
    error_msg = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"error")))
    assert error_msg.is_displayed(), "Error message isn't displayed"
    assert "Your password is invalid!" in error_msg.text, "Unexpected error message"
