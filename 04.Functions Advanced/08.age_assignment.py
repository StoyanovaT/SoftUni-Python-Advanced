def age_assignment(*args, **kwargs):
    info = {}
    for key, value in kwargs.items():
        for name in args:
            if key == name[0]:
                info[name] = value
    sorted_info = [f'{key} is {value} years old.' for key, value in sorted(info.items(), key=lambda x: x[0])]
    return '\n'.join(sorted_info)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))