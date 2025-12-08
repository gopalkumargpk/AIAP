public class CheckNumber {
    
    // Method to check if a number is positive, negative, or zero
    static String checkNumber(int num) {
        if (num > 0) {
            return "The number is positive";
        } else if (num < 0) {
            return "The number is negative";
        } else {
            return "The number is zero";
        }
    }
    
    public static void main(String[] args) {
        // Test with different inputs
        int[] testInputs = {-5, 0, 7};
        
        System.out.println("Java Output:");
        for (int num : testInputs) {
            String result = checkNumber(num);
            System.out.println("Input: " + num + " → Output: " + result);
        }
    }
}
