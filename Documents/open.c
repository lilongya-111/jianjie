//#include<stdio.h>
//#include<errno.h>
//#include<string.h>
#include "t_stdio.h"

int main(int argc,char *argv[])
{
    FILE* fp=fopen(argv[1],"r");
    if(fp==NULL)
    {
       // perror("fopen");
       // printf("fopen faied...%d\n",errno);
        //printf("fopen faied...%s\n",strerror(errno));
        E_MSG("fopen",-1);
        //return -1;
    }

    printf("fopen success...\n");
    fclose(fp);
    return 0;


}