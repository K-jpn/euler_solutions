'''
Problem01
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Step1
loop through 0 to 9
find the multiples of 3 or 5
add all
'''

def euler_01():
    answer = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            answer = answer + i
    print('The answer is %d' % answer)

if __name__ == '__main__':
    euler_01()
