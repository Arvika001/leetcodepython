/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    const INF = Number.MAX_SAFE_INTEGER;
    const distances = Array.from({ length: 26 }, () => Array(26).fill(INF));

    // Initialize direct transformation costs
    for (let i = 0; i < original.length; i++) {
        const s = original[i].charCodeAt(0) - 'a'.charCodeAt(0);
        const t = changed[i].charCodeAt(0) - 'a'.charCodeAt(0);
        distances[s][t] = Math.min(distances[s][t], cost[i]);
    }

    // Floyd-Warshall algorithm to find minimum costs between all pairs
    for (let k = 0; k < 26; k++) {
        for (let i = 0; i < 26; i++) {
            for (let j = 0; j < 26; j++) {
                distances[i][j] = Math.min(distances[i][j], distances[i][k] + distances[k][j]);
            }
        }
    }

    let totalCost = 0;

    // Calculate the total cost to convert source to target
    for (let i = 0; i < source.length; i++) {
        if (source[i] === target[i]) {
            continue; // No cost if characters are the same
        }

        const srcIndex = source[i].charCodeAt(0) - 'a'.charCodeAt(0);
        const tgtIndex = target[i].charCodeAt(0) - 'a'.charCodeAt(0);

        if (distances[srcIndex][tgtIndex] === INF) {
            return -1; // Impossible to convert this character
        } else {
            totalCost += distances[srcIndex][tgtIndex];
        }
    }

    return totalCost;
};
