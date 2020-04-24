import unittest

from app.objs.objects import Application


# coverage run --source=app -m nose2
# coverage report

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


class TestResume(unittest.TestCase):
    """
    """
    def test_resume_properties(self):
        """
        """



if __name__ == '__main__':
    unittest.main()
