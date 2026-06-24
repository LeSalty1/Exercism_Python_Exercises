# This program takes two lists and checks if one is a sub/superlist of the other.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4
def sublist(list_one, list_two):
  s_list_one = str(list_one).strip("[]") + ","
  s_list_two = str(list_two).strip("[]") + ","
  if s_list_one == s_list_two: 
    return EQUAL 
  elif s_list_one in s_list_two: 
    return SUBLIST
  elif s_list_two in s_list_one: 
    return SUPERLIST 
  return UNEQUAL
