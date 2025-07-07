/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
        const arr = new Set(nums);
        return nums.length !== arr.size;
};