class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        
        var map = [Int: Int]()

        for i in 0..<nums.count {
            if let index = map[target - nums[i]] {
                return [i, index]
            }

            map[nums[i]] = i
        }

        return []
    }
}