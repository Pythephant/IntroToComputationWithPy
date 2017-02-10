#define a funtion to calculate the root of the polynomial

def calRoot(num,degree = 2,eRate = 0.01):
    #abs() is in order to deal with the negative input nums
    epsilon = abs(num*eRate)    
    if type(degree) is not type(1) and degree % 2 == 0 and num < 0:
        print 'negative number for even degree!'
        return None
    guess = num/2.0
    count = 0
    while abs(guess**degree - num) >= epsilon:
        count += 1
        guess = guess - ((guess**degree) - num)/(degree*(guess**(degree -1)))
        print guess,'is the',degree,'degree root of',num,',calCounts:',count
    return guess

if __name__ == '__main__':
    print calRoot(1024,10,0.00001)
