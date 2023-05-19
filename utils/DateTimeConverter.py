#!/bin/env python
# -*- coding: utf-8 -*-


"""
RDB - DateTimeConverter
"""

import datetime
import time

class DateTimeConverter():
    """
    Třída DateTimeConverter
    """

    @staticmethod
    def timestamp_to_datetime(timestamp):
        return datetime.datetime.fromtimestamp(timestamp)
    
    @staticmethod
    def datetime_to_timestamp(datetime_obj):
        return int(datetime_obj.timestamp())

    @staticmethod
    def date_to_timestamp(day, month, year):
        date_obj = datetime.datetime(year, month, day)
        return int(date_obj.timestamp())

    @staticmethod
    def timestamp_now():
        current_timestamp = int(time.time())
        return current_timestamp
