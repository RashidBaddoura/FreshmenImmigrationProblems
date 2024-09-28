class Solution(object):
    def isPerfectSquare(self, num):
        rounded_num = int(num**0.5) if num**0.5%1 < 0.5 else int(num**0.5) + 1
        if abs(num**0.5 - rounded_num) < 0.000001:
            return True
        else:
            return False