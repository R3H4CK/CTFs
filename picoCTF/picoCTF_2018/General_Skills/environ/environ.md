환경변수(environment variable)는 프로세스가 시스템에서 동작하는데 영향을 주는 동적인 값들의 모임이다.  
리눅스 기반 환경에서 환경변수를 확인하려면 env(environment) 또는 export를 사용하면 된다.
``` bash
env | grep pico
```
SECRET_FLAG=picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}
``` bash
export | grep pico
```
declare -x SECRET_FLAG="picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}"
