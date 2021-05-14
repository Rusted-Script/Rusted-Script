/*
Copyright (c) Rusted Studio
Licensed under APGL-3.0 license. Read LiCENSE.txt for more info
Developers:
CertifiedRice - Lead Developer
Rusted Studio - Development Studio
Rusted Script Github Repository Contributors - Developers
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define _GNU_SOURCE
#define PY_SSIZE_T_CLEAN

int main(void)
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("test.rusted", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        int lenofline = read;
        char final[256];
        char * cmd = "python3 main.py run_line ";
        char * token = strtok(line, "\r");
        snprintf(final, sizeof final, "%s%s", cmd, token);
        system(final);
    }

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}
