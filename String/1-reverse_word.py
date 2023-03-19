# Reverse words in a given string
def reverseWord(S):
    S = S.split(".")
    n = len(S)
    l = 0
    r = n-1
    mid = (l+r) // 2
    while l <= mid:
        S[l],S[r] = S[r],S[l]
        l+=1
        r-=1
    new_str = None
    for i in range(len(S)):
        if new_str is not None:
            new_str=new_str+"."+S[i]
        else:
            new_str = S[i]
    return new_str


inp_S = "i.like.this.program.very.much"
res = reverseWord(inp_S)
print(res)