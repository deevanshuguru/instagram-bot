from instagrapi import Client

cl = Client()
cl.login(USERNAME, PASSWORD)

cl.insights_media_feed_all("VIDEO", "ONE_WEEK", "LIKE_COUNT", 42)
cl.insights_account()

media_pk = cl.media_pk_from_url('https://www.instagram.com/p/CTA31aPj3IH/')
cl.insights_media(media_pk)
