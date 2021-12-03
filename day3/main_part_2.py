with open('data.txt') as f:
    bits = [bit.strip("\n") for bit in f.readlines()]


def calc_row(bits, i, oxy = True):
    one_counter = 0
    zero_counter = 0
    for j in range(len(bits)):
        if bits[j][i] == "0":
            zero_counter+=1
        elif bits[j][i] == "1":
            one_counter+=1
    if oxy:
        if zero_counter > one_counter:
            oxygen_filtered = filter(lambda bit: bit[i] == "0", bits)
        elif zero_counter <= one_counter:
            oxygen_filtered = filter(lambda bit: bit[i] == "1", bits)
    else:
        if zero_counter > one_counter:
            oxygen_filtered = filter(lambda bit: bit[i] == "1", bits)
        elif zero_counter <= one_counter:
            oxygen_filtered = filter(lambda bit: bit[i] == "0", bits)
    one_counter = 0
    zero_counter = 0
    return list(oxygen_filtered)#, list(co_filtered)


for i in range(len(bits[0])):
    bits = calc_row(bits, i, True)
    if len(bits) == 1:
        oxygen = int(bits[0],2)
        print(f"oxygen: {oxygen}")
        break

with open('data.txt') as f:
    bits = [bit.strip("\n") for bit in f.readlines()]


for i in range(len(bits[0])):
    bits = calc_row(bits, i, False)
    if len(bits) == 1:
        co = int(bits[0],2)
        print(f"co: {co}")
        break

multiplication = oxygen * co
print(multiplication)