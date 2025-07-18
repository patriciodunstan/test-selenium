from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_page_title():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get("https://www.github.com")

    titleElement = browser.find_element(
        By.ID,'hero-section-brand-heading'
    )

    assert titleElement.text == "Build and ship software on a single, collaborative platform"

    browser.quit()

