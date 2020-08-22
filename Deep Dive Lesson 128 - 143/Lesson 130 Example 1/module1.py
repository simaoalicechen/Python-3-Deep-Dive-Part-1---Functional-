
import sys 
print('===============================')
print('Running main.py - module name: {0}'.format(__name__))
import main
# print(module1)
# module1.pprint_dict('main.globals', globals)

# print(sys.path)
# print(sys.modules['module1'])

print('importing module1 again...')
del globals()['module1']

module.pprint('main.globals', globals)
import module1

print('================================')