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
    commentauthorsub = []
    commentdictionary = {}
    
class frequencycounter:
    counter = []
    user_input = ''

def output():
        max_key = max(commentor.commentdictionary, key=commentor.commentdictionary.get)
        print('Subreddit I want to recommend is:', max_key)

def freeqcounter():
    for subcounter in commentor.commentauthorsub:
        user = str(subcounter)
        if user.lower() != frequencycounter.user_input.lower():
            frequencycounter.counter.append(user)
        else:
            continue
    for i in range(len(frequencycounter.counter)):  
        if frequencycounter.counter[i] in commentor.commentdictionary:
            commentor.commentdictionary[frequencycounter.counter[i]] += 1
        else:
            commentor.commentdictionary[frequencycounter.counter[i]] = 1

def find_user_profile(user_input):
    for unique_author in commentor.commentauthor:
        comment_author = str(unique_author)   
        for submission in reddit.redditor(comment_author).submissions.top("all"):
            commentor.commentauthorsub.append(submission.subreddit)


def subreddit_scrape():
    print("Please do not put any spaces in your input")
    user_input = input("What Subreddit are you interested in? ")
    
    frequencycounter.user_input = str(user_input)

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
    freeqcounter()
    output()