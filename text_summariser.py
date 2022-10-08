# Importing required libraries
import nltk
from nltk.corpus import stopwords
import heapq

nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing data
para = "Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods. It helps determine how best to manipulate data sources to get the answers you need, making it easier for data scientists to discover patterns, spot anomalies, test a hypothesis, or check assumptions.EDA is primarily used to see what data can reveal beyond the formal modeling or hypothesis testing task and provides a provides a better understanding of data set variables and the relationships between them. It can also help determine if the statistical techniques you are considering for data analysis are appropriate. Originally developed by American mathematician John Tukey in the 1970s, EDA techniques continue to be a widely used method in the data discovery process today." # Template text
sentences = nltk.sent_tokenize(para)

words = []
for sentence in sentences:
  words+= nltk.word_tokenize(sentence)

stop_words = set(stopwords.words('english'))
# print(stopwords)
filtered_words = [w for w in words if not w.lower() in stop_words]
# print(filtered_words)

# Getting frequencies for each key word
word_frequencies = {}
for word in filtered_words:
  if ((word!='.') and (word!=',')):
    if word not in word_frequencies.keys():
      word_frequencies[word]=1
    else:
      word_frequencies[word]+=1

maximum_frequncy = max(word_frequencies.values())
weighted_frequency = {}

for word in word_frequencies.keys():
    weighted_frequency[word] = (word_frequencies[word]/maximum_frequncy)

print(weighted_frequency)

# Sentence scores based on key word frequency
sentence_score = {}
for sentence in sentences:
  word_list = nltk.word_tokenize(sentence.lower())
  for word in word_list:
    if word in weighted_frequency.keys():
              if len(sentence.split(' ')) < 30:
                  if sentence not in sentence_score.keys():
                      sentence_score[sentence] = weighted_frequency[word]
                  else:
                      sentence_score[sentence] += weighted_frequency[word]
print(sentence_score)

summary_sentences = heapq.nlargest(5, sentence_score, key=sentence_score.get)
summary = ' '.join(summary_sentences)
print(summary)
