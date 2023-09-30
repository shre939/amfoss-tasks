n = int(input())  # Number of cities
times = list(map(int, input().split()))  # List of travel times to each town

min_time = min(times)  # Find the minimum travel time

if times.count(min_time) > 1:
    print("Still Aetheria")
else:
    min_index = times.index(min_time) + 1  # Find the index of the minimum time (add 1 for 1-based indexing)
    print(min_index)

