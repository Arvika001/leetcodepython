/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    const t = new Array(n + 1).fill(0); // Initialize the array to store ugly numbers
    t[1] = 1; // The first ugly number is 1

    let i2 = 1, i3 = 1, i5 = 1; // Pointers for 2, 3, and 5

    for (let i = 2; i <= n; i++) {
        const i2thUgly = t[i2] * 2;
        const i3rdUgly = t[i3] * 3;
        const i5thUgly = t[i5] * 5;

        // The next ugly number is the minimum of the three candidates
        t[i] = Math.min(i2thUgly, i3rdUgly, i5thUgly);

        // Increment the pointers based on which candidate was used
        if (t[i] === i2thUgly) {
            i2++;
        }
        if (t[i] === i3rdUgly) {
            i3++;
        }
        if (t[i] === i5thUgly) {
            i5++;
        }
    }

    return t[n]; // Return the nth ugly number
};
