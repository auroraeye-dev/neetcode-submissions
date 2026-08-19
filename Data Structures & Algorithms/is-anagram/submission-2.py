class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=list(s)
        list2=list(t)
        dict1={}
        dict2={}
        for i in list1:
            if i not in dict1:
                dict1[i] = list1.count(i)
        for j in list2:
            if j not in dict2:
                dict2[j] = list2.count(j)

        if dict1==dict2:
            return True
        else:
            return False
        