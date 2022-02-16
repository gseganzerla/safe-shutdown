from unittest import TestCase, mock
from safe_shutdown.services.system_service import SystemService


class TestSystemService(TestCase):

    @mock.patch('safe_shutdown.services.system_service.os')
    def test_shutdown(self, mock_os):
        SystemService.shutdown()

        mock_os.system.assert_called_once_with('poweroff')