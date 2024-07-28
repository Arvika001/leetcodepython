/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n <= 0) {
        return false; // Ugly numbers are positive
    }

    // Continuously divide n by 2, 3, and 5
    while (n % 2 === 0) {
        n /= 2;
    }
    while (n % 3 === 0) {
        n /= 3;
    }
    while (n % 5 === 0) {
        n /= 5;
    }

    // If n is reduced to 1, it is an ugly number
    return n === 1;
};
