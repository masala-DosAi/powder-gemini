from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:/Users/Ruby Kumari/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument(r"profile-directory=Profile 4")

# Set up the ChromeDriver service
service = Service(r'C:/Users/Ruby Kumari/Desktop/chromedriver.exe')

# Initialize the ChromeDriver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)
your_name = '/powder'


while True:
    try:
        # Wait and look for all chats with unread message indicators (green badge)
        unread_chats = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//*[@id='pane-side']//span[contains(@aria-label, 'unread message')]")))

        # If there are any unread chats
        if unread_chats:
                    for chat in unread_chats:
                        chat.click()  # Click the chat with unread messages
                        time.sleep(1)  # Allow chat to load

                        

                        # Check if the chat is a group chat by comparing the title
                
                    

                    # Locate recent messages in the group
                        messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text")
                    if messages:
                        last_message = messages[-1].text  # Get the last message text
                        print(last_message)
                        message=last_message.split(' ')

                        # Check if your name appears in the last message
                        if your_name in message[0].lower():
                            print("You were mentioned")

                           # Send an automated reply
                            message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p'
                            message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_box_path)))
                            other_chat = driver.find_element(By.XPATH, "//*[@id='pane-side']//span[contains(@title, 'Yash')]")
                            message_box.send_keys('hello world' + Keys.ENTER)

    except Exception as e:
        print(f"Error occurred: {e}")

    # Check again after a delay
        time.sleep(1)
