# while and for loops

# x = 0
# while (x < 5):
#     print(x)
#     x = x + 1

# for loop

# for x in range(5, 10):
#     print(x)

# Array

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for d in days:
    # if d == "Friday":
    #     break  # loop break/stop
    if d == "Friday":
        continue  # skip this value
    print(d)
