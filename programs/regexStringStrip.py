#! python3
#regexStringStrip.py - Searching for white spaces and removing them.
import re
def newStrip(text, stringRemove):

    if stringRemove != None:
        regexRemoveCharacter = re.compile(r'['+ str(stringRemove) + ']')
        text = regexRemoveCharacter.sub('',text)
        return text
    else:
        regexRemoveWhitespacesStartEnd = re.compile(r'{\s*}(.*?){\s*}')
        text = regexRemoveWhitespacesStartEnd.search(text)
        print(text)
        return text
    
text = ' Test Test Test Test '
text1 = newStrip(text,None)
text2 = newStrip(text,'t')
print(text1)
print(text2)
