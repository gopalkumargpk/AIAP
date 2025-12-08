function checkNumber(num) {
    // Check if a number is positive, negative, or zero
    if (num > 0) {
        return "The number is positive";
    } else if (num < 0) {
        return "The number is negative";
    } else {
        return "The number is zero";
    }
}

// Test with different inputs
const testInputs = [-5, 0, 7];

console.log("JavaScript Output:");
testInputs.forEach(num => {
    const result = checkNumber(num);
    console.log(`Input: ${num} → Output: ${result}`);
});
