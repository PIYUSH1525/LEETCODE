/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = n;       // initialize count with n
    return function() {
        return count++;  // return current count, then increment
    };
};
