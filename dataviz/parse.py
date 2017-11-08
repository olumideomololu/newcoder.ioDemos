import csv

MY_FILE =  "data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""parses a raw CSV file to a JSON like object."""

	# Open CSV file
	opened_file = open(raw_file)

	# Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	# setup an empty list
	parsed_data = []

	# skip over the first line of the file for the headers
	fields = csv_data.next()

	# iterate over each row of the csv file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	# Close CSV file
	opened_file.close()

	# Build a data structure to return parsed data


	return parsed_data

def main():
	# call parse function and give it needed parameters
	new_data = parse(MY_FILE, ",")

	#show data
	print new_data

if __name__ == '__main__':
	main()