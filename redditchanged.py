# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:55:47 2020

@author: David Lee
"""
from redditclient import reddit
import csv

class commentor:
    commentlist = []
    commentauthor = []
    commentdictionary = {}

def find_user_profile(user_input):
    for unique_author in commentor.commentauthor:
        comment_author = str(unique_author)   
        for submission in reddit.redditor(comment_author).submissions.top("all"):
            print(submission.subreddit)
            
            

def subreddit_scrape():
    print("Please do not put any spaces in your input")
    user_input = input("What Subreddit are you interested in? ")
    

    Targeted_posts = reddit.subreddit(user_input).hot(limit=10)
    for posts in Targeted_posts:
        submission = reddit.submission(id = posts.id)
        submission.comments.replace_more(limit=None)
        for top_comment in submission.comments:
            commentor.commentauthor.append(top_comment.author)
            commentor.commentlist.append(top_comment.body)
    
    return user_input
            
if __name__ == "__main__":
    subreddit_scrape()
    find_user_profile(subreddit_scrape)
