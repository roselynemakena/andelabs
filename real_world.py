#this is a problem demonstrating a simple task creation app that creates a project with a deadline

class Project(object):
  """docstring for Project"""
  def __init__(self, project_name, project_description, project_deadline):
    self.project_name = project_name
    self.project_deadline = project_deadline
    self.project_description = project_description


#Inheritance of Project into User module
class User(Project):
  """docstring for User"""
  def __init__(self, first_name, last_name):
    Project.__init__(project_name, project_description, project_deadline)
    self.first_name = first_name
    self.last_name = last_name


p = Project("ProjectOne", "A project about contructing a building", "10/03/2017")
print(p)
    
