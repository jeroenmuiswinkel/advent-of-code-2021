with open('test_data.txt') as f:
    lines = f.readlines()
data = [int(number.replace("\n", "")) for number in lines]

print(data)