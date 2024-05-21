from __future__ import print_function
import sys
from threading import Timer
from datetime import datetime, timedelta
import time
import splinter as sp
from splinter import Browser

# Enter personal info here!
confirmation_number = 'ABC123'
first_name = 'PAUL'
last_name = 'LISKER'
departure_day = 16
departure_month = 9
departure_year = 2016   # 4 digits
departure_hour = 18     # 24 hour format
departure_minute = 50

spin_cursor = False

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

def checkin(browser):
    spin_cursor = False
    time.sleep(3)  # To make sure that their server allows for checking in.
    checkin_button = browser.find_by_id('form-mixin--submit-button')
    checkin_button.click()
    time.sleep(3)
    print_documents_button = browser.find_by_xpath("//button[contains(text(), 'Print Documents')]")
    print_documents_button.click()
    print('Checked in at', datetime.now())
    print("")
    quit(browser)
    return

def get_input():
    get_user_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_user_input = raw_input

    return get_user_input()

def quit(browser):
    print("When you're finished, click enter to close the browser session.")
    get_input()
    browser.quit()

def main(confirmation_number, first_name, last_name, departure_day,
         departure_month, departure_year, departure_hour, departure_minute):
    webdriver_path = '/Users/jakeschinasi/Downloads/chromedriver_mac64'
    browser = sp.Browser('chrome', executable_path=webdriver_path)
    browser.visit('https://checkin.jetblue.com/checkin')
    
    # Find the confirmation code input field using CSS attribute selector
    confirmation_input = browser.find_by_css('input[name="confirmationCode"]')
    # Clear the input field before filling it (optional)
    confirmation_input.first.fill('')
    # Fill the confirmation code input field
    confirmation_input.first.fill(confirmation_number)
    
    # Find the last name input field using CSS attribute selector
    last_name_input = browser.find_by_css('input[name="lastName"]')
    # Clear the input field before filling it (optional)
    last_name_input.first.fill('')
    # Fill the last name input field
    last_name_input.first.fill(last_name)

    # Rest of your code...

if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    browser = main(confirmation_number, first_name, last_name, departure_day,
                   departure_month, departure_year, departure_hour,
                   departure_minute)

    spinner = spinning_cursor()
    while spin_cursor:
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

    print("When you're finished, click enter to close the browser session.")
    get_input()
    browser.quit()
