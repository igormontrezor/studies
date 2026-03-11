class Solution:
    def longestCommonPrefix(self, string_list):
        prefix = ""
        for count in range(0,len(string_list[0])):
            char_reference = string_list[0][count] #0/0 first letter or first character of first string
            for index in range(1,len(string_list)):
                if count >= len(string_list[index]) or string_list[index][count] != char_reference:
                    return prefix
            prefix += char_reference
        return prefix
string_list = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(string_list))
