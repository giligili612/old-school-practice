#ifndef TINY_LOG_H
#define TINY_LOG_H

#include <stdio.h>

#define COLOR_RESET   "\033[0m"
#define COLOR_RED     "\033[1;31m"
#define COLOR_GREEN   "\033[32m"
#define COLOR_YELLOW  "\033[1;33m"
#define COLOR_BLUE    "\033[34m"

#define TINY_LOG_DEBUG(fmt, ...) \
    fprintf(stderr, COLOR_BLUE "[DEBUG] " fmt "\n", ##__VA_ARGS__);

#define TINY_LOG_INFO(fmt, ...) \
    fprintf(stderr, COLOR_RESET "[INFO] " fmt "\n", ##__VA_ARGS__);

#define TINY_LOG_WARN(fmt, ...) \
    fprintf(stderr, COLOR_YELLOW "[WARN] " fmt "\n", ##__VA_ARGS__);

#define TINY_LOG_ERROR(fmt, ...) \
    fprintf(stderr, COLOR_RED "[ERROR] " fmt "\n", ##__VA_ARGS__);

#endif