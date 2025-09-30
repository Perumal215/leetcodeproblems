class Solution(object):
    def longestCommonPrefix(self, strs):
        str_arr_1=strs[0]
        for str_arr_2 in strs:
            while not str_arr_2.startswith(str_arr_1):
                str_arr_1 =str_arr_1[:-1]
                if not str_arr_1:
                    return ""
        return str_arr_1

        