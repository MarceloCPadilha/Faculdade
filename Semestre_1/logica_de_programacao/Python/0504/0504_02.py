   ##
  ####
 ######
########
 ######
  ####
   ##

lenght = 4

top = [((" " * (lenght - i)) + ("##" * i)) for i in range(1, lenght)]

# print("{}\n{}".format("\n".join(top),"\n".join(top[-2::-1])))
print("\n".join(top + top[-2::-1]))
