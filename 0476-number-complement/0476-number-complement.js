/**
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    // Create a mask with all bits set to 1 for the length of num
    let mask = 1;
    while (mask < num) {
        mask = (mask << 1) | 1;
    }
    
    // Return the complement using XOR
    return num ^ mask;
};
