

while True:  # driver code for capacity user input
    try:
        user_capacity = int(input("Please input desired capacity parameter :  "))
    except ValueError:
        print("invalid input. Please enter a positive integer")
        continue
    if type(user_capacity) != int:
        print("invalid input. Please enter a positive integer")
        continue
    break

weights = []
values = []
with open('data.txt', 'r') as infile:
    i = 0
    # iterate through each line
    for line in infile:
        # populate list by values separated by spaces, strip newline characters
        item_pair = line.strip().split(" ")
        weights.append(int(item_pair[0]))
        values.append(int(item_pair[1]))

def knappy(capacity, weight, value, n):
    # fill table with 0s
    table =[ [0 for j in range(capacity + 1)] for k in range(n + 1)]

    for item in range(n+1):
        for cap in range(capacity+1):

            if item == 0 or cap == 0:
                table[item][cap] = 0

            elif weight[item-1] <= cap:
                table[item][cap] = max( value[item-1] + table[item - 1][cap - weight[item - 1]], table[item - 1][cap])

            else:
                table[item][cap] = table[item - 1][cap]

    return table[n][capacity]


n = len(weights)
print("The maximum value that can be fit in the knapsack is:", knappy(user_capacity, weights, values, n))

