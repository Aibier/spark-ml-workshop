def calculatePower(a, b):
    return pow(a, b)


def isMatch(key, myStr):
    return False if len(myStr) == 0 else key.lower() in myStr.lower()


def countElephant(key, myStr):
    count = myStr.count(key)
    return '"{}" occurs {} time(s) in "{}"'.format(key, count, myStr)


def evaluateSpeed(score):
    if score < 0:
        return 'score can not be negative.'

    if score <= 60:
        return 'Low speed'
    elif 61 < score <= 80:
        return 'Medium speed'
    else:
        return 'Fast speed'

