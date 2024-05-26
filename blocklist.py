from datetime import datetime as dt

# Get the host path
# I am using Mac and so this is the host path
# If you are using Windows, search on Google "how to get host path" :D
hostpath = "C:\Windows\System32\Drivers\etc\hosts"

# localhost (will redirect to this host)
redirect = "127.0.0.1"

websitelist = [
    "www.reddit.com",
    "www.facebook.com",
    "www.instagram.com",
    "www.youtube.com",
    "www.cnn.com",
    "www.twitter.com",
    "www.buzzfeed.com",
    "www.yahoo.com",
    "www.tumblr.com",
    "www.netflix.com",
]

"""
Datetime Format
--------------
The datetime format is Year, Month, Day, Hour, Minute, 
e.g. (2022, 12, 28, 14, 15)
2022 - year
12 - month
28 - day
14 - hour (24 hrs format) (14 hrs = 2 pm)
15 - minutes
"""

# Will start to block at 9hrs and finish 5hrs in the evening
blocktime = {
    "start": dt(dt.now().year, dt.now().month, dt.now().day, 9),
    "end": dt(dt.now().year, dt.now().month, dt.now().day, 17)
}
