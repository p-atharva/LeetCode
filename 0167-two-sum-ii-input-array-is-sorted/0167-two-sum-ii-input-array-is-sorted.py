class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1

        while lp < rp:
            sumnumbers = numbers[lp] + numbers[rp]
            if sumnumbers > target:
                rp -= 1
            elif sumnumbers < target:
                lp += 1
            else:
                return [lp+1, rp+1]
        