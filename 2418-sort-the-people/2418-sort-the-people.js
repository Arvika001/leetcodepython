/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    // Create a list of tuples (height, name)
    let people = names.map((name, index) => [heights[index], name]);
    
    // Sort the list in descending order based on height
    people.sort((a, b) => b[0] - a[0]);
    
    // Extract the names from the sorted list
    let sortedNames = people.map(person => person[1]);
    
    return sortedNames;
};
