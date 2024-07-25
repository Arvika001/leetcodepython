/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    // Base case: if the array has 0 or 1 element, it's already sorted
    if (nums.length <= 1) {
        return nums;
    }

    // Split the array into two halves
    const mid = Math.floor(nums.length / 2);
    const left = sortArray(nums.slice(0, mid));
    const right = sortArray(nums.slice(mid));

    // Merge the sorted halves
    return merge(left, right);
};

// Helper function to merge two sorted arrays
function merge(left, right) {
    const sorted = [];
    let i = 0, j = 0;

    // Compare elements from left and right arrays and merge them in sorted order
    while (i < left.length && j < right.length) {
        if (left[i] <= right[j]) {
            sorted.push(left[i]);
            i++;
        } else {
            sorted.push(right[j]);
            j++;
        }
    }

    // If there are remaining elements in left, add them
    while (i < left.length) {
        sorted.push(left[i]);
        i++;
    }

    // If there are remaining elements in right, add them
    while (j < right.length) {
        sorted.push(right[j]);
        j++;
    }

    return sorted;
}