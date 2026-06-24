def append(list1, list2):
    return list1 + list2

def concat(lists):
    combined_list = []
    for s_list in lists: 
        combined_list += s_list
    return combined_list


def filter(function, list):
    filtered_list = []
    for item in list: 
        if function(item): 
            filtered_list += [item]
    return filtered_list

def length(list):
    i = 0 
    for item in list: 
        i += 1 
    return i


def map(function, list):
    mapping = []
    for item in list: 
        mapping += [function(item)]
    return mapping

def reverse(list):
    rev_list = []
    for item in list[-1::-1]: 
        rev_list += [item]
    return rev_list
