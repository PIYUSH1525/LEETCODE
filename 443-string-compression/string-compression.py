class Solution:
    def compress(self, chars: List[str]) -> int:
        l= 0
        r = 0
        count  = 0
        while r < len(chars):
            current_char = chars[r]
            count= 0
            while (r < len(chars) and chars[r] == current_char):
                count+=1
                r+=1
            chars[l]  = current_char
            l +=1
            if count > 1:
                for dig in str(count):
                    chars[l] = dig
                    l += 1
        return l


            


                  



               