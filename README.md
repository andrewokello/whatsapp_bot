# WhatsApp Bot

This is a simple Web WhatsApp Bot developed in python using Selenium.
Heavily inspired by Harshit Sidhwa and Julián Flores and most of this readme document is a version of theirs.
For instructions or information on their implementation, please refer to https://github.com/harshitsidhwa/WhatsApp-bot-selenium/blob/master/README.md and https://github.com/robotfpv/web-whatsapp-bot/blob/master/README.md 

Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

  - Send messages to family, friends and contacts automatically
  - Send documents to family, friends and contacts
  
   >Disclaimer - This project is for education purpose only. I do not condon misuse.

   >Warning – These steps might get you banned permanently from using Whatsapp. So, use it wisely.

# Features!

  - Send a specific message to a particular contact.
  - One can send a single message to multiple contacts.
  - One can set a limit to the number of contacts they want to send to.
  - Save the contact name, number in a csv file and save it in the same directory.
  
### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* Selenium requires a driver to interface with the chosen browser.
> For [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)


### Instructions

* Click here to download [python3](https://www.python.org/downloads/).

* Install python3 on your operating system.

* Replace the drivers in the folder in the project

* Install the requirements on python3 on using on your preferred terminal.

  ```sh
  $ pip3 install -r requirements.txt
  ```

* Open web_whatsapp_bot.py with your favorite text editor

* Edit the message to be sent on Whatsapp.

* Create the list of the phone number with the country prefix in a list of integers format (without any symbols or spaces).

* The Contacts file needs to be a CSV file with the following column names: name ; phone number (please make sure there is no space before the column names)

* If you want to attach a Document, add the document to the PDFs folder and name it. Change this name in Line 71 on functions.py

* If you want to set a Limit to the number of contacts to message, change this on Line 28 on whatsapp.py

* Run whatsapp.py using Python3

  ```sh
  $ python3 whatsapp.py
  ```

* When the browser is opened web.whatsapp.com will be opened and will ask to scan a QR code when you its first time

* Scan the QR code within time(by default 10 seconds).

* Run the script.

The program will take care of any invalid phone number.


