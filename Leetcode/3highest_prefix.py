def longestCommonPrefix(strs):
    prfx=strs[0]
    for i in range(len(strs)):
        new_prfx = ""
        len_prfx=len(prfx)
        len_str=len(strs[i])
        sm = min(len_prfx, len_str)
        for j in range(sm):
            if strs[i][j] == prfx[j]:
                new_prfx+=prfx[j]
            else:
                break
        prfx=new_prfx
    return new_prfx

# strs=["flower","floe","flight","doe"]
# strs=["flower","flew",]

# prfx=strs[0]
# for i in range(len(strs)):
#     new_prfx = ""
#     len_prfx=len(prfx)
#     len_str=len(strs[i])
#     sm = min(len_prfx, len_str)
#     for j in range(sm):
#         if strs[i][j] == prfx[j]:
#             new_prfx+=prfx[j]
#     prfx=new_prfx
# print(new_prfx)



print(longestCommonPrefix(["flower","flow","flight"]))