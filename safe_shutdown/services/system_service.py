import os

class SystemService:

    @staticmethod
    def shutdown():
        os.system('poweroff')