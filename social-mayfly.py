import getopt
import sys

import src.credentialing as credentialing

from src.bluesky import Bluesky_Client
from src.mastodon import Mastodon_Client

def run(creds_file, threshold):
	credentials = credentialing.read_creds(creds_file)

	for cred in credentials:
		if cred["type"] == "bluesky":
			client = Bluesky_Client(cred["handle"], cred["password"])
		elif cred["type"] == "mastodon":
			client = Mastodon_Client(cred["access_token"], cred["api_base_url"])

		client.delete_posts_after_threshold(threshold)

if __name__ == '__main__' and len(sys.argv) > 0:

	creds_file = "creds.json"
	threshold = 30

	try:
		opts, params = getopt.getopt(sys.argv[1:], "c:t:", ["creds", "threshold"])
	except getopt.GetoptError:
		print('ERROR: getopt error')
		sys.exit(2)

	# Process args
	for opt, arg in opts:
		if opt in ["-c", "--creds"]:
			creds_file = arg
		elif opt in ["-t", "--threshold"]:
			threshold = int(arg)

	run(creds_file, threshold)
    