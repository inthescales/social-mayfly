import json

accepted = {
	"bluesky": ["handle", "password"],
	"mastodon": ["access_token", "api_base_url"]
}

def read_creds(file):
    with open(file) as creds_data:
    	creds = json.load(creds_data)

    	for cred in creds:
    		if "type" not in cred:
    			print("ERROR: no service type specified")
    			exit(0)
    		elif cred["type"] not in accepted.keys():
    			print("ERROR: unrecognized service type '" + cred["type"] + "'")
    			exit(0)

    		type = cred["type"]
    		for key in accepted[type]:
    			if key not in cred:
    				print("ERROR: credential of type '" + type + "' must have keys " + ", ".join(accepted[type]))
    				exit(0)

    		for key in cred:
    			if key not in accepted[type] + ["type"]:
    				print("ERROR: extraneous key '" + key + "'")
    				exit(0)

    	return creds
