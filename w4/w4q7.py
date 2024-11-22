#w4q7
def create_dict_from_lists(keys, values):
    result_dict = {key: [] for key in keys}
    
    for i, value in enumerate(values):
        key = keys[i % len(keys)]  
        result_dict[key].append(value)
    
    return result_dict

keys_list = ['a', 'b', 'c']
values_list = [1, 2, 2, 3, 4, 4, 4]

result = create_dict_from_lists(keys_list, values_list)

print(result)