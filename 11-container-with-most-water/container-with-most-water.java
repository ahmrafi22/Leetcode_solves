class Solution {
    public int maxArea(int[] height) {
        int first = 0;
        int last = height.length - 1;
        int area = 0;
        
        while (last > first) {
            area = Math.max(area, Math.min(height[first], height[last]) * Math.abs(first - last));
            
            if (height[first] < height[last]) {
                first++;
            } else {
                last--;
            }
        }
        
        return area;
    }
}