n = 5
for i in range(1,n+1):
    spc = n - i
    star = 2 * i -1 # to keep pyramid symmetrical
    print(" "* spc + "*" * star)

#     *
#    ***
#   *****
#  *******
# *********