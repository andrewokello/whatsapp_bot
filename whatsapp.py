"""
By: Andrew Mark
Date: March 12th, 2021

Heavily inspired by Harshit Sidhwa and Julián Flores. 
For instructions or information on their implementation, please refer to https://github.com/harshitsidhwa/WhatsApp-bot-selenium/blob/master/README.md and https://github.com/robotfpv/web-whatsapp-bot/blob/master/README.md

Please do NOT use this for spam, bullying, etc.
By using this script, YOU will take FULL responsibility for anything that happens to ANYONE you use this on and anything you do with this script!.
Additionally, using this script may involve a risk of you being banned and even other risks including but not limited to: being hacked, etc.
Use this script at your own risk!
"""

from functions import *


if __name__ == "__main__":
    """
    Send WhatsApp Message to Contacts and attach PDF with a configurable limit
    """
    print('\n\n')
    print('='*80)
    print('Lets Do it!!!!!')
    print('='*80)
    print('\n\n')
    
    # Set Limit here
    limit = None
    
    start_time = time()
    # Get Bot Object
    app = WhatsappBot()

    # Open Whatsapp
    app.open_whatsapp()
    
    # Run Main Function
    app.main_func(app.get_contacts(limit=limit))

    print('\nTook {}'.format(format_timespan(round(time() - start_time, 2))))
    
    app.driver.quit()