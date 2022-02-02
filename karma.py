import datetime
import re
from tabulate import tabulate
import RedditAPI

namesOfSubs = ['CryptoCurrency','ethtrader','dankmemes','HydroHomies','Vechain']
subInfo = ''
previousKarma = []
currentKarma = []
difference = []

# read the file first 
def findSub(fileName,subName):
    file = open(fileName, 'r')
    with file as f:
        for line in file:
            if (line.find(subName) != -1):
                subInfo = line
                return subInfo

# get the sub name, post karma and comment karma
def extractInfo():
    list = []

    # name of the sub
    subName = re.findall(r'\[.*?\]', str(subInfo))
    list.append(subName[0][1:-1])

    # post and comment karma
    commentKarma = re.findall(r'\|.*', str(subInfo))
    toString = str(commentKarma[0][1:])
    afterSplit = toString.split(" | ")
    for i in range(len(afterSplit)):
        list.append(afterSplit[i])
    return list

# calculate the karma difference
def earnedKarma(pre, cur):
    list = []
    # append the sub name
    list.append(cur[0])

    # calculate and append the post karma
    calPostKarma = int(cur[1]) - int(pre[1])
    list.append(calPostKarma)
    
    # calculate and append the comment karma
    calCommentKarma = int(cur[2]) - int(pre[2])
    list.append(calCommentKarma)

    return list


# find the post and comment karma of different subs
for i in namesOfSubs:
    subInfo = findSub('./previousKarma.txt',i)
    previousKarma.append(extractInfo())

    subInfo = findSub('./currentKarma.txt',i)
    currentKarma.append(extractInfo())

# calculate the earned karma
for i in range(len(previousKarma)):
    karma = earnedKarma(previousKarma[i],currentKarma[i])
    difference.append(karma)

#console display
table = difference
print(tabulate(table, headers=["Reddit Subs","Post Karma", "Comment Karma"]))

# write a file
def createFile(difference):
    x = datetime.datetime.now()
    cTime = (x.strftime("%I-" +"%M-" + "%A"))
    f = open(cTime+".txt", "x")
    f.write(str(tabulate(table, headers=["Reddit Subs","Post Karma", "Comment Karma"])))
#createFile(difference)