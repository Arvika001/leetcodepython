/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    return n > 0 && (n & (n - 1)) === 0 && (n & 0x55555555) !== 0;
};
