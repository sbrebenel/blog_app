##date
import nltk
#nltk.download()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

hotel_rev = "4 star, REALLY? This was the worst movie I have ever watched. I wouldn't even give it one star."

stop_words = set(stopwords.words("english"))

words = word_tokenize(hotel_rev)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
#print(filtered_sentence)

sentance = ' '.join(filtered_sentence)
#print(sentance)

sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sentance)
print(ss)
#for k in ss:
#    print('{0}: {1}, '.format(k, ss[k]), end='')
#print()