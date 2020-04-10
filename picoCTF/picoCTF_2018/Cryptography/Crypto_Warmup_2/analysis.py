text = "cvpbPGS{guvf_vf_pelcgb!}"

print(len(text))
for i in range(len(text)):
    for j in range(len(text)):
        if text[i:j] in text[i+1:]:
            print(text[i:j])
