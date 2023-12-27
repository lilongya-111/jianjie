#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define BUF_SIZE 4096

int main(int argc, char *argv[]) {
    int source_fd, dest_fd;
    ssize_t num_read, num_written;
    char buffer[BUF_SIZE];

    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    source_fd = open(argv[1], O_RDONLY);
    if (source_fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    dest_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    if (dest_fd == -1) {
        perror("open");
        exit(EXIT_FAILURE);
    }

    while ((num_read = read(source_fd, buffer, BUF_SIZE)) > 0) {
        num_written = write(dest_fd, buffer, num_read);
        if (num_written != num_read) {
            perror("write");
            exit(EXIT_FAILURE);
        }
    }

    if (num_read == -1) {
        perror("read");
        exit(EXIT_FAILURE);
    }

    if (close(source_fd) == -1) {
        perror("close");
        exit(EXIT_FAILURE);
    }

    if (close(dest_fd) == -1) {
        perror("close");
        exit(EXIT_FAILURE);
    }

    exit(EXIT_SUCCESS);
}