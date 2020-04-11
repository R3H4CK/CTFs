flag = ""
text = "Yif wonhr axqkp vqu godbc qefx yif tmzj lqs. N hmp'y aftnfef yinc nc cohi mp fmcj bxqatfd np Bnhq. Ny'c mtdqcy mc nv N cqtefl m bxqatfd mtxfmlj! Qrmj, vnpf. Ifxf'c yif vtms: bnhqHYV{coacynyoynqp_hnbifxc_mxf_yqq_fmcj_lpsmqkdejf}"
table = "mahlfvsingrtdpqbwxcyoekujzMAHLFVSINGRTDPQBWXCYOEKUJZ"

for ch in text:
    for i in range(len(table)):
        if ch == table[i]:
            if table[i].islower():
                flag += chr(97 + i)
            elif table[i].isupper():
                flag += chr(39 + i)
    if not ch.isalpha():
        flag += ch
print(flag)
