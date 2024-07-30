/**
 * @param {string} s
 * @return {number}
 */
var minimumDeletions = function(s) {
    const n = s.length;

    // Count total 'a's in the string
    let counta = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === 'a') {
            counta++;
        }
    }

    // Initialize variables to track minimum deletions
    let count = Infinity;  // To track the minimum deletions
    let countb = 0;        // To count the number of 'b's seen so far

    // Iterate through the string to calculate minimum deletions
    for (let i = 0; i < n; i++) {
        if (s[i] === 'a') {
            counta--;  // One less 'a' to consider
        }
        count = Math.min(count, countb + counta);  // Update minimum deletions

        if (s[i] === 'b') {
            countb++;  // Increment count of 'b's
        }
    }

    return count;
};
