class Solution {
    func containsDuplicate(_ nums: [Int]) -> Bool {
        var nums = nums
        nums.sort()
        // nums.sort()

        for i in 0..<nums.count - 1 {
            if nums[i] == nums[i+1] {
                return true
            }
        }

        return false
    }
}