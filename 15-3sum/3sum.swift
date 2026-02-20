class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {

        // [0,0,0,0,1,1,2]
        // 0 - [0, 0]
        // 0 - []
        // [-4,1,1,1,2,2,3,3,3]
        var ans = [[Int]]()
        var nums = nums
        nums.sort()


        for i in 0..<nums.count {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue
            }
            let target = nums[i]
            // print(target)
            var l = i+1
            var r = nums.count - 1

            while(l < r) {
                if (r < nums.count - 1 && nums[l] == nums[l-1] && nums[r] == nums[r+1]) {
                    // l += 1
                    r -= 1
                    continue
                }
                let val = target + nums[l] + nums[r]
                if  val == 0 {
                    ans.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    // print(l, r, [target, nums[l-1], nums[r+1]])
                } else if val < 0 {
                    l += 1
                } else {
                    r -= 1
                }
            }
        }

        return ans
        
    }
}