# blog_app

WebApp for analyze comments from blog or Twitter

Requirement:

- MySQL installed with 2 tables (articles and comments linked by foreign key)
- Data inserted in both tables

Actions (most of them are present in article_1.js):

- Most Common Words - generate graph based on the most common words used in comments for one article;
- Sentiment Analyze General - generate 3 graphs based on the words used in comments with 3 different algorithms : TheySay Preceive, Vader, Text Processing
- Entity Analyze - words which belong to 5 different category : People, Organizations, Places, Date/Time, Others
- Emotion Analyze - generate 2 graphs based on the words used in comments with 2 different algorithms : Indico, TheySay Preceive
- Generate Comment - Insert 10 comments from comments.txt file