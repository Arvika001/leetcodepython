/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2) {
    // Split the sentences into arrays of words
    let words1 = sentence1.split(' ');
    let words2 = sentence2.split(' ');

    // Ensure words1 is the longer array
    if (words1.length < words2.length) {
        [words1, words2] = [words2, words1]; // Swap using destructuring assignment
    }

    const lenWords1 = words1.length;
    const lenWords2 = words2.length;

    // Check for matching from the start
    let startIndex = 0;
    while (startIndex < lenWords2 && words1[startIndex] === words2[startIndex]) {
        startIndex++;
    }

    // Check for matching from the end
    let endIndex = 0;
    while (endIndex < lenWords2 && words1[lenWords1 - 1 - endIndex] === words2[lenWords2 - 1 - endIndex]) {
        endIndex++;
    }

    // Check if the unmatched part of the longer sentence can accommodate the unmatched part of the shorter sentence
    return startIndex + endIndex >= lenWords2;
};