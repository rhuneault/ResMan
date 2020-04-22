import unittest

from app.objs.objects import Application


class TestApplication(unittest.TestCase):
    """
    """

    def test_application_properties(self):
        """
        """
        a = Application('TD Canada Trust', 'Senior Confabulator', 'Not applied')
        assert a.company == 'TD Canada Trust'
        assert a.position == 'Senior Confabulator'
        assert a.status == 'Not applied'




if __name__ == '__main__':
    unittest.main()
