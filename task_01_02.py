plates = int(input())
wash = float(input())
while wash > 0 and plates > 0:
    wash -= 0.5
    plates -= 1
if wash <= 0 and plates > 0:
    print('Моющее средство закончилось. Осталось ' + str(plates) + ' тарелок')
elif plates == 0 and wash >= 0:
    print('Все тарелки вымыты. Осталось ' + str(wash) + ' ед. моющего средства')
else:
    print('Все тарелки вымыты, моющее средство закончилось')
