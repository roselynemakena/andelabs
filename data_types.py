
def data_type(value):
  if isinstance(value, str):
    return len(value)
  if value == None:
    return 'no value'
  if isinstance(value, bool):
    return True
  if isinstance(value, int):
    if value<100:
      return 'less than 100'
    elif value==100:
      return 'equal to 100'
    else:
      return 'more than 100'
  if isinstance(value, list):
    if len(value) <= 0:
      return 'no value'
    elif len(value) < 3:
      return None
    else:
      return value[2]
      