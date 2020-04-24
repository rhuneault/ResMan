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
    def __init__(self):
        """
        """
        self._first = None
        self._middle = None
        self._last = None

    def add_name(self, first, last, middle=None):
        """Add the job applicant's name to the resume.

        :param first: The first name of the job applicant
        :param last: The last name of the job applicant
        :return: None
        """
        self._first = first
        self._last = last
        self._middle = middle

    def name(self, middle=None):
        """Return the name in the requested format.

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


