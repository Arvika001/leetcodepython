/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
    let count = 0; // Initialize a counter for seniors

    for (let detail of details) {
        // Extract the age from the string (characters at indices 11 and 12)
        let ageStr = detail.substring(11, 13); // The age is represented by the 12th and 13th characters
        let age = parseInt(ageStr); // Convert the age string to an integer
        
        // Check if the age is greater than 60
        if (age > 60) {
            count++; // Increment the counter if the age is greater than 60
        }
    }

    return count; // Return the total count of seniors
};
