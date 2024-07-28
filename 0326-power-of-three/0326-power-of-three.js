/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    if (n <= 0) {
        return false; // Powers of three are positive integers
    }
    
    while (n % 3 === 0) {
        n /= 3; // Divide n by 3 until it is no longer divisible
    }
    
    return n === 1; // If n is reduced to 1, it is a power of three
};
