class Solution {
    func numSubarrayBoundedMax(_ nums: [Int], _ left: Int, _ right: Int) -> Int {
        
        var c = -1
        var ans = 0
        var maxi = 0
        var prev = 0
        for i in 0..<nums.count {
            maxi = max(nums[i], maxi)
            if (maxi >= left && maxi <= right) {
                if nums[i] < left || nums[i] > right {
                    ans += prev - c
                } else {
                    ans += i - c
                    prev = i
                }
            } else if maxi > right {
                c = i
                maxi = 0
                prev = 0
            }

            // print(ans)
        }

        return ans
    }
}