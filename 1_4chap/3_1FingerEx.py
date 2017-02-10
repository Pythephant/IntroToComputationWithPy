

if __name__ == '__main__':
    num = int(raw_input('Enter a integer:'))
    #as prerequisited  0<pwr<6
    pwr = 1
    isExist = False
    while pwr < 6:
        for i in range(-abs(num),abs(num)+1):
            if i**pwr == num:
                print 'root:',i,',power:',pwr,'is',num
                isExist = True
        pwr = pwr + 1
    if not isExist:
        print 'no root and pwr exist of',num
