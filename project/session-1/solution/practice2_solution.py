start = [9.35, 9.44, 9.09, 7.55]

avg_score = 0
sum_score = 0

for i in range(0, len(start)):
    sum_score += start[i]

avg_score = sum_score / len(start)
print(avg_score)
