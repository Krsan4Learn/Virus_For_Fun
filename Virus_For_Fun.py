# Code With Python3
# Virus For Fun - Open Sites & Send Notifications
# Code By " القرصان الإلكتروني للتعليم "
# Folowme : thedigitalagee.blogspot.com

import webbrowser
import time
import random

while True:
    print("Start")
    sites = random.choice(["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a2f7c9d8-a913-4273-847f-705be41395df/d9efmjk-729da713-847d-48cb-abeb-5b5dcd2d2206.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYTJmN2M5ZDgtYTkxMy00MjczLTg0N2YtNzA1YmU0MTM5NWRmXC9kOWVmbWprLTcyOWRhNzEzLTg0N2QtNDhjYi1hYmViLTViNWRjZDJkMjIwNi5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.qVeP2vRQnv_8Z1aW04JsvbEGbNyr7KDC5LUQ64K9BD8", "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/a2f7c9d8-a913-4273-847f-705be41395df/d9ebz2w-66957331-3bd7-4c21-9da4-f42cb7b178c5.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYTJmN2M5ZDgtYTkxMy00MjczLTg0N2YtNzA1YmU0MTM5NWRmXC9kOWViejJ3LTY2OTU3MzMxLTNiZDctNGMyMS05ZGE0LWY0MmNiN2IxNzhjNS5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.-HdxkDyK0yu0RotAUX1Ix_4YYjmhlZxhAAzNJsbA5Ts", "https://d2skuhm0vrry40.cloudfront.net/2015/articles/1/8/7/1/5/3/2/san-francisco-subway-system-hacked-passengers-get-free-rides-148033947612.gif"])
    visit = "{}".format(sites)
    Open = webbrowser.open(visit)
    sec = random.randrange(1,6)
    time.sleep(sec)

    from win10toast import ToastNotifier

    ToastNotifie = ToastNotifier()
    ToastNotifie.show_toast("Virus", "You Have Been Hacked !! ", threaded=True, icon_path=None, duration=3)
    print("Stop")

