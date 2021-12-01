with open('data.txt') as f:
    lines = f.readlines()
data = [int(number.replace("\n", "")) for number in lines]

sums_of_measurements = [data[i]+data[i+1]+data[i+2] for i in range(len(data)-2)]

times_depth_increases = 0
for i in range(len(sums_of_measurements)-1):
    if sums_of_measurements[i] < sums_of_measurements[i+1]:
        times_depth_increases+=1

print(times_depth_increases)