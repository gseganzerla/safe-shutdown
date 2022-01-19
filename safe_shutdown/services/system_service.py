import os

class SystemService:

    @classmethod
    def shutdown():
        os.system('poweroff')