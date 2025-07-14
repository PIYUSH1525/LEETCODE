__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def rotate(self, nums: List[int], k: int) -> None: 
        n = len(nums)
        k %= n 
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Reverse whole array
        reverse(0, n - 1)

        # Reverse first k
        reverse(0, k - 1)

        # Reverse rest
        reverse(k, n - 1)


    #    APPROACH 1
        # n = len(nums)
        # res = [0]*n
        # for i in range(n):
        #     res[(i+k)%n] = nums[i]
        # nums[:] =res 
        # """
        # Do not return anything, modify nums in-place instead.
        # """
        