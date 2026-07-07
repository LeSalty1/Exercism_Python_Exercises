# This is still a work in-progress 
# The intent is to be able to encode/decode data already optimal for run-length encoding. 
def decode(string):
    if string = "": 
        return ""
    

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
        
        
