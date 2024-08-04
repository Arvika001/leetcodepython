/**
 * @param {number[]} nums
 * @param {number} n
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeSum = function(nums, n, left, right) {
    const MOD = 1e9 + 7; // Define the modulo constant
    const minHeap = []; // Use an array to simulate a min-heap

    // Calculate all subarray sums and push them into the min-heap
    for (let i = 0; i < n; i++) {
        let currentSum = 0;
        for (let j = i; j < n; j++) {
            currentSum += nums[j];
            minHeap.push(currentSum); // Add the current subarray sum
        }
    }

    // Sort the min-heap to get the sums in non-decreasing order
    minHeap.sort((a, b) => a - b);

    // Calculate the sum of the numbers from index left to index right
    let result = 0;
    for (let i = left - 1; i < right; i++) {
        result = (result + minHeap[i]) % MOD; // Use modulo to avoid overflow
    }

    return result; // Return the final result
};
