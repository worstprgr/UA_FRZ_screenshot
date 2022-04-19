#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from pathlib import Path

# chrome config
chromeOptions = Options()
chromeOptions.headless = True
chromeOptions.add_argument("--window-size=1920x1080")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument("--no-sandbox")
s = Service('/usr/bin/chromedriver')  # Linux
# s = Service('C:/chromedriver/chromedriver.exe')  # Windows

driver = webdriver.Chrome(service=s, options=chromeOptions)

# set geolocation
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
    "latitude": 50.73873801240445,
    "longitude": 33.908773265183434,
    "accuracy": 100
})


url = [
    'https://www.radarbox.com/@46.74259,28.94285,z4',
    'https://www.flightradar24.com/43.57,34.39/4',
    'https://planefinder.net/'
]

pages = [
    'RADARBOX', 'FLIGHTRADAR24', 'PLANEFINDER'
]

absolute_path = '/home/pi/PYTHON/scr_ukraine_flight/'

main_delay = 30  # default: 30


# count section
Path(absolute_path + 'count.txt').touch(exist_ok=True)

# write zeros if file is empty
csv_empty = os.stat(absolute_path + 'count.txt').st_size == 0

if csv_empty is True:
    with open(absolute_path + 'count.txt', 'w') as cvw:
        cvw.write('0')

# get count
with open(absolute_path + 'count.txt', 'r') as of:
    count = int(of.read())

print('[COUNT]: ' + str(count))

print('# # # # ' + pages[0] + ' # # # #')
try:
    # radarbox
    driver.get(url[0])
    time.sleep(main_delay)
    print(pages[0] + ': Taking screenshot')
    driver.save_screenshot(absolute_path + '0/scr_' + str(count) + '.png')
    time.sleep(1)
    driver.quit()
except:
    print(pages[0] + ': Connection Error/Timeout')
    pass

# sleep between get_url
print()
time.sleep(2)

# save count
print('[Saving count]')
with open(absolute_path + 'count.txt', 'w') as cf:
    cf.write(str(count + 1))

# */30 * * * * python3 /home/pi/PYTHON/scr_ukraine_flight/main.py > /cronlog
