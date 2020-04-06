해당 프로그램을 실행하면 'out', 'error'에서 출력하는 문자가 뒤죽박죽 섞여있다. 이를 해결하기 위해서는 널 장치(null device)라는 것을 이용하는데 기록 대상이 되는 모든 데이터를 버리지만 쓰기 작업은 성공했다고 보고하는 장치이다.  
UNIX/LINUX 계열 시스템에서는 /dev/null 이라는 널 장치가 존재한다. 따라서 문제가 되는 스트림을 이 공간에 버리면 된다.
참고: stdin(0), stdout(1), stderr(2)

``` bash
./in-out-error 1>/dev/null
```
Please may I have the flag?  
picoCTF{p1p1ng_1S_4_7h1ng_437b5c88}picoCTF{p1p1ng_1S_4_7h1ng_437b5c88}picoCTF{p1p1ng_1S_4_7h1ng_437b5c88}...  
  
flag: `picoCTF{p1p1ng_1S_4_7h1ng_437b5c88}`
