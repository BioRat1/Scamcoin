import praw

reddit = praw.Reddit(
    user_agent="ScamBot (by u/KingTrog",
    client_id="V49lu1T2RaoFZw",
    client_secret="ZJo1pmpDOrP3nAiWtQxf4I07a5DyZg",
    username="KingTrog",
    password="wolvess123",
)

subreddit = reddit.subreddit("Bitcoin"+"Scams")
for b in subreddit.search("scam", limit=50):
    print(b.title)
    print(b.selftext)
        
input()
    



