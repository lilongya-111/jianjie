#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "t_stdio.h"
int main(int argc, char *argv[])
{
    int flags = O_RDONLY | O_CREAT | O_EXCL;
    int mode = 00644;
    int fd = open(argv[1], flags, mode);
    if (fd == -1)
        E_MSG("open", -1);
    printf("file %s open success...", argv[1]);
    close(fd);

    return 0;
}
