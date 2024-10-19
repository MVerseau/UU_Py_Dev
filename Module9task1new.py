def apply_all_func(int_list: list[int | float], *functions: callable):
    my_dict = {}
    for i in functions:
        my_dict[i.__name__] = i(int_list)

    return my_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
