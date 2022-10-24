from collections import deque

vowels = deque(input().split())
consonants = input().split()
flowers_dict = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}
found = False
found_word = ''

while vowels and consonants:
    v_c = [vowels.popleft(), consonants.pop()]

    for key, value in flowers_dict.items():
        for char in v_c:
            if char in flowers_dict[key]:
                flowers_dict[key] = flowers_dict[key].replace(char, '')
        if flowers_dict[key] == '':
            found = True
            found_word = key
            break
    if found:
        break

if found:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print("Vowels left: ", end='')
    print(' '.join(vowels))
if consonants:
    print("Consonants left: ", end='')
    print(' '.join(consonants))
