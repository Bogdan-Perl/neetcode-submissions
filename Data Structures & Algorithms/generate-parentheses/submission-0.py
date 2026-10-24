class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        #two choices, eaither add an opening or add a closing
        # if and only if opening < closing we can add a closing
        # once opening == closing == n we end
        def backtrack(curr, opn, cls):
            if opn == cls == 0:
                res.append(curr[::])
            
            if opn:
                backtrack(curr + "(", opn - 1, cls)
            if opn < cls:
                backtrack(curr + ")", opn, cls - 1)
            

        backtrack("", n, n)
        return res
            



            
            
            