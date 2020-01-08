class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_to_str = str(x)
        temp_str = []
        j = len(num_to_str)-1
        while j>=0:
            temp_str.append(num_to_str[j])
            j = j -1
        for i in range(0,len(num_to_str)):
            if num_to_str[i] == temp_str[i]:
                palin = True
            else:
                palin = False
                break
        return palin