class VaultDoor7:
    def passwordToIntArray(self, password):
        x = [0 for i in range(8)]
        hexBytes = bytearray(map(ord, password))
        for i in range(8):
            x[i] = hexBytes[i*4] << 24 \
                | hexBytes[i*4+1] << 16 \
                | hexBytes[i*4+2] << 8 \
                | hexBytes[i*4+3]
        return x

    def checkPassword(self, password):
        if len(password) != 32:
            return False
        x = self.passwordToIntArray(password)
        print(x)
        return x[0] == 1096770097 \
            and x[1] == 1952395366 \
            and x[2] == 1600270708 \
            and x[3] == 1601398833 \
            and x[4] == 1716808014 \
            and x[5] == 1734304823 \
            and x[6] == 962880562 \
            and x[7] == 895706419


vaultDoor = VaultDoor7()
userInput = input("Enter vault password: ")
if vaultDoor.checkPassword(userInput):
    print("Access granted.")
else:
    print("Access denied!")
