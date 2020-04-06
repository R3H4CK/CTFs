우선 absolutely-relative.c의 소스를 보면 다음과 같습니다.

``` c
#include <stdio.h>
#include <string.h>

#define yes_len 3
const char *yes = "yes";

int main()
{
    char flag[99];
    char permission[10];
    int i;
    FILE * file;


    file = fopen("/problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/flag.txt" , "r");
    if (file) {
    	while (fscanf(file, "%s", flag)!=EOF)
    	fclose(file);
    }   
	
    file = fopen( "./permission.txt" , "r");
    if (file) {
    	for (i = 0; i < 5; i++){
            fscanf(file, "%s", permission);
        }
        permission[5] = '\0';
        fclose(file);
    }
    
    if (!strncmp(permission, yes, yes_len)) {
        printf("You have the write permissions.\n%s\n", flag);
    } else {
        printf("You do not have sufficient permissions to view the flag.\n");
    }
    
    return 0;
}
```

소스를 보면 flag는 절대경로로 open 하고 permission.txt는 상대경로로 open 한다. 아래의 비교문을 보면 permission.txt에 "yes" 문자열을 넣어주면 flag를 얻을 수 있다는 것을 알 수 있다. 현재 경로에서는 권한 거부 때문에 permission.txt를 만들 수 없으므로 다른 경로에 생성하면 된다.

``` bash
echo "yes" > permission.txt                                                                      
/problems/absolutely-relative_0_d4f0f1c47f503378c4bb81981a80a9b6/absolutely-relative
```

You have the write permissions.  
picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}  
  
flag: `picoCTF{3v3r1ng_1$_r3l3t1v3_befc0ce1}`
