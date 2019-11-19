from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument("--disable-extensions")
option.add_argument("--disable-infobars")
option.add_argument("--disable-logging")
option.add_argument("--disable-notifications")
option.add_argument("--disable-default-apps")
option.add_argument('--user-data-dir=/Users/phamkethanh/Library/Application Support/Google/Chrome/')
option.add_argument('--profile-directory=Profile 2')


driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=option)

driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-N950U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"})


# driver.set_window_size(720, 480)

driver.get('http://whoer.net')