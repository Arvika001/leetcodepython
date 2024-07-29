/**
 * @param {number[]} rating
 * @return {number}
 */
var numTeams = function(rating) {
    const n = rating.length;
    let teams = 0;

    // Iterate through each soldier as the middle member of the team
    for (let j = 0; j < n; j++) {
        let countSmallerLeft = 0;
        let countLargerLeft = 0;
        let countSmallerRight = 0;
        let countLargerRight = 0;

        // Count how many ratings are smaller and larger to the left of j
        for (let i = 0; i < j; i++) {
            if (rating[i] < rating[j]) {
                countSmallerLeft++;
            } else if (rating[i] > rating[j]) {
                countLargerLeft++;
            }
        }

        // Count how many ratings are smaller and larger to the right of j
        for (let k = j + 1; k < n; k++) {
            if (rating[j] < rating[k]) {
                countLargerRight++;
            } else if (rating[j] > rating[k]) {
                countSmallerRight++;
            }
        }

        // Calculate the number of valid teams with j as the middle member
        teams += countLargerLeft * countSmallerRight + countSmallerLeft * countLargerRight;
    }

    return teams;
};
