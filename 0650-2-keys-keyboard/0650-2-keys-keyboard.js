/**
 * @param {number} n
 * @return {number}
 */
var minSteps = function(n) {
    // Create a memoization array
    const t = Array(1001).fill().map(() => Array(1001).fill(-1));

    // Helper function to perform the recursive calculation
    function solve(currCountA, pasteCountA) {
        // Base case: if we have exactly n A's
        if (currCountA === n) {
            return 0;
        }
        // If we exceed n A's, return a large number
        if (currCountA > n) {
            return 1000;
        }
        // Return cached result if already computed
        if (t[currCountA][pasteCountA] !== -1) {
            return t[currCountA][pasteCountA];
        }

        // Option 1: Copy and Paste
        const copyPaste = 1 + 1 + solve(currCountA + currCountA, currCountA);
        // Option 2: Paste
        const paste = 1 + solve(currCountA + pasteCountA, pasteCountA);

        // Store the minimum steps in the memoization table
        t[currCountA][pasteCountA] = Math.min(copyPaste, paste);
        return t[currCountA][pasteCountA];
    }

    // Handle the case where n is 1
    if (n === 1) {
        return 0; // We already have 1 A
    }

    // Start the recursion with 1 A and 1 paste
    return 1 + solve(1, 1);
};

