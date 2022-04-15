from bybit_api import BybitAPI
from selenium import webdriver
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from settings import ID_BOX, SALE_TIME, HEADERS, REQUESTS_NUMBER

import time


bybit = BybitAPI(ID_BOX)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.bybit.com/en-US/login")


input('Залогинтесь и нажмите Enter')
driver.get(f'https://www.bybit.com/en-US/nft/detail/?id={ID_BOX}')

time.sleep(15)
resp = [request for request in driver.requests if request.url == 'https://api2.bybit.com/spot/api/nft/v1/user/userInfo']
HEADERS['usertoken'] = resp[0].headers['usertoken']
time.sleep(5)



while True:
    time_now = time.time()
    if SALE_TIME > time_now:
        print(f'{SALE_TIME - time_now} - осталось секунд')

    if (SALE_TIME - 2) < time_now:
        bybit.startSsc(HEADERS)
        break

for result in bybit.results:
    print(result)

time.sleep(99999)
