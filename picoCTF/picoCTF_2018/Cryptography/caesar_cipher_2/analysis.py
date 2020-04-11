text = "d]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q"

print(len(text))

cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
for ch in text:
    if ch.islower():
        cnt1 += 1
    elif ch.isupper():
        cnt2 += 1
    elif ch.isdigit():
        cnt3 += 1
    else:
        cnt4 += 1
print(cnt1, cnt2, cnt3, cnt4, sep='\n')

for ch in text:
    if not ch.isalpha() and not ch.isdigit() and ch != ' ':
        text = text.replace(ch, '')
for word in text.split(' '):
    if word in text:
        print(word)
