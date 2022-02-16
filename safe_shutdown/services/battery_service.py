from safe_shutdown.models.battery import Battery
from safe_shutdown.services.log_service import LogService
from safe_shutdown.services.system_service import SystemService

class BatteryService:
    def __init__(self, battery: Battery):
        self.battery = battery
        self.logger = LogService()        
        

    def should_shutdown(self):
        if self.battery.percent <= self.battery.power_off and self.battery.status == False:
            self.logger.write(self.battery)
            SystemService.shutdown() 