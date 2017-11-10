import geojson
import parse as p 

def create_map(data_file):
	# Define GeoJSON 
	geo_map = {"type": "FeatureCollection"}

	# define empty list to collect each point to graph
	item_list = []

	# Iterate over our data to create geojson document
	for index, line in enumerate(data_file):

		# skip zero coordinates as this will throw of map
		if line['X'] == "0" or line['Y'] == "0":
			continue

		# setup new dictionary for each iteration
		data = {}

		# assign line items to geojson fields.
		data['type'] = 'Feature'
		data['id'] = index
		data['properties'] = {'title': line['Category'], 
							'description': line['Descript'],
							'date': line['Date']}
		data['geometry'] = {'type': 'Point',
							'coordinates': (line['X'], line['Y'])}

		# add data dictionary to our item_list
		item_list.append(data)

	for point in item_list:
		geo_map.setdefault('features', []).append(point)

	with open('file_sf.geojson', 'w') as f:
		f.write(geojson.dumps(geo_map))

def main():
	data = p.parse(p.MY_FILE, ",")

	return create_map(data)

if __name__ == '__main__':
	main()
