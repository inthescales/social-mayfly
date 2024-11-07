from datetime import datetime

import atproto

from src.client import Client

class Bluesky_Client(Client):
	"""Client class for ATProtocol (Bluesky)"""
	
	def __init__(self, handle, password):
		self.client = atproto.Client()
		self.client.login(handle, password)
		self.handle = handle

	def delete_post(self, feed_item):
		"""Delete a single specified feed item. Note that a feed item is not a 'post' per se — it could be a repost"""

		post = feed_item.post
		uri = feed_item.post.uri

		# if isinstance(feed_item.reason, atproto.models.app.bsky.feed.defs.ReasonRepost):
		# 	self.client.unrepost(uri)
		# else:
		# 	self.client.delete(uri)

		print("WOULD DELETE POST - " + str(self.get_post_date(feed_item)))

	def remove_favorite(self, post):
		"""Remove favorite from a single specified post"""
		
		# self.client.unlike(post.uri)

		print("WOULD UNLIKE POST - " + str(self.get_favorite_date(feed_item)))

	def fetch_posts(self):
		"""Fetch all posts for the user"""

		first = True
		cursor = None
		posts = []

		while first or cursor != None:
			first = False

			profile_feed = self.client.get_author_feed(actor=self.handle, cursor=cursor)
			cursor = profile_feed.cursor
			for feed_view in profile_feed.feed:
				posts.append(feed_view)

		return posts

	def fetch_favorites(self):
		"""Fetch all favorites for the user"""
		print("ERROR: Not yet implemented (get_actor_likes may not be available in atproto lib yet?)")
		assert False

	# Data inspection ------------------------

	def get_post_date(self, feed_item):
		"""Returns the time associated with the given post"""

		if isinstance(feed_item.reason, atproto.models.app.bsky.feed.defs.ReasonRepost):
			raw_timestamp = feed_item.reason.indexed_at
		else:
			raw_timestamp = feed_item.post.indexed_at

		return datetime.fromisoformat(raw_timestamp).replace(tzinfo=None)

	def get_favorite_date(self, favorite):
		"""Returns the time associated with the given favorite"""
		print("ERROR: not yet implemented")
		assert False
