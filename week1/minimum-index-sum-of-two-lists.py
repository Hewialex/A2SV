class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        h = len(list1) + len(list2)
        res = []

        for i in range(len(list1)):
            for j in range (len(list2)):
                if list1[i] == list2[j]:
                    if (i+j) <= h:
                        if res == None:
                            res.append(list2[j])

                        elif h == i+j:
                            res.append(list2[j])
                        else:
                                 res=[]
                                 res.append(list2[j])
                        h = i+j
        return res