# hertz
> Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with nc 2018shell.picoctf.com 48186.

## Summary
* mono-alphabetic substitution cipher
* classical cipher

## Analysis
``` python
text = """
-------------------------------------------------------------------------------
hpukwjit cnwn at dpow qzjk - tobtiaioiapu_hagcnwt_jwn_tpzxjbzn_xvjthwyajl
-------------------------------------------------------------------------------
"ynzz, gwauhn, tp knupj juv zohhj jwn upy moti qjlazd ntijint pq icn
bopujgjwint. boi a yjwu dpo, aq dpo vpui inzz ln icji icat lnjut yjw,
aq dpo tiazz iwd ip vnqnuv icn auqjlant juv cpwwpwt gnwgniwjinv bd icji
juiahcwati-a wnjzzd bnzanxn cn at juiahcwati-a yazz cjxn upicauk
lpwn ip vp yaic dpo juv dpo jwn up zpuknw ld qwanuv, up zpuknw ld
'qjaicqoz tzjxn,' jt dpo hjzz dpowtnzq! boi cpy vp dpo vp? a tnn a
cjxn qwakcinunv dpo-tai vpyu juv inzz ln jzz icn unyt."

ai yjt au mozd, 1805, juv icn tgnjenw yjt icn ynzz-eupyu juuj gjxzpxuj
thcnwnw, ljav pq cpupw juv qjxpwain pq icn nlgwntt ljwdj qnvpwpxuj.
yaic icntn ypwvt tcn kwnninv gwauhn xjtaza eowjkau, j lju pq cakc
wjue juv algpwijuhn, ycp yjt icn qawti ip jwwaxn ji cnw wnhngiapu. juuj
gxzpxuj cjv cjv j hpokc qpw tpln vjdt. tcn yjt, jt tcn tjav, toqqnwauk
qwpl zj kwaggn; kwaggn bnauk icnu j uny ypwv au ti. gninwtbowk, otnv
puzd bd icn nzain.

jzz cnw auxaijiaput yaicpoi nrhngiapu, ywaiinu au qwnuhc, juv vnzaxnwnv
bd j thjwzni-zaxnwanv qppilju icji lpwuauk, wju jt qpzzpyt:

"aq dpo cjxn upicauk bniinw ip vp, hpoui (pw gwauhn), juv aq icn
gwptgnhi pq tgnuvauk ju nxnuauk yaic j gppw auxjzav at upi ipp inwwabzn,
a tcjzz bn xnwd hcjwlnv ip tnn dpo ipuakci bniynnu 7 juv 10 juuniin
thcnwnw."

"cnjxnut! ycji j xawoznui jiijhe!" wngzanv icn gwauhn, upi au icn
znjti vathpuhnwinv bd icat wnhngiapu. cn cjv moti nuinwnv, ynjwauk ju
nlbwpavnwnv hpowi ouaqpwl, eunn bwnnhcnt, juv tcpnt, juv cjv tijwt pu
cat bwnjti juv j tnwnun nrgwnttapu pu cat qzji qjhn. cn tgpen au icji
wnqaunv qwnuhc au ycahc pow kwjuvqjicnwt upi puzd tgpen boi icpokci, juv
yaic icn knuizn, gjiwpuafauk auipujiapu ujiowjz ip j lju pq algpwijuhn
ycp cjv kwpyu pzv au tphanid juv ji hpowi. cn ynui og ip juuj gxzpxuj,
eattnv cnw cjuv, gwntnuiauk ip cnw cat bjzv, thnuinv, juv tcauauk cnjv,
juv hplgzjhnuizd tnjinv caltnzq pu icn tpqj.

"qawti pq jzz, vnjw qwanuv, inzz ln cpy dpo jwn. tni dpow qwanuv't
lauv ji wnti," tjav cn yaicpoi jzinwauk cat ipun, bnunjic icn
gpzainuntt juv jqqnhinv tdlgjicd pq ycahc auvaqqnwnuhn juv nxnu awpud
hpozv bn vathnwunv.
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
-------------------------------------------------------------------------------
hpukwjit cnwn at dpow qzjk - tobtiaioiapu_hagcnwt_jwn_tpzxjbzn_xvjthwyajl
-------------------------------------------------------------------------------
"ynzz, gwauhn, tp knupj juv zohhj jwn upy moti qjlazd ntijint pq icn
bopujgjwint. boi a yjwu dpo, aq dpo vpui inzz ln icji icat lnjut yjw,
aq dpo tiazz iwd ip vnqnuv icn auqjlant juv cpwwpwt gnwgniwjinv bd icji
juiahcwati-a wnjzzd bnzanxn cn at juiahcwati-a yazz cjxn upicauk
lpwn ip vp yaic dpo juv dpo jwn up zpuknw ld qwanuv, up zpuknw ld
'qjaicqoz tzjxn,' jt dpo hjzz dpowtnzq! boi cpy vp dpo vp? a tnn a
cjxn qwakcinunv dpo-tai vpyu juv inzz ln jzz icn unyt."

ai yjt au mozd, 1805, juv icn tgnjenw yjt icn ynzz-eupyu juuj gjxzpxuj
thcnwnw, ljav pq cpupw juv qjxpwain pq icn nlgwntt ljwdj qnvpwpxuj.
yaic icntn ypwvt tcn kwnninv gwauhn xjtaza eowjkau, j lju pq cakc
wjue juv algpwijuhn, ycp yjt icn qawti ip jwwaxn ji cnw wnhngiapu. juuj
gxzpxuj cjv cjv j hpokc qpw tpln vjdt. tcn yjt, jt tcn tjav, toqqnwauk
qwpl zj kwaggn; kwaggn bnauk icnu j uny ypwv au ti. gninwtbowk, otnv
puzd bd icn nzain.

jzz cnw auxaijiaput yaicpoi nrhngiapu, ywaiinu au qwnuhc, juv vnzaxnwnv
bd j thjwzni-zaxnwanv qppilju icji lpwuauk, wju jt qpzzpyt:

"aq dpo cjxn upicauk bniinw ip vp, hpoui (pw gwauhn), juv aq icn
gwptgnhi pq tgnuvauk ju nxnuauk yaic j gppw auxjzav at upi ipp inwwabzn,
a tcjzz bn xnwd hcjwlnv ip tnn dpo ipuakci bniynnu 7 juv 10 juuniin
thcnwnw."

"cnjxnut! ycji j xawoznui jiijhe!" wngzanv icn gwauhn, upi au icn
znjti vathpuhnwinv bd icat wnhngiapu. cn cjv moti nuinwnv, ynjwauk ju
nlbwpavnwnv hpowi ouaqpwl, eunn bwnnhcnt, juv tcpnt, juv cjv tijwt pu
cat bwnjti juv j tnwnun nrgwnttapu pu cat qzji qjhn. cn tgpen au icji
wnqaunv qwnuhc au ycahc pow kwjuvqjicnwt upi puzd tgpen boi icpokci, juv
yaic icn knuizn, gjiwpuafauk auipujiapu ujiowjz ip j lju pq algpwijuhn
ycp cjv kwpyu pzv au tphanid juv ji hpowi. cn ynui og ip juuj gxzpxuj,
eattnv cnw cjuv, gwntnuiauk ip cnw cat bjzv, thnuinv, juv tcauauk cnjv,
juv hplgzjhnuizd tnjinv caltnzq pu icn tpqj.

"qawti pq jzz, vnjw qwanuv, inzz ln cpy dpo jwn. tni dpow qwanuv't
lauv ji wnti," tjav cn yaicpoi jzinwauk cat ipun, bnunjic icn
gpzainuntt juv jqqnhinv tdlgjicd pq ycahc auvaqqnwnuhn juv nxnu awpud
hpozv bn vathnwunv.
"""

text = list(text)
table = "ibhykxpctagmjeuofzqsndrvwl"
for i in range(len(text)):
    if text[i].islower():
        text[i] = table[ord(text[i]) - 97]
    elif text[i].isupper():
        text[i] = table[ord(text[i]) - 65]
print(''.join(text))
```
문제에서 치환 암호(substitution cipher)를 사용한다고 한다고 하는데 정확하게는 <a href="https://www.dcode.fr/monoalphabetic-substitution" target="_blank">모노 알파베틱 치환 암호</a>(mono-alphabetic substitution cipher)를 사용한다.

flag: `substitution_ciphers_are_solvable_vdascrwiam`
