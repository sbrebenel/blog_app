from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

comment = "4 star, REALLY? This was the worst movie I have ever watched. I wouldn't even give it one star."

print(analyzer.polarity_scores(comment))
vector = analyzer.polarity_scores(comment)

score_sentiment = []

score_neg = vector['neg']*100 
print(score_neg)
score_sentiment.append(score_neg)

score_pos = vector['pos']*100
print(score_pos)
score_sentiment.append(score_pos)

score_neutral = vector['neu']*100
print(score_neutral)
score_sentiment.append(score_neutral)

score_comp = vector['compound']*100
print(score_comp)
score_sentiment.append(score_comp)


#structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
print(score_sentiment)

