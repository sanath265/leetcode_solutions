class Solution {
    func buildArray(_ nums: [Int]) -> [Int] {
        var a = [Int]()

        for num in nums {
            if num < nums.count {
                a.append(nums[num])
            }
            // a.append[nums[num]]
        }

        return a
    }
}