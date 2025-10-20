/**
 * @param {number[]} height
 * @return {number}
 */

var maxArea = function (height) {
  let first = 0;
  let last = height.length - 1;
  let area = 0;

  while (last > first) {
    const currentHeight = Math.min(height[first], height[last]);
    const width = last - first;
    area = Math.max(area, currentHeight * width);

    if (height[first] < height[last]) {
      first++;
    } else {
      last--;
    }
  }

  return area;
};
