/**
 * @param {string} sentence1
 * @param {string} sentence2
 * @return {boolean}
 */
var areSentencesSimilar = function(sentence1, sentence2) {
    // Split the sentences into arrays of words
    const words1 = sentence1.split(' ');
    const words2 = sentence2.split(' ');

    // Ensure words1 is the longer array
    if (words1.length < words2.length) {
        return areSentencesSimilar(sentence2, sentence1);
    }

    const lenWords1 = words1.length;
    const lenWords2 = words2.length;

    // Check for matching from both ends
    let startIndex = 0;
    while (startIndex < lenWords2 && words1[startIndex] === words2[startIndex]) {
        startIndex++;
    }

    let endIndex = 0;
    while (endIndex < lenWords2 && words1[lenWords1 - 1 - endIndex] === words2[lenWords2 - 1 - endIndex]) {
        endIndex++;
    }

    // Calculate total matched words and check if they cover all of words2
    return startIndex + endIndex >= lenWords2;
};