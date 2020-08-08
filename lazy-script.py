#!/usr/bin/python3

import webbrowser
import time
import os

sec_time_sleep_interval = 1

#url = 'https://docs.python.org/'

# Open URL in new window, raising the window if possible.
#webbrowser.open_new(url)

# Open URL in a new tab, if a browser window is already open.

answer1 = str(input('1)Do you want to open links in a new tabs in default web-browser? [yes/no] '))

if answer1.lower() == 'yes':
    
    print('Starting to open up a job related links in a new tabs\n\n')

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    webbrowser.open_new_tab('https://docs.python.org/')
    time.sleep(sec_time_sleep_interval)

    print("All tabs are opened\n\n")
 
else:
    
    print('Your answer is no, so links in a new tabs would not be opened!\n\n')

    answer2 = str(input('2)Do you want to open monitoring tools in a new window of a browser? [yes/no] '))

if answer2.lower() == 'yes':
        print('Starting to open up tools in a new Windows of a browser')
        webbrowser.open_new('https://docs.python.org/')
        time.sleep(sec_time_sleep_interval)

        webbrowser.open_new('https://docs.python.org/')
else:
        print('3) Your answer is no, so tools would not be opened in a new window of web-browser!\n\n')

answer3 = str(input('Do you want to start Thunderbird? [yes/no] '))

if answer3.lower() == 'yes':
    print('Starting to open Thunderbird mail client.\n\n')
    os.system('thunderbird &')
else:
    print('Your answer is no, so Thunderbird would not be started!\n\n')
