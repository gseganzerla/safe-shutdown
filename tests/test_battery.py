from unittest import TestCase, mock

from safe_shutdown.models.battery import Battery
from safe_shutdown.services.battery_service import BatteryService, LogService, SystemService

class TestBattery(TestCase):
    def setUp(self) -> None:
        super().setUp()


        self.battery = Battery(100, 0, False)
        self.service = BatteryService(self.battery)

    def test_battery_representation(self):
        self.assertEqual(
            str(self.battery),
            'Battery(percent=100, power_off=0, status=False)'
        )

    @mock.patch.object(SystemService, 'shutdown')
    @mock.patch.object(LogService, 'write')
    def test_should_shutdown_with_low_battery(self, mock_write, mock_shutdown):

        battery = Battery(5, 10, False)
        service = BatteryService(battery)
        service.should_shutdown()

        mock_write.assert_called_once_with(battery)
        mock_shutdown.assert_called_once()

    @mock.patch.object(SystemService, 'shutdown')
    @mock.patch.object(LogService, 'write')
    def test_should_shutdown_with_charged_battery(self, mock_write, mock_shutdown):

        battery = Battery(100, 10, False)
        service = BatteryService(battery)
        service.should_shutdown()

        mock_write.assert_not_called()
        mock_shutdown.assert_not_called()