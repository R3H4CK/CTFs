# be-quick-or-be-dead-1

## Summary
* XOR(eXclusive OR)
* signal

## Solution
``` c
#include <stdio.h>
#include <unistd.h>
#include <signal.h>

int key;

void __noreturn alarm_handler()
{
  puts("You need a faster machine. Bye bye.");
  exit(0);
}

unsigned int set_timer()
{
  if ( __sysv_signal(14, (__sighandler_t)alarm_handler) == (__sighandler_t)-1LL )
  {
    printf(
      "\n\nSomething went terribly wrong. \nPlease contact the admins with \"be-quick-or-be-dead-1.c:%d\".\n",
      59LL);
    exit(0);
  }
  return alarm(1u);
}

signed __int64 calculate_key()
{
  signed int v1; // [rsp+0h] [rbp-4h]

  v1 = 1975726731;
  do
    ++v1;
  while ( v1 != -343513834 );
  return 3951453462LL;
}

int get_key()
{
  puts("Calculating key...");
  key = calculate_key();
  return puts("Done calculating key");
}

__int64 __fastcall decrypt_flag(int a1)
{
  __int64 result; // rax
  int v2; // [rsp+0h] [rbp-14h]
  unsigned int i; // [rsp+10h] [rbp-4h]

  v2 = a1;
  for ( i = 0; ; ++i )
  {
    result = i;
    if ( i > 0x39 )
      break;
    flag[i] ^= *((_BYTE *)&v2 + (signed int)i % 4);
    if ( (signed int)i % 4 == 3 )
      ++v2;
  }
  return result;
}

int print_flag()
{
  puts("Printing flag:");
  decrypt_flag(key);
  return puts(flag);
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  header();
  set_timer();
  get_key();
  print_flag();
  return 0;
}
```

Hex-Rays를 적용한 소스를 보자. __sysv_signal 함수는 해당 시그널(signal)이 발생하면, handle에 전달된 함수를 호출한다. 시그널이 alarm_handler를 호출해서 flag를 출력하기 전에 종료된다.  
끝에서 alarm 함수로 1초 후에 시그널을 발생시키는 것을 볼 수 있다. 인자를 10으로 고치면 시그널이 발생하기 전에 끝이나고 flag를 출력할 것이다.

``` bash
gdb be-quick-or-be-dead-1
break *0x000000000040078e
run
set $edi=10
c
```

위의 명령어를 실행하면 flag를 출력한다. (단, 주소는 다를 수 있음)  

flag: `picoCTF{why_bother_doing_unnecessary_computation_402ca676}`
