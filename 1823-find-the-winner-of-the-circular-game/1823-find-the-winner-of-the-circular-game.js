/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    let friends = Array.from({ length: n }, (_, index) => index + 1);
    let current_position = 0;
    
    while (friends.length > 1) {
        let to_remove = (current_position + k - 1) % friends.length;
        friends.splice(to_remove, 1);
        current_position = to_remove % friends.length;
    }
    
    return friends[0];
    
      
};