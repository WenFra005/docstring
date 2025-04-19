import inspect

def extract_docstrings(module):
    module_counter = 1
    docstrings = [f"{module_counter}.   {module.__name__}\n"]
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            class_counter = 1
            docstrings.append(f"{module_counter}.{class_counter}    {name}\n")
            for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                method_counter = 1
                docstring = inspect.getdoc(method)
                if docstring:
                    docstrings.append(f"{module_counter}.{class_counter}.{method_counter}   "
                                      f"{method_name}\n{docstring}\n")
                    method_counter += 1
            class_counter +=1
        elif inspect.isfunction(obj):
            function_counter = 1
            docstring = inspect.getdoc(obj)
            if docstring:
                docstrings.append(f"{module_counter}.{function_counter}     {name}\n{docstring}\n")
                function_counter += 1
    return "\n".join(docstrings)
