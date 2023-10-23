'''
Draw pattern as mentioned below :
*
**
***
****
*****

'''

for x in range(1,6):
    for y in range(1,6):
        if y<=x:
            print('*', end='')
        else:
            print('',end='')
    print('')