class Server(object):
  def __init__(self, adapter=None):
    self.client = adapter()

  def find_all(self, selector):
    return self.client.find_all(selector)
 
  def find(self, selector):
    return self.client.find(selector)
 
  def create(self, emp):
    return self.client.create(emp)
  
  def update(self, selector, emp):
    return self.client.update(selector, emp)
  
  def delete(self, selector):
    return self.client.delete(selector)