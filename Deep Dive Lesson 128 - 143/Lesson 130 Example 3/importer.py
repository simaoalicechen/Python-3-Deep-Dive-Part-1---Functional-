importer.py

import os.path
import types 
import sys
def import_(module_name, module_file, module_path): 
    if module_name in sys.modules: 
        return sys.modules[module_name]
    
    module_ref_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_path, module_file)

    # read source code from file 

    with open(module_rel_file_path, 'r') as code_file: 
        source_code = code_file.read()

    # create a module object 
    mod = types.MOduleType(module_name)
    mod.__file__ = module_abs_file_path

    # set a ref in sys.modules 
    sys.modules[module_name] = mod 

    # compile source code 

    code = compile(source_code, filename = module_abs_file_path, mode = 'exec') 

    #exectute compiled source code 
    exec(code)


    return sys.modules[module_name]