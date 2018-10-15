class Config:
    def __init__(self):
        self.host_name = 'localhost'
        self.port_number = 8000
        self.driver = 'chromedriver'
        self.version = 'production'

    def get_executable_path(self):
        if self.version == 'production':
            return '/usr/local/bin/{0}'.format(self.driver)
        return 'C:/{0}'.format(self.driver)
