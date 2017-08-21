#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]

topic = []
topic_i = 0
for topic_i in xrange(n):
    topic_t = int(raw_input().strip())
    topic.append(topic_t)

maxi = 0
teams = {}

for t in range(len(topic)):
    for p in range(t, len(topic), 1):
        if t != p:
            topic_sum = str(topic[t] + topic[p])
            known_team_topics = m - topic_sum.count('0')
            if known_team_topics > maxi:
                maxi = known_team_topics

            if known_team_topics in teams:
                teams[known_team_topics].append( (topic[t], topic[p]) )
            else:
                teams[known_team_topics] = [ (topic[t], topic[p]) ]

print maxi
print len( teams[maxi] )
