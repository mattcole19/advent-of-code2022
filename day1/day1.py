
# Part 1
# with open('input.txt') as file:
#     max_calories = 0
#     curr_calories = 0
#     for line in file:
#         if line == "\n":
#             if curr_calories > max_calories:
#                 max_calories = curr_calories
#             curr_calories = 0
#         else:
#             curr_calories += int(line)
# print(max_calories)

# -----------------------------------
def update_top_3(top3, current):
    top3[0] = current
    top3.sort()

# Part 2
with open('input.txt') as file:
    top_3 = [0, 0, 0]
    curr_calories = 0
    for line in file:
        if line == "\n":
            # Check if it makes it in the top 3!
            if curr_calories > top_3[0]:
                update_top_3(top_3, curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(line)

print(f'Top 3: {top_3}')
print(f'Sum: {sum(top_3)}')




