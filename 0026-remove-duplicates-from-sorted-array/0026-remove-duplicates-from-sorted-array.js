/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 0) {
        return 0; // Handle the edge case for empty array
    }

    let k = 1; // Pointer for the position of unique elements

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) { // Check if the current element is different from the last unique element
            nums[k] = nums[i]; // Place the unique element at the k-th position
            k++; // Move the pointer forward
        }
    }

    return k; // Return the number of unique elements
};
