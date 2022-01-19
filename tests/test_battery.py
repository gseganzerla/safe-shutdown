from unittest import TestCase

from safe_shutdown.models.battery import Battery


class TestBattery(TestCase):
    def setUp(self) -> None:
        super().setUp()


        self.battery = Battery(100, 0, False)

    def test_battery_representation(self):
        self.assertEqual(
            str(self.battery),
            'Battery(percent=100, power_off=0, status=False)'
        )
