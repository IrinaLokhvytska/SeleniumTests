class Config:
    def __init__(self):
        self.host_name = 'localhost'
        self.port_number = 8000
        self.driver = 'chromedriver'

    def get_executable_path(self, version):
        if version == 'prod':
            return '/usr/local/bin/{0}'.format(self.driver)
        return 'C:/{0}'.format(self.driver)
