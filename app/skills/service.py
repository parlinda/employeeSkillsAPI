from ..server import Server
from ..server.mongo import MongoRepository
from .schema import employeeSchema

class Service(object):
  def __init__(self, user_id, repo_client=Server(adapter=MongoRepository)):
    self.repo_client = repo_client
    self.user_id = user_id

    if not user_id:
      raise Exception("user id not provided")

  def find_all_emps(self):
    emps  = self.repo_client.find_all({'user_id': self.user_id})
    return [self.dump(emp) for emp in emps]

  def find_emp(self, repo_id):
    emp = self.repo_client.find({'user_id': self.user_id, 'repo_id': repo_id})
    return self.dump(emp)

  def create_emp_for(self, githubRepo):
    self.repo_client.create(self.prepare_emp(githubRepo))
    return self.dump(githubRepo.data)

  def update_emp_with(self, repo_id, githubRepo):
    records_affected = self.repo_client.update({'user_id': self.user_id, 'repo_id': repo_id}, self.prepare_emp(githubRepo))
    return records_affected > 0

  def delete_emp_for(self, repo_id):
    records_affected = self.repo_client.delete({'user_id': self.user_id, 'repo_id': repo_id})
    return records_affected > 0

  def dump(self, data):
    return employeeSchema(exclude=['_id']).dump(data).data

  def prepare_emp(self, githubRepo):
    data = githubRepo.data
    data['user_id'] = self.user_id
    return data