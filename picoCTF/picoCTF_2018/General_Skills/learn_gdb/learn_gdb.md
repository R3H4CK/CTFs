GNU 디버거(gdb)를 사용할 수 있도록 도와주는 문제이다. 프로그램이 flag를 출력하지 않고 그냥 끝나버리므로 decrypt_flag 함수가 끝나고 나서 바로 다음 지점에 BP를 걸고 gdb 스크립트를 사용하여 flag_buf의 값을 출력하면 된다.

``` bash
gdb run
```

GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1  
Copyright (C) 2016 Free Software Foundation, Inc.  
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>  
This is free software: you are free to change and redistribute it.  
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"  
and "show warranty" for details.  
This GDB was configured as "x86_64-linux-gnu".  
Type "show configuration" for configuration details.  
For bug reporting instructions, please see:  
<http://www.gnu.org/software/gdb/bugs/>.  
Find the GDB manual and other documentation resources online at:  
<http://www.gnu.org/software/gdb/documentation/>.  
For help, type "help".  
Type "apropos word" to search for commands related to "word"...  
Reading symbols from run...(no debugging symbols found)...done.  
(gdb)

``` bash
disass main
```

Dump of assembler code for function main:  
   0x00000000004008c9 <+0>:     push   %rbp  
   0x00000000004008ca <+1>:     mov    %rsp,%rbp  
   0x00000000004008cd <+4>:     sub    $0x10,%rsp  
   0x00000000004008d1 <+8>:     mov    %edi,-0x4(%rbp)  
   0x00000000004008d4 <+11>:    mov    %rsi,-0x10(%rbp)  
   0x00000000004008d8 <+15>:    mov    0x200af9(%rip),%rax        # 0x6013d8 <stdout@@GLIBC_2.2.5>  
   0x00000000004008df <+22>:    mov    $0x0,%ecx  
   0x00000000004008e4 <+27>:    mov    $0x2,%edx                     
   0x00000000004008e9 <+32>:    mov    $0x0,%esi                                                                           
   0x00000000004008ee <+37>:    mov    %rax,%rdi                                                                             
   0x00000000004008f1 <+40>:    callq  0x400650 <setvbuf@plt>                                                                  
   0x00000000004008f6 <+45>:    mov    $0x4009d0,%edi                                                                        
   0x00000000004008fb <+50>:    callq  0x400600 <puts@plt>                                                                   
   0x0000000000400900 <+55>:    mov    $0x0,%eax                                                                             
   0x0000000000400905 <+60>:    callq  0x400786 <decrypt_flag>                                                               
   0x000000000040090a <+65>:    mov    $0x400a08,%edi                                                                        
   0x000000000040090f <+70>:    callq  0x400600 <puts@plt>                                                                   
   0x0000000000400914 <+75>:    mov    $0x0,%eax                                                                             
   0x0000000000400919 <+80>:    leaveq                                                                                       
   0x000000000040091a <+81>:    retq                                                                                         
End of assembler dump.                                                                                                     
(gdb)

``` bash
break* 0x000000000040090a
```

Breakpoint 1 at 0x40090a                                                                                                   
(gdb) 

``` bash
run
```

Starting program: /problems/learn-gdb_0_716957192e537ac769f0975c74b34194/run                                                 
Decrypting the Flag into global variable 'flag_buf'                                                                          
.....................................                                                                                        
                                                                                                                           
Breakpoint 1, 0x000000000040090a in main ()                                                                                  
(gdb) printf "%s\n", (const char*)flag_buf  
picoCTF{gDb_iS_sUp3r_u53fuL_a6c61d82}  
(gdb)  
  
flag: `picoCTF{gDb_iS_sUp3r_u53fuL_a6c61d82}`
