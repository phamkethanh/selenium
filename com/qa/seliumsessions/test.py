import random

from selenium import webdriver

proxyList = [
    'us-10m.homeip.io:30000',
    'us-10m.homeip.io:30001',
    'us-10m.homeip.io:30002'
]
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/phamkethanh/Library/Application Support/Google/Chrome/")
options.add_argument('--profile-directory=Profile 2')
options.add_argument('--proxy-server={}'.format(random.choice(proxyList)))

options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})



driver = webdriver.Chrome('/Users/phamkethanh/PycharmProjects/sele/drivers/chromedriver', chrome_options=options)

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-N950U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"})


# driver.set_window_size(720, 480)

driver.get('http://whoer.net')

