"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
"""

games_qty = int(input().strip())

scores = [int(score) for score in input().strip().split()]

all_time_best_score_counter = 0
all_time_worst_score_counter = 0
best_score = scores[0]  # since n >= 1 we don't need to test for empty list
worst_score = scores[0]  # since n >= 1 we don't need to test for empty list

for score in scores:
    if score > best_score:
        best_score = score
        all_time_best_score_counter += 1
    elif score < worst_score:
        worst_score = score
        all_time_worst_score_counter += 1

print(
    all_time_best_score_counter,
    all_time_worst_score_counter
)
