
def find_missing(list1, list2):
  if list1==[] or list2==[]:
    return 0
  diff = list(set(list1).symmetric_difference(set(list2)))
  if diff == []:
    return 0
  else:
    return diff

r = find_missing([1,2,3],[1,2,3,4])
print(r)