/**
 * @param {number} n
 * @return {boolean}
 */
var isUgly = function(n) {
    if (n <= 0) {
        return false; // Ugly numbers are positive
    }

    // Divide n by 2, 3, and 5 until it is no longer divisible
    for (let factor of [2, 3, 5]) {
        while (n % factor === 0) {
            n /= factor;
        }
    }

    // If n is reduced to 1, it is an ugly number
    return n === 1;
};
