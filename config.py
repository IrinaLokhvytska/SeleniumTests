HOST_NAME = 'localhost'
PORT_NUMBER = 8000
driver = "chromedriver"

executable_path = {
    'dev': "C:/{0}".format(driver),
    'prod': "/usr/local/bin/{0}".format(driver)
}
