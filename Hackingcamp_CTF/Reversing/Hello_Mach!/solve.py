table = "BIKGZq]9fi:goUGkib'EUb>iaoxyw"

for i in range(0xff):
    flag = ""
    for ch in table:
        flag += chr(ord(ch) ^ i)
    print(i, flag)
    if flag[:5] == "HCAMP":
        break
