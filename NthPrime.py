# This exercise intentionally avoid importing modules. 
# Checks if a number is prime (not as efficient as it could be)
def is_prime(numb): 
    if numb > 3: 
        if numb % 2 == 0 or numb % 3 == 0: 
            return False
    return not any(numb % i == 0 for i in range(5, numb//2, 2))

# Takes a number n and returns the nth prime. 
def prime(number):
    if number < 1: 
        raise ValueError("there is no zeroth prime")
    count = 0 
    test = 1
    while count != number: 
        test += 1 
        if is_prime(test):  
            count += 1 
    return test 
