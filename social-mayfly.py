import src.credentialing as credentialing

from src.bluesky import Bluesky_Client
from src.mastodon import Mastodon_Client

credentials = credentialing.read_creds("creds.json")
threshold = 30

for cred in credentials:
	if cred["type"] == "bluesky":
		client = Bluesky_Client(cred["handle"], cred["password"])
	elif cred["type"] == "mastodon":
		client = Mastodon_Client(cred["access_token"], cred["api_base_url"])

	client.delete_posts_after_threshold(threshold)
