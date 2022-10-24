def start_spring(**kwargs):
    result = ''
    result_dict = {}
    for key, value in kwargs.items():
        if value not in result_dict.keys():
            result_dict[value] = []
        result_dict[value].append(key)
    for key, value in result_dict.items():
        result_dict[key] = sorted(value)

    sorted_result = sorted(result_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    for tuple_ in sorted_result:
        new_key = tuple_[0]
        new_values = tuple_[1]
        sorted_new_values = sorted(new_values)
        result += f"{new_key}:\n"
        for val in sorted_new_values:
            result += f"-{val}\n"

    return result.strip()


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))



