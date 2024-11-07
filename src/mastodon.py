from mastodon import Mastodon

from src.client import Client

class Mastodon_Client(Client):
	"""Client class for Mastodon"""

	def __init__(self, access_token, api_base_url):
		self.client = Mastodon(
			access_token = access_token,
			api_base_url = api_base_url,
		)
		self.id = self.client.me().id

	def fetch_posts(self):
		"""Fetch all posts for the user"""

		fetch_limit = 40

		last_id = None
		all_posts = []

		while True:
			posts = self.client.account_statuses(id=self.id, limit=fetch_limit, max_id=last_id)

			if len(posts) == 0:
				break
			else:
				all_posts.append(posts)
				last_id = posts[-1].id
		
		return all_posts

	def fetch_favorites(self):
		"""Fetch all favorites for the user"""

		fetch_limit = 40
		all_faves = []

		faves = self.client.account_favourites(id=self.id, limit=fetch_limit, max_id=last_id)

		while True:
			faves = self.client.fetch_next(faves)

			if len(faves) == 0:
				break
			else:
				all_faves.append(faves)
				last_id = faves[-1].id
		
		return all_faves

	def delete_post(self, post):
		"""Delete a single specified post"""
		
		self.client.status_delete(post.id)

	def remove_favorite(self, post):
		"""Remove favorite from a single specified post"""
		
		self.client.status_unfavourite(post.id)

	# Data inspection ------------------------

	def get_post_date(self, post):
		return post.created_at

	def get_favorite_date(self, favorite):
		"""Returns the time associated with the given favorite"""
		print("ERROR: this apparently doesn't exist in the Mastodon API")
		assert False
