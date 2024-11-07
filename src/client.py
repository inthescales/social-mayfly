from datetime import datetime

seconds_in_day = 24 * 60 * 60

def passes_threshold(timestamp, threshold):
	"""Returns true if the timestamp is more than [threshold] days ago"""

	current_time = datetime.now()
	difference = current_time - timestamp
	return difference.total_seconds() > seconds_in_day * threshold

class Client:
	"""Generic superclass for a client object, which performs actions for a single specified account"""
	
	def __init__(self):
		print("ERROR: cannot instantiate generic Client")
		assert False

	# Network actions ------------------------

	def fetch_posts(self):
		"""Fetch all posts for the user"""
		print("ERROR: cannot perform network actions on generic Client class")
		assert False

	def fetch_favorites(self):
		"""Fetch all favorites for the user"""
		print("ERROR: cannot perform network actions on generic Client class")
		assert False

	def delete_post(self, post):
		"""Delete a single specified post"""
		print("ERROR: cannot perform network actions on generic Client class")
		assert False

	def remove_favorite(self, post):
		"""Remove favorite from a single specified post"""
		print("ERROR: cannot perform network actions on generic Client class")
		assert False

	# Data inspection ------------------------

	def get_post_date(self, post):
		"""Returns the time associated with the given post"""
		print("ERROR: cannot inspect data on generic Client class")
		assert False

	def get_favorite_date(self, favorite):
		"""Returns the time associated with the given favorite"""
		print("ERROR: cannot inspect data on generic Client class")
		assert False

	# Deletion actions ------------------------

	def delete_posts_after_threshold(self, threshold):
		"""Delete all posts for the account older than the given threshold (in days)"""
		posts = self.fetch_posts()
		for post in posts:
			timestamp = self.get_post_date(post)
			if passes_threshold(timestamp, threshold):
				self.delete_post(post)

	def remove_favorites_after_threshold(self, threshold):
		"""Remove all favorites for the account older than the given threshold (in days)"""
		faves = self.fetch_favorites()
		current_time = datetime.now()
		for fave in faves:
			if passes_threshold(timestamp, threshold):
				self.delete_post(post)
