with open('data.txt') as f:
    data = [int(number) for number in f.readlines()]

times_depth_increases = 0
for i in range(len(data)-1):
    if data[i] < data[i+1]:
        times_depth_increases+=1

print(times_depth_increases)