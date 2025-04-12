import time
import joblib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Load model and vectorizer
model = joblib.load("/Users/hari1476/Desktop/instasafe/model/nlp_model.pkl")
vectorizer = joblib.load("/Users/hari1476/Desktop/instasafe/model/vectorizer.pkl")

# Setup Chrome
options = Options()
options.add_argument("--user-data-dir=/tmp/insta-profile")  # Persist login
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Instagram DMs
driver.get("https://www.instagram.com/direct/inbox/")
print("⚠️ Please log in manually if needed...")
time.sleep(30)

print("🧠 Monitoring DMs for offensive messages...")

def is_offensive(text):
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return prediction[0] == 1  # Offensive

while True:
    try:
        time.sleep(5)
        elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'x1i10hfl') or contains(@class,'_aacl')]")

        for el in elements:
            try:
                text = el.text.strip()
                if text and is_offensive(text):
                    print(f"🚨 Offensive DM detected:\n{text}")
                    driver.execute_script("arguments[0].scrollIntoView(true);", el)
                    time.sleep(2)

                    # Go to container with 3-dot menu
                    container = el.find_element(By.XPATH, "./ancestor::div[contains(@class, 'x1lliihq')]")
                    menu_button = container.find_element(By.XPATH, ".//div[@aria-label='More options']")

                    driver.execute_script("arguments[0].click();", menu_button)
                    time.sleep(2)

                    # Click "Unsend"
                    unsend_option = driver.find_element(By.XPATH, "//div[text()='Unsend']")
                    driver.execute_script("arguments[0].click();", unsend_option)
                    time.sleep(2)

                    # Confirm unsend
                    confirm_button = driver.find_element(By.XPATH, "//button[text()='Unsend']")
                    driver.execute_script("arguments[0].click();", confirm_button)
                    print("🗑️ Message unsent.\n")

            except Exception as e:
                print("⚠️ Error in individual message:", e)

    except KeyboardInterrupt:
        print("🛑 Monitoring stopped by user.")
        break
    except Exception as e:
        print("⚠️ General loop error:", e)
