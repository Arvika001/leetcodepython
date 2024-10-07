/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0; // Pointer for the position of the next valid element

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i]; // Move valid element to the front
            k++; // Increment the count of valid elements
        }
    }

    return k; // Return the count of valid elements
};
