def words_sorting(*args):
    words_dict = {}
    for word in args:
        curr_sum = 0
        for let in word:
            curr_sum += ord(let)
        words_dict[word] = curr_sum

    if sum(words_dict.values()) % 2 != 0:
        sorted_words = [f'{key} - {value}' for key, value in sorted(words_dict.items(), key=lambda x: -x[1])]
    else:
        sorted_words = [f'{key} - {value}' for key, value in sorted(words_dict.items(), key=lambda x: x[0])]

    return '\n'.join(sorted_words)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
