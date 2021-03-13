# Selenium imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Imports
import platform
from time import sleep, time
from pathlib import Path
from elements import *
import pandas as pd
import traceback
from alive_progress.core.progress import alive_bar
from pathlib import Path
from humanfriendly import format_timespan


class WhatsappBot:
    """
    This is the main part of the bot and contains all its functions
    """

    def __init__(self):
        options = Options()
        if platform.system() == 'Darwin':
            self.driver = webdriver.Chrome(
                options=options, executable_path=str(Path('..').cwd()) + '/drivers/chromedriver_mac')
        elif platform.system() == 'Linux':
            self.driver = webdriver.Chrome(
                options=options, executable_path=str(Path('..').cwd()) + '/drivers/chromedriver_linux')
        else:
            self.driver = webdriver.Chrome(
                options=options, executable_path=str(Path('..').cwd()) + '\drivers\chromedriver.exe')

    def open_whatsapp(self):
        self.driver.get("https://web.whatsapp.com")
        print('Please Scan the QR code within 10 secs')
        sleep(10)  # wait time to scan the code in second
        print('3 secs left.\n\n')
        sleep(4)

    def get_contacts(self, limit: int = None):
        """
        Gets the contact names and number within the limit
        :param  limit: int
        :return contact: dataframe
        """
        if limit:
            return pd.read_csv('contacts.csv')[:limit]
        else:
            return pd.read_csv('contacts.csv')

    def get_text(self, target: str):
        """
        Creates custom message to send and returns it
        :param contact_name: str
        :return custom_message: str
        """
        main_text = 'This is a test'
        skip_line = '\n'
        return 'Hello {target}{skip_line}{skip_line}{main_text}'.format(target=target, main_text=main_text, skip_line=skip_line)

    def get_pdf(self):
        """
        Gets the pdf to send to the contact using the contact name
        :param contact_name: str
        :return custom_message: str
        """
        return str(Path('..').cwd()) + '/pdfs/the only pdf.pdf'

    def send_message(self, contact_name: str, contact_number: int, sent: list, failed: list):
        """
        Sends custom message to given number on whatsapp and attaches a pdf document
        :param  contact_name: str
                contact_number: int
                sent: list
                failed: list
        :return:    sent: list
                    failed: list
        """
        self.driver.get(
            "https://web.whatsapp.com/send?phone={}&source=&data=#".format(contact_number))
        sleep(10)

        try:
            message_box = self.driver.find_element_by_xpath(
                elements.message_box['name'])
            message_box.send_keys(self.get_text(contact_name))
            message_box.send_keys(Keys.ENTER)
            sent.append(contact_number)
        except Exception as e:
            failed.append(contact_number)
            # print(traceback.print_exc())

        try:
            sleep(2)
            self.driver.find_element_by_css_selector(
                elements.add_attach['name']).click()
            sleep(2)
            self.driver.find_element_by_css_selector(
                elements.find_file['name']).send_keys(self.get_pdf())
            sleep(2)
            self.driver.find_element_by_xpath(
                elements.send_attach['name']).click()
        except Exception as e:
            pass
            # print(traceback.print_exc())

    def main_func(self, contacts: dict):
        """
        This is the main function in the class. It loops through the dataframe and calls the send_message function while showing a progress bar
        :param  contacts: dict
        :return None (calls function to send message)
        """
        sent, failed = [], []
        with alive_bar(len(contacts)) as bar:
            for index, contact in contacts.iterrows():
                bar.text('Sending Message to {}'.format(contact['name']))
                sleep(5)
                self.send_message(
                    contact['name'], contact['phone number'], sent, failed)
                bar()

        # Create sent and failed list
        df = pd.DataFrame(sent, columns=["Phone Number"])
        df.to_csv('success.csv', index=False)

        df = pd.DataFrame(failed, columns=["Phone Number"])
        df.to_csv('failed.csv', index=False)
