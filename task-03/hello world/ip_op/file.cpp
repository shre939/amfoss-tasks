#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream input("input.txt");
    std::ofstream output("output.txt");
    std::string content;

    if (input && output) {
        while (getline(input, content)) {
            output << content << std::endl;
        }
    }

    input.close();
    output.close();
    return 0;
}
