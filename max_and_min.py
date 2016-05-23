list = [
    [200000000, 34, 65],
    [200000005, 32, 65],
    [200000010, 35, 66],
    [200086410, 20, 66],
    [200086415, 40, 66],
]

DAY_LENGTH_IN_SECONDS = 86400

last_day = 0
last_max = None
last_min = None

maxes = []
mins = []

for datapoint in list:
    if datapoint[0] > last_day + DAY_LENGTH_IN_SECONDS:
        if last_max is not None:
            maxes.append(last_max)  # saves last day's max and to the lists
            mins.append(last_min)

        last_day = datapoint[0]
        last_max = datapoint[1]  # reset max and min to new values
        last_min = datapoint[1]
    else:
        if datapoint[1] > last_max:
            last_max = datapoint[1]
        if datapoint[1] < last_min:
            last_min = datapoint[1]


print("maxes:", maxes, "mins:", mins)