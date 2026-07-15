# Converts from Arabic numeral representation into Roman numeral representation.
def roman(number): 
    numerals = {1000 : "M", 
     900 : "CM", 
     500 : "D", 
     400 : "CD", 
     100 : "C", 
     90 : "XC", 
     50 : "L", 
     40 : "XL", 
     10 : "X", 
     9 : "IX", 
     5 : "V", 
     4 : "IV", 
     1 : "I"}
    output = ""
    for mod_rep, rome_num in numerals.items(): 
        while number >= mod_rep: 
            output += rome_num
            number -= mod_rep
    return output
