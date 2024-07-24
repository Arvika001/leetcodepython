/**
 * @param {number[]} mapping
 * @param {number[]} nums
 * @return {number[]}
 */
var sortJumbled = function(mapping, nums) {
    // Helper function to get the mapped number
    const getMappedNum = (num) => {
        if (num < 10) {
            return mapping[num];
        }

        let mappedNum = 0;
        let placeValue = 1;

        while (num > 0) {
            const lastDigit = num % 10;
            const mappedDigit = mapping[lastDigit];
            mappedNum += mappedDigit * placeValue;

            placeValue *= 10;
            num = Math.floor(num / 10);
        }

        return mappedNum;
    };

    // Create an array of tuples (mapped value, original index)
    const mappedNums = nums.map((num, i) => [getMappedNum(num), i]);

    // Sort based on the mapped values, maintaining original order for ties
    mappedNums.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1];
        }
        return a[0] - b[0];
    });

    // Extract the sorted original numbers based on their mapped values
    return mappedNums.map(([_, i]) => nums[i]);
};
