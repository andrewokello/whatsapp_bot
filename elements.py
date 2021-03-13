from selenium.webdriver.common.by import By


class elements:
    message_box = {"type": By.NAME,
                   "name": "/html/body/div/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"}
    add_attach = {"type": By.CSS_SELECTOR,
                  "name": "span[data-icon='clip']"}
    find_file = {"type": By.CSS_SELECTOR,
                 "name": "input[type='file']"}
    send_attach = {"type": By.CSS_SELECTOR,
                   "name": "span[data-icon='send-light']"}

    send_attach = {"type": By.XPATH,
                   "name": "/html/body/div/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span"}
