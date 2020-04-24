import unittest

from app.objs.objects import Application, ResumeBase


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
    def test_resume_name_raise_error(self):
        """
        """
        rb = ResumeBase()
        with self.assertRaises(ValueError):
            print(rb.name())

    def test_resume_name(self):
        """
        """
        rb = ResumeBase()
        rb.add_name('John', 'Doe')
        self.assertEqual(rb.name(), 'John Doe')

    def test_resume_middle_name(self):
        """
        """
        rb = ResumeBase()
        rb.add_name('John', 'Doe', middle='Patrick')
        self.assertEqual(rb.name(), 'John Patrick Doe')

    def test_resume_no_middle_name(self):
        """
        """
        rb = ResumeBase()
        rb.add_name('John', 'Doe', middle='Patrick')
        self.assertEqual(rb.name(middle='omit'), 'John Doe')

    def test_resume_middle_initial_name(self):
        """
        """
        rb = ResumeBase()
        rb.add_name('John', 'Doe', middle='Patrick')
        self.assertEqual(rb.name(middle='initial'), 'John P. Doe')

    def test_resume_no_middle_name(self):
        """
        """
        rb = ResumeBase()
        rb.add_name('John', 'Doe')
        with self.assertRaises(ValueError):
            print(rb.name(middle='initial'))


if __name__ == '__main__':
    unittest.main()
