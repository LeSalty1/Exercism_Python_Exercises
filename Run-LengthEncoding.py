# The intent is to be able to encode/decode data already optimal for run-length encoding. 
import string as st
def decode(string):
    if string == "": 
        return "" 
    stored_numbs = ""
    ret_string = ""
    for char in string: 
        if char.isnumeric(): 
            stored_numbs += char 
        elif char.isalpha() or char in st.whitespace: 
            if len(stored_numbs) == 0: 
                ret_string += char 
            else: 
                ret_string += char * int(stored_numbs)
                stored_numbs = ""
    return ret_string
    

def encode(string):
    if string == "": 
        return ""
    code = ""
    count = 1 
    previous = string[0]
    
    for i in range(1, len(string)): 
        if previous != string[i]: 
            if count == 1: 
                code += previous
            else: 
                code += str(count) + previous
            previous = string[i]
            count = 1
        elif previous == string[i]:
            count += 1 
            previous = string[i]
            
    if count == 1: 
        code += previous
    else: 
        code += str(count) + previous
    return code
        
        

        
