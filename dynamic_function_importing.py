"""
e.g.
if we want to check if the function "run_function" exists and can be imported from "models.run_data_prep", we will use the below code with the parameters:

function_name: "run_function"
module_path: "models."
module_name: "run_data_prep"

if the function can be imported, it is called using "function_signature(**args)"
"""


from importlib import import_module

try:
    function_signature = import_modules(<function_name>, <module_path>, <module_name>)
except ImportError as Err:
    raise ImportError("Could not import module <module_name>")
    
function_signature(**args)

def import_modules(operator_name, module_path, module_name):
    function_reference = import_operator(module_path + module_name, operator_name)
    return function_reference

def import_operator(operator_path, operator_name):
    try:
        operator_module = import_module(operator_path)
        function_reference = getattr(operator_module, operator_name)
    except AttributeError as err:
        raise AttributeError(f"Failed to find function {operator_name} in {operator_path} : {err}")
    
    return function_reference
    
