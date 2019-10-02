def seperateValues(listParameter):
    spam = ''
    for i in listParameter:
        if((i + 1) == len(listParameter)):
            spam = str(spam) + ' and ' + str(listParameter[i])
        elif(spam == ''):
            spam = str(spam) + str(listParameter[i])
        else:
            spam = str(spam) +', ' + str(listParameter[i])
    return spam

eggs = [0,1,2,3,4,5,6,7,8,9]
print(seperateValues(eggs))
