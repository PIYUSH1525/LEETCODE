/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    return arr.slice()                // create a shallow copy to avoid mutating original array
              .sort((a, b) => fn(a) - fn(b));  // sort by the value returned by fn
};
