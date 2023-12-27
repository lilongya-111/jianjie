#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "t_stdio.h"
int cp_file(int s_fd, int d_fd)
{
    int total = 0;
    int r, w;
    char buf[128]; 
    while ((r = read(s_fd, buf, 128)) > 0)
    {
        char *tmp = buf;
        while (r > 0)
        {
            w = write(d_fd, tmp, r);
            r = r - w;
            total += w;
            tmp+=w;
        }
    }
    return total;
}

int main(int argc, char *argv[])
{

    int src_fd = open(argv[1], O_RDONLY);
    int flags = O_WRONLY | O_CREAT | O_TRUNC;
    int dst_fd = open(argv[2], flags, 0644);
    if ((src_fd == -1) | (dst_fd == -1))
        E_MSG("open", -1);
    cp_file(src_fd, dst_fd);
    close(src_fd);
    close(dst_fd);
    return 0;
}