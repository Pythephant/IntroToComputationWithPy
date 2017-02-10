def largestOdd(numList):
    odds = findOdd(numList)
    maxOdd = findMax(odds)
    #print maxOdd
    return maxOdd

def findOdd(args):
    oddList = []
    for ele in args:
        if ele%2 == 1:
            oddList.append(ele)
    return oddList

def findMax(lst):
    if lst:
        maxEle = lst[0]
        for ele in lst:
            if maxEle < ele:
                maxEle = ele
        return maxEle
    else:
        return None

if __name__ == '__main__':
    ints = raw_input('please input the int to check the max odd(split by \',\'):')
    ints = ints.split(',')
    maxOdd = largestOdd([int(i) for i in ints])
    print 'in the main:',maxOdd
