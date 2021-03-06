# blaise's cipher
> My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with nc 2018shell.picoctf.com 46966.

## Summary
* vigenere cipher
* classical cipher

## Analysis
``` python
text = """
Yse lncsz bplr-izcarpnzjo dkxnroueius zf g uzlefwpnfmeznn cousex bls ltcmaqltki my Rjzn Hfetoxea Gqmexyt axtfnj 1467 fyd axpd g rptgq nivmpr jndc zt dwoynh hjewkjy cousex fwpnfmezx. Llhjcto'x dyyypm uswy ybttimpd gqahggpty fqtkw debjcar bzrjx, lnj xhizhsey bprk nydohltki my cwttosr tnj wezypr uk ehk hzrxjdpusoitl llvmlbky tn zmp cousexypxz. Qltkw, tn 1508, Ptsatsps Zwttnjxiax, tn nnd wuwv Puqtgxfahof, tnbjytki ehk ylbaql rkhea, g hciznnar hzmvtyety zf zmp Volpnkwp cousex. Yse Zwttnjxiax nivmpr, nthebjc, otqj pxtgijjo a vwzgxjdsoap, roltd, gso pxjoiiylbrj dyyypm ltc scnecnnyg hjewkjy cousex fwpnfmezx.

Hhgy ts tth ktthn gx ehk Atgksprk htpnjc wgx zroltngqwy jjdcxnmej gj Gotgat Gltzndtg Gplrfdo os siy 1553 gzoq Ql cokca jjw. Sol. Riualn Hfetoxea Hjwlgxz. Hk gfiry fpus ehk ylbaql rkhea uk Eroysesnfs, hze ajipd g wppkfeitl "noaseexxtgt" (f vee) yz scnecn htpnjc arusahjes kapre qptzjc. Wnjcegx Llhjcto fyd Zwttnjxiax fski l focpd vfetkwy ol xfbyyttaytotx, Merqlsu'x dcnjxe sjlnz yse vfetkwy ol xfbyyttaytotx noaqo bk jlsoqj cnfygki disuwy hd derjntosr a tjh kkd. Veex hexj eyvnnarqj sosrlk bzrjx zr ymzrz usrgxps, qszwt yz buys pgweikx tn gigathp, ox ycatxxizypd "uze ol glnj" fwotl hizm ehk rpsyfre. Hjwlgxz's sjehui ehax cewztrki dtxtyg yjnuxney ltc otqj tnj vee. Fd iz nd rkqltoaple jlse yz skhfrk f dhuwe kkd ahxfde, yfj be f arkatoax aroaltk hznbjcsgytot, Gplrfdo'y xjszjx wgx notxtdkwlbrd xoxj deizce.

Hqliyj oe Bnretjce vzmloxsej mts jjdcxnatoty ol f disnwax gft yycotlpr gzeoqjj cousex gpfuwp tnj noawe ol Mpnxd TIO tq Fxfyck, ny 1586. Lgypr, os ehk 19ys ckseuxd, ehk nyvkseius zf Hjwlgxz's inahkw hay rtsgyerogftki eo Bnretjce. Jfgij Plht ny hox moup Ehk Hzdkgcegppry qlmkseej yse sndazycihzeius my yfjitl ehgy siyyzre mld "olyoxjo tnnd isuzrzfyt itytxnmuznzn gso itxeegi yasjo a xjrrkxdibj lnj jwesjytgwj cousex kzr nnx [Volpnkwp] tntfgn mp hgi yozmtnm yz du bttn ne". pohzCZK{g1gt3w3_n1pn3wd_ax3s7_maj_hof08hk0}

Ehk Atgksprk htpnjc ggnyej f cevzeaznzn ltc bknyg kcnevytotfwle xerusr. Nuypd gzehuw lnj rltnjxaznnigs Nhgwwey Qftcnogk Izdmxzn (Rjhiy Hlrxtwl) ifwlki ehk Atgksprk htpnjc utgcegplbrj tn nnd 1868 pojne "Zmp Arusahje Cousex" ny a imtljwpn'y rlggetnk. Ny 1917, Sinpnznqii Fxexnnat ipsiwtbki ehk Atgksprk htpnjc ay "nxpuxdihqp ol ycatxwaznzn". Zmts xjauzfeius hay szt jjdexapd. Imlrrjd Bggmamj ts qszwt yz hgap bxtvet f gaxnlnz tq tnj nivmpr gx paxqj ay 1854; mzwkapr, nj oijs'e pagwiym siy bzrq. Plsoxvi kseixjwy hwzkk yse inahkw lnj ufbrndhki ehk ypcnstqaj tn zmp 19tn hpnzzcy. Kapn hjqoxj ehox, ehuzrh, ytxe yptlrjo cxdatgsllexes itflj tncgxtotfwle gcegp ehk htpnjc it yse 16zm netyfre.

Hcyvyzgxfahoh dloip raqp uyjo ay f narhflgytot ftd hd ehk Xhiyx Lrsd mezbpet 1914 fyd 1940.
Zmp Volpnkwp cousex nd soralk jyoals tu gp a lnplj htpnjc il ne iy zdej ny cusuutheius hizm nivmpr jndky. Yse Ityfkiprgyp Szfeey tq Asjciif, qox jiasuwe, axpd g gcayx nivmpr jndk zt tmvqpmkse tnj Gimjyexj nivmpr jzcitl ehk Fxexnnat Htvoq Hax. Yse Ityfkiprghj's sjdsglps cjce lfc fxtx skhcez fyd zmp Utnzn xjrurfcle hcaippd zmpix rpsyfrey. Ysruzrhuze tnj hax, yse Ityfkiprgyp lkfoexxsiv ucisfcird cernpd auzn zmcek ppy vmcayjd, "Mgsnhkxeex Gwulk", "Nosuwezj Giiyzre" fyd, gx ehk blr ifxe zt l crtde, "Itxe Xjerogftoty".

Goqmexy Gexslm zwtej yz rkulix yse hwzkks nivmpr (iwpaznyg zmp Vkwyas?밃tgksprk htpnjc it 1918), gft, tt xazypr cmlt nj oij, yse inahkw hay xeirq gursprggwe zt nreueatfwyynd. Vkwyas'x hoxp, socjgex, jgetyfarqj lki eo zmp otj-eisj aaj, f ehktceznnarqj utgcegplbrj nivmpr.
"""

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
```

## Solve
``` python
text = """
Yse lncsz bplr-izcarpnzjo dkxnroueius zf g uzlefwpnfmeznn cousex bls ltcmaqltki my Rjzn Hfetoxea Gqmexyt axtfnj 1467 fyd axpd g rptgq nivmpr jndc zt dwoynh hjewkjy cousex fwpnfmezx. Llhjcto'x dyyypm uswy ybttimpd gqahggpty fqtkw debjcar bzrjx, lnj xhizhsey bprk nydohltki my cwttosr tnj wezypr uk ehk hzrxjdpusoitl llvmlbky tn zmp cousexypxz. Qltkw, tn 1508, Ptsatsps Zwttnjxiax, tn nnd wuwv Puqtgxfahof, tnbjytki ehk ylbaql rkhea, g hciznnar hzmvtyety zf zmp Volpnkwp cousex. Yse Zwttnjxiax nivmpr, nthebjc, otqj pxtgijjo a vwzgxjdsoap, roltd, gso pxjoiiylbrj dyyypm ltc scnecnnyg hjewkjy cousex fwpnfmezx.

Hhgy ts tth ktthn gx ehk Atgksprk htpnjc wgx zroltngqwy jjdcxnmej gj Gotgat Gltzndtg Gplrfdo os siy 1553 gzoq Ql cokca jjw. Sol. Riualn Hfetoxea Hjwlgxz. Hk gfiry fpus ehk ylbaql rkhea uk Eroysesnfs, hze ajipd g wppkfeitl "noaseexxtgt" (f vee) yz scnecn htpnjc arusahjes kapre qptzjc. Wnjcegx Llhjcto fyd Zwttnjxiax fski l focpd vfetkwy ol xfbyyttaytotx, Merqlsu'x dcnjxe sjlnz yse vfetkwy ol xfbyyttaytotx noaqo bk jlsoqj cnfygki disuwy hd derjntosr a tjh kkd. Veex hexj eyvnnarqj sosrlk bzrjx zr ymzrz usrgxps, qszwt yz buys pgweikx tn gigathp, ox ycatxxizypd "uze ol glnj" fwotl hizm ehk rpsyfre. Hjwlgxz's sjehui ehax cewztrki dtxtyg yjnuxney ltc otqj tnj vee. Fd iz nd rkqltoaple jlse yz skhfrk f dhuwe kkd ahxfde, yfj be f arkatoax aroaltk hznbjcsgytot, Gplrfdo'y xjszjx wgx notxtdkwlbrd xoxj deizce.

Hqliyj oe Bnretjce vzmloxsej mts jjdcxnatoty ol f disnwax gft yycotlpr gzeoqjj cousex gpfuwp tnj noawe ol Mpnxd TIO tq Fxfyck, ny 1586. Lgypr, os ehk 19ys ckseuxd, ehk nyvkseius zf Hjwlgxz's inahkw hay rtsgyerogftki eo Bnretjce. Jfgij Plht ny hox moup Ehk Hzdkgcegppry qlmkseej yse sndazycihzeius my yfjitl ehgy siyyzre mld "olyoxjo tnnd isuzrzfyt itytxnmuznzn gso itxeegi yasjo a xjrrkxdibj lnj jwesjytgwj cousex kzr nnx [Volpnkwp] tntfgn mp hgi yozmtnm yz du bttn ne". pohzCZK{g1gt3w3_n1pn3wd_ax3s7_maj_hof08hk0}

Ehk Atgksprk htpnjc ggnyej f cevzeaznzn ltc bknyg kcnevytotfwle xerusr. Nuypd gzehuw lnj rltnjxaznnigs Nhgwwey Qftcnogk Izdmxzn (Rjhiy Hlrxtwl) ifwlki ehk Atgksprk htpnjc utgcegplbrj tn nnd 1868 pojne "Zmp Arusahje Cousex" ny a imtljwpn'y rlggetnk. Ny 1917, Sinpnznqii Fxexnnat ipsiwtbki ehk Atgksprk htpnjc ay "nxpuxdihqp ol ycatxwaznzn". Zmts xjauzfeius hay szt jjdexapd. Imlrrjd Bggmamj ts qszwt yz hgap bxtvet f gaxnlnz tq tnj nivmpr gx paxqj ay 1854; mzwkapr, nj oijs'e pagwiym siy bzrq. Plsoxvi kseixjwy hwzkk yse inahkw lnj ufbrndhki ehk ypcnstqaj tn zmp 19tn hpnzzcy. Kapn hjqoxj ehox, ehuzrh, ytxe yptlrjo cxdatgsllexes itflj tncgxtotfwle gcegp ehk htpnjc it yse 16zm netyfre.

Hcyvyzgxfahoh dloip raqp uyjo ay f narhflgytot ftd hd ehk Xhiyx Lrsd mezbpet 1914 fyd 1940.
Zmp Volpnkwp cousex nd soralk jyoals tu gp a lnplj htpnjc il ne iy zdej ny cusuutheius hizm nivmpr jndky. Yse Ityfkiprgyp Szfeey tq Asjciif, qox jiasuwe, axpd g gcayx nivmpr jndk zt tmvqpmkse tnj Gimjyexj nivmpr jzcitl ehk Fxexnnat Htvoq Hax. Yse Ityfkiprghj's sjdsglps cjce lfc fxtx skhcez fyd zmp Utnzn xjrurfcle hcaippd zmpix rpsyfrey. Ysruzrhuze tnj hax, yse Ityfkiprgyp lkfoexxsiv ucisfcird cernpd auzn zmcek ppy vmcayjd, "Mgsnhkxeex Gwulk", "Nosuwezj Giiyzre" fyd, gx ehk blr ifxe zt l crtde, "Itxe Xjerogftoty".

Goqmexy Gexslm zwtej yz rkulix yse hwzkks nivmpr (iwpaznyg zmp Vkwyas?밃tgksprk htpnjc it 1918), gft, tt xazypr cmlt nj oij, yse inahkw hay xeirq gursprggwe zt nreueatfwyynd. Vkwyas'x hoxp, socjgex, jgetyfarqj lki eo zmp otj-eisj aaj, f ehktceznnarqj utgcegplbrj nivmpr.
"""
key = "flag"

def encrypt(plain, key):
    plain = list(plain)
    j = 0
    for i in range(len(plain)):
        j %= len(key)
        if plain[i].islower():
            if key[j].islower():
                plain[i] = (ord(plain[i]) - 97 + ord(key[j]) - 97) % 26
            elif key[j].isupper():
                plain[i] = (ord(plain[i]) - 97 + ord(key[j]) - 65) % 26
            plain[i] += 97
        elif plain[i].isupper():
            if key[j].islower():
                plain[i] = (ord(plain[i]) - 65 + ord(key[j]) - 97) % 26
            elif key[j].isupper():
                plain[i] = (ord(plain[i]) - 65 + ord(key[j]) - 65) % 26
            plain[i] += 65
        else:
            plain[i] = ord(plain[i])
        j += 1
    return ''.join(map(chr, plain))

def decrypt(cipher, key):
    cipher = list(cipher)
    j = 0
    for i in range(len(cipher)):
        j %= len(key)
        if cipher[i].islower():
            if key[j].islower():
                cipher[i] = (ord(cipher[i]) - ord(key[j])) % 26
            elif key[j].isupper():
                cipher[i] = (ord(cipher[i]) - 97 - ord(key[j]) + 65) % 26
            if cipher[i] < 0:
                cipher[i] += 26
            cipher[i] += 97
            j += 1
        elif cipher[i].isupper():
            if key[j].islower():
                cipher[i] = (ord(cipher[i]) - 65 - ord(key[j]) + 97) % 26
            elif key[j].isupper():
                cipher[i] = (ord(cipher[i]) - ord(key[j])) % 26
            if cipher[i] < 0:
                cipher[i] += 26
            cipher[i] += 65
            j += 1
        else:
            cipher[i] = ord(cipher[i])
    return ''.join(map(chr, cipher))

print(decrypt(text, key))
```
"blaise의 암호"라고 말하는 것을 보니 비즈네르 암호(vigenere cipher)이다.  
비즈네르 암호는 16세기 지오반 바스티타 벨라소(이탈리아어: Giovan Battista Bellaso)라는 이탈리아인이 만들었다. '비즈네르'라는 이름의 유래는 프랑스의 외교관이었던 블레즈 드 비즈네르(프랑스어: Blaise de Vigenère)라는 다른 암호를 만든 사람인데, 역사적인 인용의 오류 때문에 비즈네르라는 이름으로 굳어졌다.  

flag: `picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_cdf08bf0}`
