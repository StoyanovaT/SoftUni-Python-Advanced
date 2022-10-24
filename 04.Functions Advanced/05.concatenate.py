def concatenate(*args, **kwargs):
    result = ''
    for txt in args:
        result += txt

    for key, value in kwargs.items():
        result = result.replace(key, value)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))