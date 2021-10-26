#!/usr/bin/python3
'''This module is defining class BaseModel'''
import uuid
from datetime import datetime


class BaseModel():
    '''Base model for future classes'''

    def __init__(self):
        '''init method of BaseModel'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        '''string representation of the BaseModel'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Updates update_at attribute with current date/time'''
        self.update_at = datetime.now()

    def to_dict(self):
        '''return dictionary containing key:value from __dict__'''
        newDic = self.__dict__.copy()
        newDic['__class__'] = self.__class__.__name__
        newDic['created_at'] = self.created_at.isoformat()
        newDic['updated_at'] = self.updated_at.isoformat()

        return newDic
