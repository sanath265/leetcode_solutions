class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)

        l1 = -1
        l2 = -1
        ans = 0

        block = total // 2 - 1 if total %2 == 0 else total // 2
        while((l1 < len(nums1) or l2 < len(nums2)) and l1 + 1 + l2 + 1 < block):

            if l1 + 1 == len(nums1):
                l2 += 1
            elif l2 + 1 == len(nums2):
                l1 += 1
            elif nums1[l1 + 1] < nums2[l2 + 1]:
                l1 += 1
            else:
                l2 += 1
        # print(l1, l2)
        
        
        if l1 + 1 == len(nums1):
            ans += nums2[l2 + 1]
            l2 += 1
        elif l2 + 1 == len(nums2):
            ans += nums1[l1 + 1]
            l1 += 1
        else:
            # print("s")
            if nums2[l2 + 1] < nums1[l1 + 1]:
                ans = nums2[l2 + 1]
                l2 += 1
            else:
                ans = nums1[l1 + 1]
                l1 += 1
        
        # print(ans)
        if total %2 == 0:
            if l1 + 1 == len(nums1):
                ans += nums2[l2 + 1]
                l2 += 1
            elif l2 + 1 == len(nums2):
                ans += nums1[l1 + 1]
                l1 += 1
            else:
                if nums2[l2 + 1] < nums1[l1 + 1]:
                    ans += nums2[l2 + 1]
                    l2 += 1
                else:
                    ans += nums1[l1 + 1]
                    l1 += 1
        
        return ans if total%2 == 1 else ans / 2.0
        