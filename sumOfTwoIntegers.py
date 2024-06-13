'''
Solved In Java

// Neetcode: https://www.youtube.com/watch?v=gVUrDV4tZfY
// Learn Bit Manipulation: https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

class Solution {
    public int getSum(int a, int b) {
        // Loop until no carry is generated
        while (b != 0) {
            // Calculate carry by ANDing the bits of a and b, then shifting the result to the left by 1 position
            int carry = (a & b) << 1;

            // Calculate sum without considering carry by XORing the bits of a and b
            a = a ^ b;

            // Update b to hold the carry value for the next iteration
            b = carry;
        }
        // Return the final sum
        return a;
    }
}

'''