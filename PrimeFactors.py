# Tests if a number is prime (not optimal but works in scope of exercise)
def is_prime(numb): 
    return all(numb % i == 0 for i in range(1, numb))

# Finds all prime factors of a number (includes duplicates e.g., factors(8) returns [2,2,2])
def factors(value):
    facts = []
    if value == 1: 
        return []
    if is_prime(value): 
        return [value]
    test_fact = 2
    while value != 1: 
        if value % test_fact == 0: 
            facts.append(test_fact)
            value = int(value/test_fact)
        else: 
            test_fact += 1
    return facts
