passwd와 shadow 파일을 주어진 것을 보니 jone the ripper를 사용해서 패스워드를 크래킹 하면 될 것 같다.  
얻은 패스워드로 해당 서버에 접속해서 로그인하면 된다.
``` console
john shadow
```
Warning: detected hash type "sha512crypt", but the string is also recognized as "HMAC-SHA256"  
Use the "--format=HMAC-SHA256" option to force loading these as that type instead  
Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"  
Use the "--format=sha512crypt-opencl" option to force loading these as that type instead  
Using default input encoding: UTF-8  
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])  
Cost 1 (iteration count) is 5000 for all loaded hashes  
Will run 8 OpenMP threads  
Proceeding with single, rules:Single  
Press 'q' or Ctrl-C to abort, almost any other key for status  
Warning: Only 31 candidates buffered for the current salt, minimum 32 needed for performance.  
Warning: Only 21 candidates buffered for the current salt, minimum 32 needed for performance.  
Almost done: Processing the remaining buffered candidate passwords, if any.  
Warning: Only 5 candidates buffered for the current salt, minimum 32 needed for performance.  
Proceeding with wordlist:password.lst, rules:Wordlist  
password1        (root)  
1g 0:00:00:01 DONE 2/3 (2020-04-10 14:31) 0.6042g/s 2396p/s 2396c/s 2396C/s 123456..random  
Use the "--show" option to display all of the cracked passwords reliably  
Session completed  

flag: `picoCTF{J0hn_1$_R1pp3d_1b25af80}`
