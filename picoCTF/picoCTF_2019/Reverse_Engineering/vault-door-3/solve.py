flag = ['\000' for i in range(32)]
buffer = "jU5t_a_sna_3lpm13gc49_u_4_m0rf41"

for i in range(8):
    flag[i] = buffer[i]

for i in range(i + 1, 16):
    flag[i] = buffer[23 - i]

for i in range(i + 1, 32, 2):
    flag[i] = buffer[46 - i]

for i in range(17, 32, 2):
    flag[i] = buffer[i]
    
print(''.join(flag))
