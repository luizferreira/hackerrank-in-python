"""
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
"""

HACKER_RANK = 'hackerrank'

queries_qty = int(input().strip())


def contains_hackerrank(query):
    for i in range(len(HACKER_RANK)):
        char = HACKER_RANK[i]
        char_index = query.find(char)
        if char_index == -1:
            return False
        query = query[char_index+1:]
    return True


for i in range(queries_qty):
    query = input().strip()
    if contains_hackerrank(query):
        print('YES')
    else:
        print('NO')
