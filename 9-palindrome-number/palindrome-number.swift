class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        
        if (x < 0) {
            return false
        }

        var ans = 0
        var prev = x

        while(prev > 0) {
            ans = ans * 10 + prev % 10
            prev = prev/10
        }

        return true ? (ans == x) : false
    }
}