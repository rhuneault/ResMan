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
