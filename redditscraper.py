# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:04:10 2020


url: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768


@author: David Lee
"""
from redditclient import reddit
import csv

commentlist = []
commentauthor = []
commentdictionary = {}


def saving_csv():
    with open('comment.csv', 'w', encoding='utf-8') as subreddit_comment:
        writer = csv.writer(subreddit_comment, quoting=csv.QUOTE_ALL)
        writer.writerow(commentlist)
        
        
def turn_dict():
    commentdictionary = dict(zip(commentauthor, commentlist))
   print(commentdictionary)
    
def subreddit_scrape():
    for randomized_subreddit in range (2):
        random_posts = reddit.subreddit('random').hot(limit=10)
        for posts in random_posts:
            submission = reddit.submission(id = posts.id)
            submission.comments.replace_more(limit=None)
            for top_comment in submission.comments:
                commentauthor.append(posts.subreddit)
                commentlist.append(top_comment.body)
                
            
if __name__ == "__main__":
    subreddit_scrape()
   turn_dict()
    saving_csv()
