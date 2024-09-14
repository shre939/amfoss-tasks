#include <stdio.h>

int main() {
    char content[1000];
    FILE *input = fopen("input.txt", "r");
    FILE *output = fopen("output.txt", "w");

    if (input == NULL || output == NULL) {
        return 1;
    }

    while (fgets(content, sizeof(content), input) != NULL) {
        fputs(content, output);
    }

    fclose(input);
    fclose(output);
    return 0;
}
