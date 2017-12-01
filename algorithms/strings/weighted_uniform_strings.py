"""
https://www.hackerrank.com/challenges/weighted-uniform-string/problem
"""

string = input().strip()

queries_qty = int(input().strip())


def weights_list(string):
    weights = set()

    while(len(string) > 0):

        char = string[0]
        accumulated_weight = 0
        i = 0
        while(i < len(string) and string[i] == char):
            accumulated_weight += char_weight(char)
            weights.add(accumulated_weight)
            i += 1
        string = string[i:]

    return weights


def char_weight(char):
    return ord(char) - ord('a') + 1


weights = weights_list(string)

for i in range(queries_qty):
    query = int(input().strip())
    print('Yes' if query in weights else 'No')
