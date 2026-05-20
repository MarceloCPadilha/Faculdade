#        #
#       ###
#      #####
#     #######
#    ##     ##
#   ###     ###
#  ####     ####
# #####     #####
#  ####     ####
#   ###     ###
#    ##     ##
#     #######
#      #####
#       ###
#        #

lenght = 4
gap = lenght + (lenght - 3)

top = [" " * (lenght - i + (gap // 2 + 1)) + "#" * (2 * i + 1)for i in range(lenght)]
mid = [" " * (lenght - i + 1) + ("#" * i) + (" " * gap) + ("#" * i)for i in range(2, lenght + 2)]

print("\n".join(top + mid + mid[-2::-1] + top[::-1]))
