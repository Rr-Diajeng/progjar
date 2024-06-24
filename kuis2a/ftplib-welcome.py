from ftplib import FTP
from io import StringIO
import unittest
from unittest.mock import patch, MagicMock
import sys


def get_ftp_welcome_message(host, username, password):
    # Create an FTP object and connect to the FTP server
    ftp = FTP(host)

    # Log in to the server with the provided username and password
    ftp.login(username, password)

    # Retrieve and return the welcome message from the FTP server
    welcome_message = ftp.getwelcome()
    
    return welcome_message


class TestFTPFunctions(unittest.TestCase):

    @patch('__main__.FTP')  # Mock the FTP class in your module
    def test_get_ftp_welcome_message(self, MockFTP):
        # Create a mock FTP instance
        mock_ftp_instance = MagicMock()
        MockFTP.return_value = mock_ftp_instance

        # Define the return value for the getwelcome method
        expected_message = "220 Welcome to the FTP server"
        mock_ftp_instance.getwelcome.return_value = expected_message

        # Call the function with test parameters
        host = 'localhost'
        username = 'hudan'
        password = '123'
        welcome_message = get_ftp_welcome_message(host, username, password)

        # Assertions to verify the behavior
        mock_ftp_instance.login.assert_called_once_with(username, password)
        print(f"login called with {mock_ftp_instance.login.call_args}") 

        mock_ftp_instance.getwelcome.assert_called_once()
        print(f"getwelcome called {mock_ftp_instance.getwelcome.call_args}")
        assert_equal(welcome_message, expected_message)


# A 'null' stream that discards anything written to it
class NullWriter(StringIO):
    def write(self, txt):
        pass

def assert_equal(parameter1, parameter2):
    if parameter1 == parameter2:
        print(f'test attribute passed: {parameter1} is equal to {parameter2}')
    else:
        print(f'test attribute failed: {parameter1} is not equal to {parameter2}')

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == 'run':
        # Example usage
        host = 'localhost'
        username = 'hudan'
        password = '123'
        welcome_message = get_ftp_welcome_message(host, username, password)
        print("Welcome message from the server:", welcome_message)

    else:
        runner = unittest.TextTestRunner(stream=NullWriter())
        unittest.main(testRunner=runner, exit=False)

