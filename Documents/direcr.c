#include "t_stdio.h"
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include<string.h>
int main(int argc, char *argv[])
{
    char*msg="this is a test";
    int flags = O_WRONLY | O_CREAT | O_TRUNC;
    int fd = open(argv[1], flags, 0644);
    if (fd == -1)
        E_MSG("open", -1);
    int s_fd = dup(1);
    dup2(fd, 1);
    close(fd);
    write(1,msg,strlen(msg));
    dup2(s_fd,1);
    close(s_fd);
    write(1,msg,strlen(msg));

    return 0;
}