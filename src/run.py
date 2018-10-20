import requests
import json

def find_substitutes(pre, med):

	# initialize dictionary to store results
	updates = {}

	# iterate through prescriptions
	for p in pre: 

		# iterate through medications
		for m in med:

			# check if medication id matches prescribed and generic value
			if m["id"] == p["medication_id"] and m["generic"] == False:

				for item in med:

					# use rxcui value and generic value to find substitute for branded medication
					if m["rxcui"] == item["rxcui"] and item["generic"] == True:

						# perform update
						updates[p["id"]] = item["id"]

	# format results
	updates = {"prescription_updates": [{"prescription_id": p, "medication_id": m} for p, m in updates.items()]}

	return updates

if __name__ == '__main__':

	# connect to api
	prescriptions = requests.get("http://api-sandbox.pillpack.com/prescriptions")
	medications = requests.get("http://api-sandbox.pillpack.com/medications")

	# store api content
	pre = prescriptions.json()
	med = medications.json()

	# call function to find substitutes
	results = find_substitutes(pre, med)

	# write to file
	with open('prescription_updates.json', 'w') as saved:
		json.dump(results, saved, indent = 4)
