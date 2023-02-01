use std::cmp;

fn capacity(left: usize, right: usize, height: &Vec<i32>) -> i32 {
    (right - left) as i32 * cmp::min(height[left], height[right])
}

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max = capacity(left, right, &height);
        while left < right {
            if height[left] < height[right] {
                left += 1;
            } else {
                right -= 1;
            }
            max = cmp::max(
                max,
                capacity(left, right, &height)
            );
        }
        max
    }
}
