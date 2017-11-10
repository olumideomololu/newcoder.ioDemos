from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np 
from parse import parse

MY_FILE =  "data/sample_sfpd_incident_all.csv"

def visualize_days():
	"""visualize data by day of week"""
	# grab data parsed earlier
	data_file = parse(MY_FILE, ",")

	# make a new variable, 'counter', from iterationg through each
	# line of data and count how many incident happen on each day 
	# of the week.
	counter = Counter(item["DayOfWeek"] for item in data_file)

	# separate x-axis data(days) from the counter variable from
	# the y-axis data(incidents)
	data_list = [
					counter["Monday"],
					counter["Tuesday"],
					counter["Wednesday"],
					counter["Thursday"],
					counter["Friday"],
					counter["Saturday"],
					counter["Sunday"]
				]

	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
	

	# with that y-axis data, assign it to a matplotlib plot instance
	plt.plot(data_list)

	#assing labels to the plot
	plt.xticks(range(len(day_tuple)), day_tuple)

	# save the plot
	plt.savefig("Days.png")

	# close the plot file 
	plt.clf()


def visualize_type():
	"""visualize data by category in a bar graph"""

	# grab parsed data
	data_file = parse(MY_FILE, ",")

	# create dict with incidents per category
	counter = Counter(item["Category"] for item in data_file)

	# set labels based on keys of counter
	labels = tuple(counter.keys())

	# set where labels hit x-axis
	xlocations = np.arange(len(labels)) + 0.5

	# width of each bar
	width = 0.5

	# assign data to bar plot
	plt.bar(xlocations, counter.values(), width=width)

	# assign labels and tick location to x-axis
	plt.xticks(xlocations + width/2, labels, rotation=90)

	# give some more room so the labels aren't cuf off in the graph
	plt.subplots_adjust(bottom=0.4)

	# make figure larger
	plt.rcParams['figure.figsize'] = 12, 8

	# save the plot
	plt.savefig("Type.png")

	# close figure
	plt.clf()


def main():
	#visualize_days()
	visualize_type()

if __name__ == '__main__':
	main()