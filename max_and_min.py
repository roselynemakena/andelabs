
def find_max_min(numbers):
    if min(numbers) == max(numbers):
      return [len(numbers)]
    else:
      result = [min(numbers),max(numbers)]
      return result
      