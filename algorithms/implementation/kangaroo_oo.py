"""
https://www.hackerrank.com/challenges/kangaroo/problem

Object Oriented solution
"""


class Kangaroo:

    def __init__(self, initial_position, velocity):
        self._initial_position = initial_position
        self._current_position = initial_position
        self._velocity = velocity

    @property
    def current_position(self):
        return self._current_position

    @property
    def velocity(self):
        return self._velocity

    def jump(self):
        self._current_position += self.velocity

    def is_ahead_of(self, other_kangaroo):
        if self.current_position > other_kangaroo.current_position:
            return True
        return False


k1_init, k1_velocity, k2_init, k2_velocity = map(int, input().strip().split())

kangaroo1 = Kangaroo(k1_init, k1_velocity)
kangaroo2 = Kangaroo(k2_init, k2_velocity)

if kangaroo1.is_ahead_of(kangaroo2):
    started_ahead = kangaroo1
    started_behind = kangaroo2
else:
    started_ahead = kangaroo2
    started_behind = kangaroo1

if started_behind.velocity > started_ahead.velocity:
    while(started_behind.current_position < started_ahead.current_position):
        kangaroo1.jump()
        kangaroo2.jump()

if kangaroo1.current_position == kangaroo2.current_position:
    print('YES')
else:
    print('NO')
