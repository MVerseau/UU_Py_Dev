import inspect

def introspection_info(obj):
    return {'type': obj.__class__.__name__, 'attributes': dir(obj), 'methods':inspect.getmembers(obj, predicate=inspect.ismethod), 'module':introspection_info.__module__}

number_info = introspection_info(42)
print(number_info)