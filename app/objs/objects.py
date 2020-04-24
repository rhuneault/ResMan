# -*- coding: utf-8 -*-
"""
This module contains key application objects for the Resume Manager application.
"""


class Application(object):
    """A job application.
    """
    def __init__(self, company_name, position_title, status):
        """Initialize a new Application object.
        """
        self._company = company_name
        self._position = position_title
        self._status = status

    def set_location(self):
        """
        """

    @property
    def company(self):
        """The name of the company which is offering the job.
        """
        return self._company

    @property
    def position(self):
        """The position which is being offered within the company.
        """
        return self._position

    @property
    def status(self):
        """The status of the job application.
        """
        return self._status


class ResumeBase(object):
    """A job resume.
    """
    def __init__(self, first_name, last_name, middle_name=None):
        """
        :param first_name: The first name of the job applicant
        :param last_name: The last name of the job applicant
        :param middle_name: (Optional) The middle name of the job applicant
        """
        self._first = first_name
        self._middle = middle_name
        self._last = last_name

    def name(self, middle=None):
        """Return the name in the requested format.

        :param middle: How to format the middle name
        :return: The first and last name of the job applicant
        """
        if self._first is None or self._last is None:
            raise ValueError('First and last name are required.')

        if middle:
            if middle.lower() == 'omit':
                return self._first.title() + ' ' + self._last.title()
            elif middle.lower() == 'initial':
                if self._middle is None:
                    raise ValueError('Middle initial format requested, but no middle name provided.')
                return self._first.title() + ' ' + self._middle[0].upper() + '. ' + self._last.title()
            # else:
            #     raise
        else:
            if self._middle:
                return self._first.title() + ' ' + self._middle.title() + ' ' + self._last.title()
            else:
                return self._first.title() + ' ' + self._last.title()


class BaseExporter(object):
    """
    """
    def export(self, resume):
        """
        """
        raise NotImplementedError('"export" must be implemented in a sub class.')


class HTMLExporter(BaseExporter):
    """
    """
    def export(self, resume):
        """
        """
        output_html = f"""<html>
	<head>
		<style>
div.ApplicantName {{
	font-family: verdana;
	font-size: 300%;
}}			
		</style>
	</head>
	<body>
		<div class='ApplicantName'>{resume.name()}</div>
		<hr />
	</body>
</html>"""
        return output_html
