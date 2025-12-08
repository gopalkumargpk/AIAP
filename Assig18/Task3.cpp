#include <iostream>
using namespace std;

// Function to calculate factorial using recursion
int factorial(int n) {
    if (n < 0) {
        cout << "Error: Factorial not defined for negative numbers" << endl;
        return -1;
    } else if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Test with different inputs
    int testInputs[] = {5, 0};
    
    cout << "C++ Output:" << endl;
    for (int num : testInputs) {
        int result = factorial(num);
        cout << "Input: " << num << " → Output: Factorial = " << result << endl;
    }
    
    return 0;
}
