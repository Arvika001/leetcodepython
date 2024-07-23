/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    // Create a frequency map to count occurrences of each number
    const freqMap = {};
    
    // Count the frequency of each number
    for (const num of nums) {
        freqMap[num] = (freqMap[num] || 0) + 1;
    }
    
    // Sort the numbers based on frequency and then by value
    const sortedNums = nums.sort((a, b) => {
        const freqA = freqMap[a];
        const freqB = freqMap[b];
        
        // Sort by frequency (ascending), and by value (descending) for ties
        if (freqA === freqB) {
            return b - a; // Larger numbers first if frequencies are the same
        }
        return freqA - freqB; // Lower frequency first
    });
    
    return sortedNums;
};
