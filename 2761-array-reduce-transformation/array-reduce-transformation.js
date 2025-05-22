/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let accumulator = init;
    for (let num of nums) {
        accumulator = fn(accumulator, num);
    }
    return accumulator;
};