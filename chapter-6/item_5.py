def staircase(n):
    if n>1:
        return '$'*(n-1) + '#'*() + '\n' + str(staircase(n-1))

print(staircase(int(input("Enter Input : "))))



# ______#
# _____##
# ____###
# ___####
# __#####
# _######
# #######