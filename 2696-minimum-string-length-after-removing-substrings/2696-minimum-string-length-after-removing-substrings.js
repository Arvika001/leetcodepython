/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    const stack = [];
    
    for (let c of s) {
        // Check if we can remove "AB" or "CD"
        if (stack.length > 0 && ((c === 'B' && stack[stack.length - 1] === 'A') || 
                                  (c === 'D' && stack[stack.length - 1] === 'C'))) {
            stack.pop();  // Remove the last character if it forms "AB" or "CD"
        } else {
            stack.push(c);  // Otherwise, add the current character to the stack
        }
    }
    
    return stack.length;  // The length of the remaining characters in the stack
};
