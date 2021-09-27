
#.............1...................
n = 5
daraja = lambda son : son ** n
print(daraja(2))

#.............2.................... 
juftmi = lambda son : son % 2 == 0
juftson = juftmi(2)
print(juftson)

#.............3.....................
toqmi = lambda son : son % 2 != 0
toqson = toqmi(3)
print(toqson)

#..............4....................
royhat1 = [1,2,3,4,5]
royhat2 = [6,7,8,9,10]

royhat_yegindisi = lambda royhat1, royhat2 : royhat1 + royhat2

yegindi = royhat_yegindisi(royhat1, royhat2)
print(yegindi)



