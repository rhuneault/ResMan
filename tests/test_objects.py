import unittest

from app.objs.objects import Application, ResumeBase, HTMLExporter


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

    def test_application_advanced_properties(self):
        """
        """
        a = Application('TD Canada Trust', 'Senior Confabulator', 'Not applied')
        a.set_location()



class TestResume(unittest.TestCase):
    """
    """
    def test_resume_name(self):
        """Test the default format works with no middle name.
        """
        rb = ResumeBase('John', 'Doe')
        self.assertEqual(rb.name(), 'John Doe')

    def test_resume_middle_name(self):
        """Test the default format works with a middle name.
        """
        rb = ResumeBase('John', 'Doe', middle_name='Patrick')
        self.assertEqual(rb.name(), 'John Patrick Doe')

    def test_resume_no_middle_name(self):
        """Test the middle name is correctly omitted when the "omit" format is specified.
        """
        rb = ResumeBase('John', 'Doe', middle_name='Patrick')
        self.assertEqual(rb.name(middle='omit'), 'John Doe')

    def test_resume_middle_initial_name(self):
        """Test that the middle name is correctly abbreviated when a middle initial format is specified.
        """
        rb = ResumeBase('John', 'Doe', middle_name='Patrick')
        self.assertEqual(rb.name(middle='initial'), 'John P. Doe')

    def test_resume_no_middle_name(self):
        """Test that an error is raised with no middle name is provided, but one is requested to be displayed.
        """
        rb = ResumeBase('John', 'Doe')
        with self.assertRaises(ValueError):
            print(rb.name(middle='initial'))

    def test_resume_add_personal_info(self):
        """The that we can add and retrieve contact and location info.
        """


class TestExporter(unittest.TestCase):
    """
    """
    def test_html_export(self):
        """
        """
        r = ResumeBase('John', 'Smith', middle_name='Quentin')
        ex = HTMLExporter()
        print(ex.export(r))



if __name__ == '__main__':
    unittest.main()
