from pprint import pprint

from graphing.subreddit import Spider

spider = Spider()
donald = spider.frontpage('/r/The_Donald')

post = donald.next()

pprint(
    [a for a in spider.subreddits_posted_in(post['username'])]

)
