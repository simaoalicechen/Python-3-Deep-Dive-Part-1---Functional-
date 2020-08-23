# run.py

import timing 
# print(f'loading run.py: __name__ = {__name__}') 
# import module1

code = '[x**2 for x in range(1000_000)]' 
result  = timing.timeit(code, 100)
print(result) 