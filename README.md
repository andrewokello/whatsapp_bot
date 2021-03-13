# WhatsApp Bot

This is a simple Web WhatsApp Bot developed in python using Selenium. 
Selenium is used mainly for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can (and should!) be automated as well.

Selenium has the support of some of the largest browser vendors who have taken (or are taking) steps to make Selenium a native part of their browser. It is also the core technology in countless other browser automation tools, APIs and frameworks.

  - Send messages to family, friends and contacts automatically
  - Send specific message at specified time for all choosen contacts
  - Send the message in group also

   >Disclaimer - This article is for education purpose only. We didn’t share any blame for the misuse of this program.

   >Warning – These steps might get you banned permanently from using Whatsapp. So, use it wisely.

# Features!

  - Send a specific message to a particular contact at any time of the day
  - One can send a single message to multiple contacts over a specific time
  - Multiple messages to multiple contacts
  - It offers a delay so that WhatsApp can detect your are sending a URL and show its pop-up description.
  - It can search a contact from the list if the contact isn't present in the recent chats
  - Save the contact name, number in a xls file and save it in the same directory.
  - Change the message along with time in the whatsapp.py
  - You can add multiple messages
  - The Script can also search for the contact in the new chat list and then send message if the contact is not found in the recent chat list.
  
### Requirements

* [Python 3+](https://www.python.org/download/releases/3.0/?) - Pyhton 3.6+ verion
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium for web automation
* Selenium requires a driver to interface with the chosen browser.
> For [Click for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
> For [Click for FireFox](https://github.com/mozilla/geckodriver/releases)
> For [Click for safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10)


### Instructions

* Click here to download [python3](https://www.python.org/downloads/).

* Install python3 on your operating system.

* Replace the drivers in the folder in the project

* Install selenium on python3 on using

  ```sh
  $ pip3 install selenium
  ```

* Open web_whatsapp_bot.py with your favorite text editor

* Edit the message to be sent on Whatsapp.

* Create the list of the phone number with the country prefix in a list of integers format (without any symbols or spaces).

* Run whatsapp.py using Python3

  ```sh
  $ python3 whatsapp.py
  ```
* If you are running it later on, make sure you set the environment variable again

* When the browser is opened web.whatsapp.com will be opened and will ask to scan a QR code when you its first time

* Scan the QR code within time(by default 10 seconds).

* Run the script.

The program will take care of any invalid phone number.


