from unittest import TestCase
import logging

from safe_shutdown.services.log_service import LogService


class TestLogService(TestCase):

    def setUp(self) -> None:
        super().setUp()

        self.service = LogService()

    def test_write(self):
        with self.assertLogs(logger='safe_shutdown', level=logging.INFO) as captured:
            self.service.write('test')
            self.assertEqual(len(captured.records), 1)


