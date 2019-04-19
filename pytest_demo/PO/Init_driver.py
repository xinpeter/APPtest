from appium import webdriver

def init_driver():
    # 设备信息
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'CQ30013F6H'
    desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['app'] = 'F:// debug.apk'
    desired_caps['appActivity'] = '.Settings'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver