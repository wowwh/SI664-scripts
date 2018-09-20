import logging
import os
import pandas as pd
import sys


def main(argv=None):
	"""
	Utilize Pandas library to read in UNESCO Heritage Sites .csv file (tabbed separator).
	Retrieve list of country and areas from the country_area column, filtering out duplicate
	entries, and sorting in alphabetical order. Then write out the list to a .csv file for
	inspection.
	"""
	if argv is None:
		argv = sys.argv

	msg = [
		'Source file read {0}',
		'UNESCO heritage site countries/areas written to file {0}'
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

	input_csv = './input/unesco_heritage_sites.csv'
	output_csv = './output/un_heritage_sites_country_area.csv'

	# Read in heritage site countries and areas and write out to a .csv file.
	data = pd.read_csv(input_csv, sep='\t', engine='python')
	logging.info(msg[0].format(os.path.abspath(input_csv)))
	data_frame = data['country_area'].drop_duplicates().sort_values()
	data_frame.to_csv(output_csv, sep='\t', encoding='utf-8', index=False)
	logging.info(msg[1].format(os.path.abspath(output_csv)))


if __name__ == '__main__':
	sys.exit(main())
