import sys
from time import sleep
from pprint import pprint

from neo4j.v1 import GraphDatabase

from graphing.subreddit import Spider

# hacky way to make the script sleep first, waiting for neo4j in compose
zzz = sys.argv[-1]
if zzz.isdigit():
    print "Detected Docker, sleeping for {} secs".format(zzz)
    sleep(float(zzz))

spider = Spider()
donald = spider.frontpage('/r/The_Donald')

post = donald.next()

pprint(
    [a for a in spider.subreddits_posted_in(post['username'])]

)
