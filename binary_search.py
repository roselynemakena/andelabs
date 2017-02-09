class BinarySearch(list):
  def __init__(self,a,b):
    self.length_list = a
    self.step = b

    
  def search(self, value):
      for i in self.values:
        if i == value:
          print "found"