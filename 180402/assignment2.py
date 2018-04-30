from math import *
import matplotlib.pyplot as plt
from numpy import *
from nltk.book import *
from pandas import *
import matplotlib.lines as mlines


def isWord(word):
    if (ord(word[0]) >= 48 and ord(word[0]) <= 57) or (ord(word[0]) >= 97 and ord(word[0]) <= 122):
        return True
    else:
        return False

#eliminate case sensitivity
refined_text = [x.lower() for x in text1]
#elminate Paragraph mark
refined_text1 = [x for x in refined_text if isWord(x)]

total_word = len(refined_text1)
word_set = set(refined_text1)
word_set_len = len(word_set)

#average word frequency
avg_word_fre = total_word / word_set_len

#word frequnct array
word_fre = zeros(word_set_len, dtype='int')
word_set_list = list(word_set)

#count word frequency
for i in range(0, total_word):
    word = refined_text1[i]
    word_index = word_set_list.index(word)
    word_fre[word_index] += 1
    
table = DataFrame(Series(word_fre, word_set_list), columns=['word_fre'])

table = table.sort_values('word_fre', ascending=False)
#make rank
rank = [x for x in range(1, table.size + 1)]

table['rank'] = rank

#log values
log_rank = log(table['rank'].tolist())
log_word_fre = log(table['word_fre'].tolist())

#linear regression
m, c = polyfit(log_rank, log_word_fre, 1)
fit_word_fre = log_rank*m + c

#draw graph
plt.figure(figsize=(20,10))
plt.xlabel('log(rank)', fontsize = 40)
plt.ylabel('log(word_fre)', fontsize = 40)
plt.xticks(fontsize = 35)
plt.yticks(fontsize = 35)

raw_line = mlines.Line2D([], [], color='red',
                          markersize=15, label='Raw Data')
fit_line = mlines.Line2D([], [], color='blue',
                          markersize=15, label='Fit Data')
plt.legend(handles=[raw_line, fit_line], fontsize= 30)

plt.plot(log_rank, log_word_fre, "r")
plt.plot(log_rank, fit_word_fre, 'b')
plt.show()

#calculate correlation coefficient
n = len(log_rank)

r = ( n*sum(log_rank*log_word_fre) - sum(log_rank)*sum(log_word_fre) ) / sqrt ( n*sum(log_rank*log_rank) - sum(log_rank)*sum(log_rank)) / sqrt ( n*sum(log_word_fre*log_word_fre) - sum(log_word_fre)*sum(log_word_fre) ) 
