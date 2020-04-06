쉘에서 해당 경로로 이동하면 굉장히 많은 폴더들이 보인다. 이 중에서 flag를 찾아야 하는데, 이런 경우 정규 표현식을 이용하여 풀 수 있다.

``` bash
cat */* | grep pico
```
``` bash
grep -r pico
```

picoCTF{grep_r_and_you_will_find_24c911ab}
