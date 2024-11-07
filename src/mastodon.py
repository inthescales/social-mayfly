from mastodon import Mastodon

class Mastodon_Client(Client):
	"""Client class for Mastodon"""

	def __init__(self, access_token, api_base_url):
		self.client = Mastodon(
			access_token = access_token,
			api_base_url = api_base_url,
		)
		self.id = client.me().id

	def fetch_posts(self):
		"""Fetch all posts for the user"""

		fetch_limit = 40

		last_id = None
		all_posts = []

		while True:
			posts = client.account_statuses(id=self.id, limit=fetch_limit, max_id=last_id)

			if len(posts) == 0:
				break
			else:
				all_posts.append(posts)
				last_id = posts[-1].id
		
		return all_posts

	def fetch_favorites(self):
		"""Fetch all favorites for the user"""
		print("ERROR: not yet implemented")
		assert False

	def delete_post(self, post):
		"""Delete a single specified post"""
		print("ERROR: not yet implemented")
		assert False

	def remove_favorite(self, post):
		"""Remove favorite from a single specified post"""
		print("ERROR: not yet implemented")
		assert False

	# Data inspection ------------------------

	def get_post_date(self, post):
		"""Returns the time associated with the given post"""
		print("ERROR: not yet implemented")
		assert False

	def get_favorite_date(self, favorite):
		"""Returns the time associated with the given favorite"""
		print("ERROR: not yet implemented")
		assert False
