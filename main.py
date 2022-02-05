from Exercise import calculatePower, isMatch, countElephant, evaluateSpeed

# What is 8 to the power 4
print(calculatePower(8, 4))
txt = "Split this string"
print(txt.split())

planet = 'Earth'
diameter = 12742
print('The diameter of {} is {} kilometers.'.format(planet, diameter))

# d. print word target
mylist = [1, 2, [3, 4], [5, [100, 200, ['target']], 23, 11], 1, 7]
print(mylist[3][1][2][0])

# e. print the world 'hello'.
my_dic = {
    'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]
}
print(my_dic['k1'][3]['tricky'][3]['target'][3])


# f. elephant contains in given string.
print(isMatch('elephant', 'Test Elephant'))
print(isMatch('elephant', 'Test'))

# g. counts the number of times the word "elephant"
testStr = "This looks like elephant, but it is not elephant."
print(countElephant('elephant', testStr))

# h. evaluateSpeed
print(evaluateSpeed(89))
