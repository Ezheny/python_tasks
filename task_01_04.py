coordx1 = int(input())
coordy1 = int(input())
coordx2 = int(input())
coordy2 = int(input())
coordx3 = int(input())
coordy3 = int(input())

deltax1 = (coordx2 - coordx1)
deltay1 = (coordy2 - coordy1)
deltax2 = (coordx3 - coordx1)
deltay2 = (coordy3 - coordy1)
deltax3 = (coordx3 - coordx2)
deltay3 = (coordy3 - coordy2)
if (deltax1*deltax2 + deltay1*deltay2 == 0) or \
    (deltax2*deltax3 + deltay2*deltay3 == 0) or \
    (deltax3*deltax1 + deltay3*deltay1 == 0):
    print('yes')
else:
    print('no')
