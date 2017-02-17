import requests

def is_redditthing(thing):
    def f(letter):
        return thing.startswith(letter) and not thing.endswith("/")
    return f("/u/") or f("/r/")

class Spider(object):
    def __init__(self):
        self.reddit = "https://reddit.com"
        self.http = requests.Session()
        self.http.headers.update({'User-Agent': 'bot: /u/benediktkr responsible'})

    def _reddit2dict(self, target):
        assert is_redditthing(target)
        return self.http.get(
            self.reddit + target + '.json').json()['data']['children']

    def frontpage(self, subreddit):
        return ({
            'username': "/u/" +a['data']['author'],
            'permalink': a["data"]["permalink"],
        } for a in self._reddit2dict(subreddit))


    def subreddits_posted_in(self, user):
        return ({
            'subreddit': "/r/" + a['data']['subreddit'],
            'username': "/u/" + user,
            'created': a['data']['created'],
            } for a in self._reddit2dict(user))
