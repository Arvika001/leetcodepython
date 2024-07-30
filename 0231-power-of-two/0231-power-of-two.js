/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n < 1) {
        return false; // Powers of two are positive integers
    }
    
    while (n % 2 === 0) {
        n /= 2; // Divide n by 2 until it is no longer divisible
    }
    
    return n === 1; // If n is reduced to 1, it is a power of two
};
