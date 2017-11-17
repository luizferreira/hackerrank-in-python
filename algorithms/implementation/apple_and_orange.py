"""
https://www.hackerrank.com/challenges/apple-and-orange/problem
"""

house_start, house_end = map(int, input().strip().split(' '))
apple_tree, orange_tree = map(int, input().strip().split(' '))

apples_qty, oranges_qty = map(int, input().strip().split(' '))

apples = map(int, input().strip().split(' '))
oranges = map(int, input().strip().split(' '))


def has_fallen_on_house(tree_position, relative_position):
    abs_position = tree_position + relative_position
    if abs_position >= house_start and abs_position <= house_end:
        return(True)
    return(False)


def how_many_fell_on_house(tree, fruit_relative_positions):
    count = 0
    for fruit_position in fruit_relative_positions:
        if has_fallen_on_house(tree, fruit_position):
            count += 1
    return(count)

print(how_many_fell_on_house(apple_tree, apples))
print(how_many_fell_on_house(orange_tree, oranges))
