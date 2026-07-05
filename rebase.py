# This function takes a number represented in base-x and outputs a list showing its representation in base-y. 
def rebase(input_base, digits, output_base):
    tot = 0
    place = 0
    if input_base < 2: 
        raise ValueError("input base must be >= 2")
    elif output_base < 2: 
        raise ValueError("output base must be >= 2")
    else: 
        for digit in digits[-1::-1]: # Converts input_base, digits -> base-10
            if 0 <= digit < input_base: 
                tot += digit*(input_base ** place) 
                place += 1
            else: 
                raise ValueError("all digits must satisfy 0 <= d < input base")
    # need to convert base-10 -> output_base, [digits]
    output_list = []
    while tot > 0: 
        output_list.insert(0, tot % output_base)
        tot = tot // output_base
    return output_list if len(output_list) != 0 else [0]
