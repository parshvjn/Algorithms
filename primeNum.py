
# def is_prime(n):
#     if n < 2: # O(1)
#         return 'not prime' # O(1)
#     for i in range(2, n): #, int(n**0.5)+1):
#         print(i)
#         if n % i == 0:
#             print('divisble by', i)
#             return 'not prime'
    
#     return 'prime' # O(1)

# print(is_prime(2**521-1))

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        print(i)
        if n % i == 0:
            return False
    return True

print(is_prime(2**521-1))