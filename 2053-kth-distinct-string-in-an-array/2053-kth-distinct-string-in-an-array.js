/**
 * @param {string[]} arr
 * @param {number} k
 * @return {string}
 */
var kthDistinct = function(arr, k) {
    const count = {}; // Object to count occurrences of each string
    
    // Count occurrences of each string
    for (const string of arr) {
        count[string] = (count[string] || 0) + 1;
    }

    // Collect distinct strings
    const distinctStrings = [];
    for (const string of arr) {
        if (count[string] === 1) { // Only consider strings that appear once
            distinctStrings.push(string);
        }
    }

    // Return the kth distinct string, if it exists
    if (k <= distinctStrings.length) {
        return distinctStrings[k - 1]; // k is 1-indexed
    } else {
        return ""; // Not enough distinct strings
    }
};
