import sched
import psutil

from safe_shutdown.models.battery import Battery
from safe_shutdown.services.battery_service import BatteryService

scheduler = sched.scheduler()

def run():
    device = psutil.sensors_battery()
    battery = Battery(device.percent, 90, False)
    service = BatteryService(battery)

    service.should_shutdown()
    scheduler.enter(delay=300, priority=1, action=run)

run()

scheduler.run(blocking=True)