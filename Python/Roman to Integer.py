class Solution(object):
    def romanToInt(self, s):
        dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000

        }
        result=0;
        prev = 0;
        for i in s[::-1]: 
            curr=dict[i];
            if(prev > curr ):
                result = result - dict[i];
            else:
                result = result + dict[i];
            prev=curr;
        return result;