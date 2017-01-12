# Part 1 Solution: 360154 is the length of the result
# iterationsLeft = 40
# inputString = "1113122113"

# Part 2 Solution: 5103798 is the length of the result
iterationsLeft = 50
inputString = "1113122113"

def say(phrase, lastValCount, lastVal):
    phrase = phrase + str(lastValCount) + str(lastVal)
    lastVal = currentVal
    lastValCount = 1

def checkValues(currentVal, lastValCount, lastVal, index):
    print "currentVal:" + str(currentVal) + ", lastVal:" + str(lastVal) + ", lastValCount:" + str(lastValCount) + ", index:" + str(index)

while (iterationsLeft > 0):
    lastVal = -1
    lastValCount = -1
    phrase = ""
    index = 1
    for currentVal in inputString:

        #checkValues(currentVal, lastValCount, lastVal, index)

        #Stage 1: Empty check
        if (lastVal == -1):
            lastVal = currentVal
            lastValCount = 1

        #Stage 2: Value check
        elif (currentVal == lastVal):
            lastValCount += 1

        elif (currentVal != lastVal):
            phrase = phrase + str(lastValCount) + str(lastVal)
            lastVal = currentVal
            lastValCount = 1

        #Stage 3: End check
        if (index == len(inputString)):
            phrase = phrase + str(lastValCount) + str(lastVal)
            lastVal = currentVal
            lastValCount = 1

        index += 1

    iterationsLeft -= 1
    inputString = phrase
    print len(phrase)
