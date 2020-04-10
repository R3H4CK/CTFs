ciphertext = "llkjmlmpadkkc"
key = "thisisalilkey"

# table
for i in range(26):
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr((ch - ord('A') + i) % 26 + ord('A')), end='')
    print()
