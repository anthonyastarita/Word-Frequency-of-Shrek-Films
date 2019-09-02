import nltk
from nltk.corpus import stopwords 
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words('english'))
stop_words.add('I')
stop_words.add('92s')
stop_words.add('f1')
stop_words.add('SHREK')
stop_words.add('1')
stop_words.add('85')
stop_words.add('92t')

tokenizer = RegexpTokenizer(r'\w+')

file = open('ShrekMovies.txt', 'r')

ShrekScript = file.read()

ShrekScriptTokenized= tokenizer.tokenize(ShrekScript)

fdist = nltk.FreqDist(ShrekScriptTokenized)

yAxis = []
xAxis = list()

for word, frequency in fdist.most_common(50):
    if word not in stop_words:
        xAxis.append(word)
        yAxis.append(frequency)


y_pos = np.arange(len(xAxis))
plt.bar(y_pos, yAxis)
plt.xticks(y_pos, xAxis, color='orange')
plt.yticks(color='orange')
plt.show()
