from datetime import datetime

from atproto import Client

seconds_in_day = 24 * 60 * 60

# Delete the specified post
def delete(client, post):
	client.delete(post.uri)

# Delete all posts from the given user from more than 'cutoff' days ago
def delete_posts_after_cutoff(client, handle, cutoff):
	first = True
	cursor = None
	now = datetime.now()

	while first or cursor != None:
		first = False

		profile_feed = client.get_author_feed(actor=handle, cursor=cursor)
		cursor = profile_feed.cursor
		for feed_view in profile_feed.feed:
			print('-', feed_view.post.indexed_at)
			post = feed_view.post
			timestamp = datetime.fromisoformat(post.indexed_at).replace(tzinfo=None)
			difference = now - timestamp
			if difference.total_seconds() > seconds_in_day * cutoff:
				delete(client, post)

# MAIN ================================

# TO DO: Read in handle and password from creds file

client = Client()
client.login(handle, password)

delete_posts_after_cutoff(client, handle, 30)
