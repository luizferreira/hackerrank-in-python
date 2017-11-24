"""
https://www.hackerrank.com/challenges/kangaroo/problem
"""


def will_they_meet(initial_distance, relative_velocity):

    try:
        jumps_necessary = initial_distance / relative_velocity
    except ZeroDivisionError:  # they have the same velocity
        if initial_distance == 0:
            # they started at the same place; in the next jump they will meet
            return True
        else:
            # they didn't started at the same place and have the same velocity
            return False

    if jumps_necessary < 0:
        return False  # they are not getting closer

    if jumps_necessary - int(jumps_necessary) != 0:
        return False  # they won't meet in the same location

    return True

k1_init, k1_velocity, k2_init, k2_velocity = map(int, input().strip().split())

initial_distance = k2_init - k1_init

relative_velocity = k1_velocity - k2_velocity

they_will_meet = True

if will_they_meet(initial_distance, relative_velocity):
    print('YES')
else:
    print('NO')
