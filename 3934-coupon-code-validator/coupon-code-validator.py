class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ll = len(code)
        combo = []
        for ii in range (ll):
            if len(code[ii]) == 0:
                continue
            if businessLine[ii] not in ["electronics" , "grocery","pharmacy","restaurant"]:
                continue
            if isActive[ii]:
                llc = len(code[ii])
                flag = True
                for jj in range(llc):
                    if code[ii][jj] not in "01234567890_" \
                        and code[ii][jj] not in "abcdefghijklmnopqrstuvwxyz"\
                        and code[ii][jj] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        flag = False
                        break
                if flag:
                    combo.append([businessLine[ii],code[ii]])
        combo.sort()
        res = [combo[ii][1] for ii in range(len(combo))]
        return res