import tweepy

from main import run

# Authenticate to Twitter
auth = tweepy.OAuthHandler("cnKvmeDFF11xGui0H3tJgZwQg", "iQNpYh5rqGW5mQEfViyEYaaMf5wM84BpHE9KhyENzHgiLV5ykF")
auth.set_access_token("1361878144345509890-l78H54RXfyu5yiMKPPYk4ovVzBatJh", "5B0Oo6OvMQCTF4soJRDguQ65Wv7LPnM09YqfTBmDVhVXi")

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

avg = 0
amt = 3

for i in range(amt):
    avg += run()

avg = avg / amt
api.update_status(f"Hello, I'm a bot! I used deep learning to try to predict the price of #dogecoin in 24 hours. Here's my prediction:\n\n${round(avg, 6)}\n\nWhat do you think?\n\n#doge #cryptocurrency")