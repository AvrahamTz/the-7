import sqlite3
import csv

class Solider:
    def __init__(self,id,first_name,last_name,gender,city,how_far=int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.city = city
        self.how_far = how_far
        self.status = str
        self.list_of_soliders= []
    def add_solider(self):
        self.list_of_soliders.append(self.to_dict(self))

    def to_dict(self):
        return {
    "id": self.id, 
    "first_name":self.first_name,
    "last_name":self.last_name,
    "city":self.city,
    'kilometers': self.how_far,
    "room": self.status 
    }






                    
        