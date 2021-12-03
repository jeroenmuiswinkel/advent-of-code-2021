with open('data.txt') as f:
    bits = [bit.strip("\n") for bit in f.readlines()]

epsilon_bit = ""
gamma_bit = ""

one_counter = 0
zero_counter = 0
for i in range(len(bits[0])):
    for j in range(len(bits)):
        if bits[j][i] == "0":
            zero_counter+=1
        elif bits[j][i] == "1":
            one_counter+=1
    if zero_counter > one_counter:
        gamma_bit = gamma_bit + "0"
        epsilon_bit = epsilon_bit + "1"
    else:
        gamma_bit = gamma_bit + "1"
        epsilon_bit = epsilon_bit + "0"
    one_counter = 0
    zero_counter = 0


gamma = int(gamma_bit, 2)
epsilon = int(epsilon_bit,2)
multiplication = gamma * epsilon

print(multiplication)

