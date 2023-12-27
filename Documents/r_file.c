#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "t_stdio.h"
int main(int argc, char *argv[])
{
    int fd = open(argv[1], O_RDONLY);
    if (fd == -1)
        E_MSG("open", -1);
    printf("file %s open success...", argv[1]);
    close(fd);

    return 0;
}
