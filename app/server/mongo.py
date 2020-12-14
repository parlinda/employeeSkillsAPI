import os
from pymongo import MongoClient

COLLECTION_NAME = 'skills'

class MongoRepository(object):
  def __init__(self):
    mongo_url = os.environ.get('MONGO_URL')
    self.db = MongoClient(mongo_url).skills

  def find_all(self, selector):
    return self.db.skills.find(selector)
 
  def find(self, selector):
    return self.db.skills.find_one(selector)
 
  def create(self, emp):
    return self.db.skills.insert_one(emp)

  def update(self, selector, emp):
    return self.db.skills.replace_one(selector, emp).modified_count
 
  def delete(self, selector):
    return self.db.skills.delete_one(selector).deleted_count