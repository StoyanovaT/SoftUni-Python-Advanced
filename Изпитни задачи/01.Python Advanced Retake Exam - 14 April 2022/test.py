# import sys
# from io import StringIO
#
# test_input1 = '''- R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left
# '''
# test_input2 = '''R - - - - -
# - - C - - -
# - - - - M -
# - - W - - -
# - E - W - R
# - - - - - -
# up, right, down, right, right, right
# '''
# test_input3 = '''R - - - - -
# - - C - - -
# - - - - M -
# C - M - R M
# - E - W - -
# - - - - - -
# right, right, up, left, left, left, left, left
# '''
#
# # sys.stdin = StringIO(test_input1)
# # sys.stdin = StringIO(test_input2)
# # sys.stdin = StringIO(test_input3)
def words_sorting(*args):
    words_dict = {}
    for arg in args:
        words_dict[arg] = sum(ord(x) for x in arg)
    if sum(words_dict.values()) % 2 != 0:
        sorted_words = [f"{key} - {value}" for key, value in sorted(words_dict.items(), key=lambda x: -x[1])]
    else:
        sorted_words = [f"{key} - {value}" for key, value in sorted(words_dict.items(), key=lambda x: x[0])]
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
