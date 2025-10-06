class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic1={}
        dic2={}
        for word in words1:
            if word in dic1:
                dic1[word]+=1
            else:
                dic1[word]=1
        
        for word in words2:
            if word in dic2:
                dic2[word]+=1
            else:
                dic2[word]=1       

        count = 0
        for word in dic1:
            if dic1[word] == 1 and dic2.get(word,0)==1:
                count+=1
        return count
        