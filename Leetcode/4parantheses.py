def isValid(s: str):
    stack_opening_bracket=[]
    pairs = {")":"(","]":"[","}":"{"}

    for brac in s:
        if brac in ["(","[","{"]:
            stack_opening_bracket.append(brac)
        elif brac in [")","]","}"]:
            if len(stack_opening_bracket)==0:
                return False
            else:
                print("Inside close brac else")
                if stack_opening_bracket.pop()==pairs[brac]:
                    1==1
                else:
                    return False
    if len(stack_opening_bracket)>0:
        return False
    return True




print(isValid("{{}"))