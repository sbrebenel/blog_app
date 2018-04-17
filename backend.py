#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import cherrypy
import simplejson
import json
import os
import datetime
import time
import MySQLdb
import collections
import re
from jinja2 import Environment, FileSystemLoader
import urllib.parse
import urllib.request
import indicoio
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

indicoio.config.api_key = 'XXXXXX'

root_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(root_dir, 'app')
lib_dir = os.path.join(root_dir, 'lib')

env_jinja = Environment(loader=FileSystemLoader(app_dir),trim_blocks=True)
stop_words_global = ["hasn't", 'being', 'both', 'theirs', 'whom', 'weren', 'ours', 'so', 'don', 'hadn', 'myself', 'you',
             'are', "mustn't", 'herself', 'an', 'itself', 'than', 'those', 'at', 'what', 'up', 'him', "she's",
             'wouldn', 'of', 'all', 'why', 'now', 'been', 'against', 'she', 'doesn', 'after', 'them', 'too',
             'aren', 'under', "shan't", 'won', 'am', 'ain', "you've", 'about', 'through', 'once', 'does', 'did',
             'own', 'until', 'over', 'out', 'any', 'some', "isn't", 'me', "you're", 've', 'd', 'further',
             'this', 'where', 'ourselves', 'their', 'couldn', 'they', 'that', "you'll", 'such', 'our', 'have',
             'm', 'he', 'same', 'when', 'for', "aren't", 'then', 'nor', "should've", "wouldn't", 'because',
             "haven't", 'be', 'my', 'o', 'the', 'her', 'mightn', 'wasn', 'didn', 'isn', "wasn't", 'was', 'off',
             "couldn't", "mightn't", 'we', 'his', 'while', 'by', 'mustn', 'i', 'can', 'to', 're', 'who', 'has',
             'doing', 'only', 'below', 'into', 'here', "didn't", 'hers', 'y', 't', 'yourself', 'or', 'which',
             'how', 's', 'if', 'before', "weren't", 'between', 'ma', 'your', 'll', 'haven', 'should', 'most',
             'again', 'it', "that'll", 'were', 'its', 'will', "needn't", 'a', "won't", 'is', 'yourselves',
             'shan', "it's", 'very', 'in', 'more', 'do', 'not', 'on', 'there', 'each', 'hasn', 'themselves',
             "hadn't", 'from', 'down', 'had', "shouldn't", "don't", 'no', 'but', 'above', 'with', 'other',
             'needn', 'and', "doesn't", 'yours', 'just', 'during', 'having', 'shouldn', 'himself', 'these',
             'as', "you'd", 'few', "one", "really"]

class Home(object):

    @cherrypy.expose()
    def index(self):
        template = env_jinja.get_template('index.html')
        return template.render(comm_art_1=self.get_number_comments_one(), comm_art_2=self.get_number_comments_two(),
                               comm_art_3=self.get_number_comments_three(), comm_art_4=self.get_number_comments_four(),
                               comm_art_5=self.get_number_comments_five(), comm_art_6=self.get_number_comments_six(),
                               comm_art_7=self.get_number_comments_seven(), comm_art_8=self.get_number_comments_eight(),
                               comm_art_9=self.get_number_comments_nine())

    #template for Article ONE
    @cherrypy.expose()
    def article_0(self):
        template = env_jinja.get_template('article_0.html')
        return template.render(article_one=self.get_article_one(), numbers_comment_one=self.get_number_comments_one(),
                               comment_author_one=self.get_comments_one())

    def get_article_one(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='1'")
        result = c.fetchall()
        c.close()
        article_one = result
        return article_one

    def get_number_comments_one(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        numbers_comment_one = result[0][0]
        return numbers_comment_one

    def get_comments_one(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        comments_one = result
        return comments_one

    # template for Article TWO
    @cherrypy.expose()
    def article_1(self):
        template = env_jinja.get_template('article_1.html')
        return template.render(article_two=self.get_article_two(), numbers_comment_two=self.get_number_comments_two(),
                               comment_author_two=self.get_comments_two())

    def get_article_two(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='2'")
        result = c.fetchall()
        c.close()
        article_two = result
        return article_two

    def get_number_comments_two(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='2'")
        result = c.fetchall()
        c.close()
        numbers_comment_two = result[0][0]
        return numbers_comment_two

    def get_comments_two(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='2'")
        result = c.fetchall()
        c.close()
        comments_two = result
        return comments_two

    # template for Article THREE
    @cherrypy.expose()
    def article_2(self):
        template = env_jinja.get_template('article_2.html')
        return template.render(article_three=self.get_article_three(),
                               numbers_comment_three=self.get_number_comments_three(),
                               comment_author_three=self.get_comments_three())

    def get_article_three(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='3'")
        result = c.fetchall()
        c.close()
        article_three = result
        return article_three

    def get_number_comments_three(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='3'")
        result = c.fetchall()
        c.close()
        numbers_comment_three = result[0][0]
        return numbers_comment_three

    def get_comments_three(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='3'")
        result = c.fetchall()
        c.close()
        comments_three = result
        return comments_three

    # template for Article FOUR
    @cherrypy.expose()
    def article_3(self):
        template = env_jinja.get_template('article_3.html')
        return template.render(article_four=self.get_article_four(),numbers_comment_four=self.get_number_comments_four(),
                               comment_author_four=self.get_comments_four())

    def get_article_four(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='4'")
        result = c.fetchall()
        c.close()
        article_four = result
        return article_four

    def get_number_comments_four(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='4'")
        result = c.fetchall()
        c.close()
        numbers_comment_four = result[0][0]
        return numbers_comment_four

    def get_comments_four(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='4'")
        result = c.fetchall()
        c.close()
        comments_four = result
        return comments_four

    # template for Article FIVE
    @cherrypy.expose()
    def article_4(self):
        template = env_jinja.get_template('article_4.html')
        return template.render(article_five=self.get_article_five(),numbers_comment_five=self.get_number_comments_five(),
                               comment_author_five=self.get_comments_five())

    def get_article_five(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='5'")
        result = c.fetchall()
        c.close()
        article_five = result
        return article_five

    def get_number_comments_five(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='5'")
        result = c.fetchall()
        c.close()
        numbers_comment_five = result[0][0]
        return numbers_comment_five

    def get_comments_five(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='5'")
        result = c.fetchall()
        c.close()
        comments_five = result
        return comments_five

    # template for Article SIX
    @cherrypy.expose()
    def article_5(self):
        template = env_jinja.get_template('article_5.html')
        return template.render(article_six=self.get_article_six(),numbers_comment_six=self.get_number_comments_six(),
                               comment_author_six=self.get_comments_six())

    def get_article_six(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='6'")
        result = c.fetchall()
        c.close()
        article_six = result
        return article_six

    def get_number_comments_six(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='6'")
        result = c.fetchall()
        c.close()
        numbers_comment_six = result[0][0]
        return numbers_comment_six

    def get_comments_six(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='6'")
        result = c.fetchall()
        c.close()
        comments_six = result
        return comments_six

    # template for Article SEVEN (7)
    @cherrypy.expose()
    def article_6(self):
        template = env_jinja.get_template('article_6.html')
        return template.render(article_seven=self.get_article_seven(),
                               numbers_comment_seven=self.get_number_comments_seven(),
                               comment_author_seven=self.get_comments_seven())

    def get_article_seven(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='7'")
        result = c.fetchall()
        c.close()
        article_seven = result
        return article_seven

    def get_number_comments_seven(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='7'")
        result = c.fetchall()
        c.close()
        numbers_comment_seven = result[0][0]
        return numbers_comment_seven

    def get_comments_seven(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='7'")
        result = c.fetchall()
        c.close()
        comments_seven = result
        return comments_seven

    # template for Article EIGHT (8)
    @cherrypy.expose()
    def article_7(self):
        template = env_jinja.get_template('article_7.html')
        return template.render(article_eight=self.get_article_eight(),
                               numbers_comment_eight=self.get_number_comments_eight(),
                               comment_author_eight=self.get_comments_eight())

    def get_article_eight(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='8'")
        result = c.fetchall()
        c.close()
        article_eight = result
        return article_eight

    def get_number_comments_eight(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='8'")
        result = c.fetchall()
        c.close()
        numbers_comment_eight = result[0][0]
        return numbers_comment_eight

    def get_comments_eight(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='8'")
        result = c.fetchall()
        c.close()
        comments_eight = result
        return comments_eight

    # template for Article NINE
    @cherrypy.expose()
    def article_8(self):
        template = env_jinja.get_template('article_8.html')
        return template.render(article_nine=self.get_article_nine(),numbers_comment_nine=self.get_number_comments_nine(),
                               comment_author_nine=self.get_comments_nine())

    def get_article_nine(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Writer,Date,Name,Body FROM articles WHERE ID='9'")
        result = c.fetchall()
        c.close()
        article_nine = result
        return article_nine

    def get_number_comments_nine(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Count(*) FROM comments WHERE ArtID='9'")
        result = c.fetchall()
        c.close()
        numbers_comment_nine = result[0][0]
        return numbers_comment_nine

    def get_comments_nine(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Name,Date,Comment,ID FROM comments WHERE ArtID='9'")
        result = c.fetchall()
        c.close()
        comments_nine = result
        return comments_nine

    @cherrypy.expose()
    def get_articles_index(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute('SELECT Name,Writer,Date FROM articles')
        result = c.fetchall()
        c.close()
        articles = []
        for i in result:
            articles.append(i)
        return json.dumps(articles,indent=4, sort_keys=True, default=str).encode('utf-8')

    # Method for post comments into article 1
    @cherrypy.expose()
    def post_comment_one(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*','*')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 1)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 2
    @cherrypy.expose()
    def post_comment_two(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 2)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 3
    @cherrypy.expose()
    def post_comment_three(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 3)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 4
    @cherrypy.expose()
    def post_comment_four(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 4)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 5
    @cherrypy.expose()
    def post_comment_five(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 5)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 6
    @cherrypy.expose()
    def post_comment_six(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 6)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 7
    @cherrypy.expose()
    def post_comment_seven(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 7)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 8
    @cherrypy.expose()
    def post_comment_eight(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 8)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # Method for post comments into article 9
    @cherrypy.expose()
    def post_comment_nine(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        com_name = kwargs['com_name']
        com_email = kwargs['com_email']
        com_text = kwargs['com_text']

        print(com_name)
        print(com_email)
        print(com_text)

        com_final = com_text.replace('*', '')
        print(com_final)

        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        id = c.lastrowid
        print(id)
        add_comments = ("INSERT INTO comments "
                        "(ID, Name, Email, Comment, ArtID) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_comments = (id, com_name, com_email, com_final.encode('utf-8'), 9)
        c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 1
    @cherrypy.expose()
    def get_most_common_words_one(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".","")
            word = word.replace(",","")
            word = word.replace(":","")
            word = word.replace("\"","")
            word = word.replace("!","")
            word = word.replace("â€œ","")
            word = word.replace("â€˜","")
            word = word.replace("*","")
            word = word.replace("'","")
            word = word.replace("=","")
            word = word.replace("+","")
            word = word.replace("-","")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10),indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 2
    @cherrypy.expose()
    def get_most_common_words_two(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='2'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 3
    @cherrypy.expose()
    def get_most_common_words_three(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='3'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 4
    @cherrypy.expose()
    def get_most_common_words_four(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='4'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 5
    @cherrypy.expose()
    def get_most_common_words_five(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='5'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 6
    @cherrypy.expose()
    def get_most_common_words_six(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='6'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 7
    @cherrypy.expose()
    def get_most_common_words_seven(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='7'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 8
    @cherrypy.expose()
    def get_most_common_words_eight(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='8'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # MOST COMMON WORDS FOR COMMENTS FROM ARTICLE 9
    @cherrypy.expose()
    def get_most_common_words_nine(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='9'")
        result = c.fetchall()
        c.close()
        comments_body = []
        for i in result:
            comments_body.append(i[0])
        comments_body_str = ''.join(comments_body)

        stopwords = stop_words_global

        comments_body_str = comments_body_str.lower()
        comments_body_str = ''.join([i for i in comments_body_str if not i.isdigit()])
        print(comments_body_str)

        reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', comments_body_str))
        wordcount = {}
        for word in reduced:
            word = word.replace(".", "")
            word = word.replace(",", "")
            word = word.replace(":", "")
            word = word.replace("\"", "")
            word = word.replace("!", "")
            word = word.replace("â€œ", "")
            word = word.replace("â€˜", "")
            word = word.replace("*", "")
            word = word.replace("'", "")
            word = word.replace("=", "")
            word = word.replace("+", "")
            word = word.replace("-", "")
            word = word.replace("@", "")
            word = word.replace("$", "")
            word = word.replace("(", "")
            word = word.replace(")", "")
            word = word.replace("%", "")
            word = word.replace("^", "")
            word = word.replace("#", "")

            if word not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(10):
            print(word, ": ", count)
        return json.dumps(word_counter.most_common(10), indent=4, sort_keys=True, default=str).encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 1
    @cherrypy.expose()
    def get_sentiment_analyze_article_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        comments_1 = result
        score_sentiment = []

        for sentence in comments_1:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 1
    @cherrypy.expose()
    def get_comments_article_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        numbers_comment_1 = result
        return json.dumps(numbers_comment_1).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 1
    @cherrypy.expose()
    def get_emotion_analyze_article_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        comments_1 = result
        score_emotion = []

        for sentence in comments_1:
            print(sentence)
            indicoio.config.api_key = 'XXXXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 1
    @cherrypy.expose()
    def generate_comments_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 1)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 2
    @cherrypy.expose()
    def get_sentiment_analyze_article_2(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='2'")
        result = c.fetchall()
        c.close()
        comments_2 = result
        score_sentiment = []

        for sentence in comments_2:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 2
    @cherrypy.expose()
    def get_comments_article_2(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='2'")
        result = c.fetchall()
        c.close()
        numbers_comment_2 = result
        return json.dumps(numbers_comment_2).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 2
    @cherrypy.expose()
    def get_emotion_analyze_article_2(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='2'")
        result = c.fetchall()
        c.close()
        comments_2 = result
        score_emotion = []

        for sentence in comments_2:
            print(sentence)
            indicoio.config.api_key = 'XXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 2
    @cherrypy.expose()
    def generate_comments_2(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 2)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 3
    @cherrypy.expose()
    def get_sentiment_analyze_article_3(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='3'")
        result = c.fetchall()
        c.close()
        comments_3 = result
        score_sentiment = []

        for sentence in comments_3:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 3
    @cherrypy.expose()
    def get_comments_article_3(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='3'")
        result = c.fetchall()
        c.close()
        numbers_comment_3 = result
        return json.dumps(numbers_comment_3).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 3
    @cherrypy.expose()
    def get_emotion_analyze_article_3(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='3'")
        result = c.fetchall()
        c.close()
        comments_3 = result
        score_emotion = []

        for sentence in comments_3:
            print(sentence)
            indicoio.config.api_key = 'XXXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 3
    @cherrypy.expose()
    def generate_comments_3(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 3)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 4
    @cherrypy.expose()
    def get_sentiment_analyze_article_4(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='4'")
        result = c.fetchall()
        c.close()
        comments_4 = result
        score_sentiment = []

        for sentence in comments_4:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 3
    @cherrypy.expose()
    def get_comments_article_4(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='4'")
        result = c.fetchall()
        c.close()
        numbers_comment_4 = result
        return json.dumps(numbers_comment_4).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 4
    @cherrypy.expose()
    def get_emotion_analyze_article_4(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='4'")
        result = c.fetchall()
        c.close()
        comments_4 = result
        score_emotion = []

        for sentence in comments_4:
            print(sentence)
            indicoio.config.api_key = 'XXXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 4
    @cherrypy.expose()
    def generate_comments_4(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 4)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 5
    @cherrypy.expose()
    def get_sentiment_analyze_article_5(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='5'")
        result = c.fetchall()
        c.close()
        comments_5 = result
        score_sentiment = []

        for sentence in comments_5:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 5
    @cherrypy.expose()
    def get_comments_article_5(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='5'")
        result = c.fetchall()
        c.close()
        numbers_comment_5 = result
        return json.dumps(numbers_comment_5).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 5
    @cherrypy.expose()
    def get_emotion_analyze_article_5(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='5'")
        result = c.fetchall()
        c.close()
        comments_5 = result
        score_emotion = []

        for sentence in comments_5:
            print(sentence)
            indicoio.config.api_key = 'XXXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 5
    @cherrypy.expose()
    def generate_comments_5(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 5)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 6
    @cherrypy.expose()
    def get_sentiment_analyze_article_6(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='6'")
        result = c.fetchall()
        c.close()
        comments_6 = result
        score_sentiment = []

        for sentence in comments_6:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 6
    @cherrypy.expose()
    def get_comments_article_6(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='6'")
        result = c.fetchall()
        c.close()
        numbers_comment_6 = result
        return json.dumps(numbers_comment_6).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 6
    @cherrypy.expose()
    def get_emotion_analyze_article_6(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='6'")
        result = c.fetchall()
        c.close()
        comments_6 = result
        score_emotion = []

        for sentence in comments_6:
            print(sentence)
            indicoio.config.api_key = 'XXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 6
    @cherrypy.expose()
    def generate_comments_6(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 6)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 7
    @cherrypy.expose()
    def get_sentiment_analyze_article_7(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='7'")
        result = c.fetchall()
        c.close()
        comments_7 = result
        score_sentiment = []

        for sentence in comments_7:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 7
    @cherrypy.expose()
    def get_comments_article_7(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='7'")
        result = c.fetchall()
        c.close()
        numbers_comment_7 = result
        return json.dumps(numbers_comment_7).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 7
    @cherrypy.expose()
    def get_emotion_analyze_article_7(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='7'")
        result = c.fetchall()
        c.close()
        comments_7 = result
        score_emotion = []

        for sentence in comments_7:
            print(sentence)
            indicoio.config.api_key = 'XXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 7
    @cherrypy.expose()
    def generate_comments_7(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 7)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 8
    @cherrypy.expose()
    def get_sentiment_analyze_article_8(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='8'")
        result = c.fetchall()
        c.close()
        comments_8 = result
        score_sentiment = []

        for sentence in comments_8:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 8
    @cherrypy.expose()
    def get_comments_article_8(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='8'")
        result = c.fetchall()
        c.close()
        numbers_comment_8 = result
        return json.dumps(numbers_comment_8).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 8
    @cherrypy.expose()
    def get_emotion_analyze_article_8(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='8'")
        result = c.fetchall()
        c.close()
        comments_8 = result
        score_emotion = []

        for sentence in comments_8:
            print(sentence)
            indicoio.config.api_key = 'XXXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 8
    @cherrypy.expose()
    def generate_comments_8(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 8)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    # SENTIMENT ANALYSE FOR COMMENTS FROM ARTICLE 9
    @cherrypy.expose()
    def get_sentiment_analyze_article_9(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='9'")
        result = c.fetchall()
        c.close()
        comments_9 = result
        score_sentiment = []

        for sentence in comments_9:
            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            u = urllib.request.urlopen("http://text-processing.com/api/sentiment/", data)

            response = u.read()
            analyze_sentiment = json.loads(response)
            print(analyze_sentiment)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['probability']['neg'], 4) * 100)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['probability']['pos'], 4) * 100)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['probability']['neutral'], 4) * 100)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SEND COMMENTS FOR ENTITY ANALYSE FROM ARTICLE 9
    @cherrypy.expose()
    def get_comments_article_9(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='9'")
        result = c.fetchall()
        c.close()
        numbers_comment_9 = result
        return json.dumps(numbers_comment_9).encode('utf-8')

    # EMOTION ANALYSE FOR COMMENTS FROM ARTICLE 9
    @cherrypy.expose()
    def get_emotion_analyze_article_9(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='9'")
        result = c.fetchall()
        c.close()
        comments_9 = result
        score_emotion = []

        for sentence in comments_9:
            print(sentence)
            indicoio.config.api_key = 'XXXX'
            analyze_emotion = indicoio.emotion(str(sentence))

            print(analyze_emotion)

            score_anger = '{:0.2f}'.format(round(analyze_emotion['anger'], 5) * 100)
            print(score_anger)
            score_emotion.append(score_anger)

            score_surprise = '{:0.2f}'.format(round(analyze_emotion['surprise'], 5) * 100)
            print(score_surprise)
            score_emotion.append(score_surprise)

            score_sadness = '{:0.2f}'.format(round(analyze_emotion['sadness'], 5) * 100)
            print(score_sadness)
            score_emotion.append(score_sadness)

            score_fear = '{:0.2f}'.format(round(analyze_emotion['fear'], 5) * 100)
            print(score_fear)
            score_emotion.append(score_fear)

            score_joy = '{:0.2f}'.format(round(analyze_emotion['joy'], 5) * 100)
            print(score_joy)
            score_emotion.append(score_joy)

            # structure of array score_emotion [0] - anger score [1] - surprise score [2] - sadness score
            # [3] - sadness score [4] - fear score [5] - joy score
            print(score_emotion)

        return json.dumps(score_emotion).encode('utf-8')

    # Method for generate comments into ARTICLE 9
    @cherrypy.expose()
    def generate_comments_9(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()

        lines = open('comments.txt', 'r').read().splitlines()
        for index, item in enumerate(lines):
            id = c.lastrowid
            print(id)
            com_name = "test_username_"+str(index+1)
            com_email = "test_email_"+str(index+1)+"@abc.com"
            com_final = item.encode('utf-8')
            no_comm = index+1
            add_comments = ("INSERT INTO comments "
                            "(Name, Email, Comment, ArtID) "
                            "VALUES (%s, %s, %s, %s)")
            data_comments = (com_name, com_email, com_final, 9)
            c.execute(add_comments, data_comments)
        db.commit()
        c.close()

        c = db.cursor()
        c.execute("SET @count = 0; UPDATE `comments` SET `comments`.`id` = @count:= @count + 1;")
        c.close()
        db.commit()

        return json.dumps("Success! " + str(no_comm) + " comments has been inserted!").encode('utf-8')

    @staticmethod
    def get_comm_art_1(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="blog")
        c = db.cursor()
        c.execute("SELECT Comment FROM comments WHERE ArtID='1'")
        result = c.fetchall()
        c.close()
        return result

    # SENTIMENT ANALYSE METHOD 2 FOR COMMENTS FROM ARTICLE 1
    @cherrypy.expose()
    def sentiment_analyse_method_2_art_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        comments1 = self.get_comm_art_1(self)
        score_sentiment = []

        for sentence in comments1:
            password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            top_level_url = "https://api.theysay.io/v1/sentiment"
            password_mgr.add_password(None, top_level_url, "email@test.com", "XXXX")
            handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)

            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            request = urllib.request.urlopen('https://api.theysay.io/v1/sentiment', data)

            response_body = request.read()
            analyze_sentiment = json.loads(response_body)

            score_neg = '{:0.2f}'.format(round(analyze_sentiment['sentiment']['negative'], 4) * 100)
            print(score_neg)
            score_sentiment.append(score_neg)

            score_pos = '{:0.2f}'.format(round(analyze_sentiment['sentiment']['positive'], 4) * 100)
            print(score_pos)
            score_sentiment.append(score_pos)

            score_neutral = '{:0.2f}'.format(round(analyze_sentiment['sentiment']['neutral'], 3) * 100)
            print(score_neutral)
            score_sentiment.append(score_neutral)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

    # SENTIMENT ANALYSE METHOD 2 FOR COMMENTS FROM ARTICLE 1
    @cherrypy.expose()
    def emotion_analyse_method_2_art_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        comments1 = self.get_comm_art_1(self)
        score_emotion = []

        for sentence in comments1:
            password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
            top_level_url = "https://api.theysay.io/v1/emotion"
            password_mgr.add_password(None, top_level_url, "email@test.com", "XXXX")
            handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)

            data = urllib.parse.urlencode({"text": sentence}).encode("utf-8")
            request = urllib.request.urlopen('https://api.theysay.io/v1/emotion', data)

            response_body = request.read()
            emotion_sentiment = json.loads(response_body)

            score_anger = emotion_sentiment['emotions'][0]['score']
            print(score_anger)
            score_emotion.append(score_anger)

            score_calm = emotion_sentiment['emotions'][1]['score']
            print(score_calm)
            score_emotion.append(score_calm)

            score_fear = emotion_sentiment['emotions'][2]['score']
            print(score_fear)
            score_emotion.append(score_fear)

            score_happy = emotion_sentiment['emotions'][3]['score']
            print(score_happy)
            score_emotion.append(score_happy)

            score_like = emotion_sentiment['emotions'][4]['score']
            print(score_like)
            score_emotion.append(score_like)

            score_shame = emotion_sentiment['emotions'][5]['score']
            print(score_shame)
            score_emotion.append(score_shame)

            score_sure = emotion_sentiment['emotions'][6]['score']
            print(score_sure)
            score_emotion.append(score_sure)

            score_surprise = emotion_sentiment['emotions'][7]['score']
            print(score_surprise)
            score_emotion.append(score_surprise)

        return json.dumps(score_emotion).encode('utf-8')

    # SENTIMENT ANALYSE METHOD 3 FOR COMMENTS FROM ARTICLE 1
    @cherrypy.expose()
    def sentiment_analyse_method_3_art_1(self):
        cherrypy.response.headers['Content-Type'] = 'application/json'
        comments1 = self.get_comm_art_1(self)

        score_sentiment = []

        for sentence in comments1:
            vector = analyzer.polarity_scores(sentence[0])

            score_neg = vector['neg'] * 100
            print(score_neg)
            score_sentiment.append(score_neg)

            score_pos = vector['pos'] * 100
            print(score_pos)
            score_sentiment.append(score_pos)

            score_neutral = vector['neu'] * 100
            print(score_neutral)
            score_sentiment.append(score_neutral)

            score_comp = round((vector['compound'] * 100),3)
            print(score_comp)
            score_sentiment.append(score_comp)

            # structure of array score_sentiment [0] - negative score [1] - positive score [2] - neutral score
            #print(score_sentiment)

        return json.dumps(score_sentiment).encode('utf-8')

server_config = {'server.socket_host': '0.0.0.0',
                 'server.socket_port': 5555,
                 'server.thread_pool': 16}

service_config = {'/': {'tools.staticdir.on': True,
                        'tools.staticdir.dir': app_dir,
                        'tools.sessions.on': True,
                        'tools.encode.on': True,
                        'tools.encode.encoding': 'utf-8'
                        },
                  '/lib': {'tools.staticdir.on': True,
                           'tools.staticdir.dir': lib_dir}}

if __name__ == '__main__':
    cherrypy.config.update(server_config)
    cherrypy.tree.mount(Home(), '/', config=service_config)
    cherrypy.engine.start()
    cherrypy.engine.block()
