import re
import itertools
result = []
''' opening a file from my file location '''
hand = open('C:\\Users\\Shivasai\\Documents\\regex_sum_actualTest_193741.txt')
for line in hand:
    s = re.findall('\d+', line)
    if s:
	result.append(s)
merged = list(itertools.chain(*result))
convertToInt = map(int, merged)
print len(convertToInt)
print convertToInt
print sum(convertToInt)