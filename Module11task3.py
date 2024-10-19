import inspect

def introspection_info(obj):
    return {'type':type(obj), 'attributes': dir(obj), 'methods':obj.__doc__,'module':inspect.getmodule(obj)}


print(inspect.getsourcefile(42))


number_info = introspection_info(42)
print(number_info)