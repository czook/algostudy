#include <vector>
#include <initializer_list>
#include <iostream>

int maxProduct(std::initializer_list<int> arr) {
    int max_product = 0;
    std::vector<int> vec(arr);
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            int product = vec[i] * vec[j];

            if (max_product == 0 || product > max_product) {
                max_product = product;
            }
        }
    }
    return max_product;
}

int main() {
    auto temp = {2, 3, 4, 5, 6};
    std::cout << "{2, 3, 4, 5, 6} " << maxProduct(temp) << std::endl;
    auto temp2 = {1, 2, 3, 4};
    std::cout << "{1, 2, 3, 4} " << maxProduct(temp2) << std::endl;
    auto temp3 = {1, 1, 2, 2};
    std::cout << "1, 1, 2, 2 " << maxProduct(temp3) << std::endl;
    auto temp4 = {-4, -3, -1, 0, 2};
    std::cout << "-4, -3, -1, 0, 2 " << maxProduct(temp4) << std::endl;
    auto temp5 = {6, 5, 8, 8, 7};
    std::cout << "6, 5, 8, 8, 7 " << maxProduct(temp5) << std::endl;

    return 0;
}

