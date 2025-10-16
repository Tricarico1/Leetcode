class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        
        print(dic)

        sorted_tup = sorted(dic.items(), key = lambda x: x[1], reverse = True)
        res = []
        for key, value in sorted_tup[:k]:
            res.append(key)
        return res


        