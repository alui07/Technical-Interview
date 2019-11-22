/* 204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
*/
class Solution {
    public int countPrimes(int n) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 1 && isPrime(i) || i == 2) {
                count++;
            }
        }
        return count;
    }
    
    public boolean isPrime(int n) {
        if (n == 1) return false;
        for (int i = 2; i*i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}