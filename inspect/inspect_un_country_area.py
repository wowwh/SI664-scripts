import logging
import os
import pandas as pd
import sys as sys


def main(argv=None):
	"""
	Utilize Pandas library to read in UNSD M49 country and area .csv file (tabbed separator).
	Retrieve individually the regions, sub-regions, intermediate regions, and country and areas,
	filtering out duplicate entries, and sorting in alphabetical order. Write out each list to
	a .csv file for inspection.
	"""
	if argv is None:
		argv = sys.argv

	msg = [
		'Source file read {0}',
		'UN regions written to file {0}',
		'UN sub-regions written to file {0}',
		'UN intermediate regions written to file {0}',
		'UN countries and areas written to file {0}'
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

	# Read in UNESCO heritage sites data (tabbed separator)
	input_csv = './input/un_area_country_codes-m49.csv'
	data = pd.read_csv(input_csv, sep='\t', engine='python')
	logging.info(msg[0].format(os.path.abspath(input_csv)))

	# Write regions to a .csv file.
	regions_csv = './output/un_regions.csv'
	regions_data_frame = data['region_name'].drop_duplicates().sort_values()
	regions_data_frame.to_csv(regions_csv, sep='\t', encoding='utf-8', index=False)
	logging.info(msg[1].format(os.path.abspath(regions_csv)))

	# Write sub-regions to a .csv file.
	sub_regions_csv = './output/un_sub_regions.csv'
	sub_regions_data_frame = data['sub_region_name'].drop_duplicates().sort_values()
	sub_regions_data_frame.to_csv(sub_regions_csv, sep='\t', encoding='utf-8', index=False)
	logging.info(msg[2].format(os.path.abspath(sub_regions_csv)))

	# Write intermediate_regions to a .csv file.
	intermed_regions_csv = './output/un_intermed_regions.csv'
	intermed_regions_data_frame = data['intermediate_region_name'].drop_duplicates().sort_values()
	intermed_regions_data_frame.to_csv(intermed_regions_csv, sep='\t', encoding='utf-8', index=False)
	logging.info(msg[3].format(os.path.abspath(intermed_regions_csv)))

	# Write countries or areas to a .csv file.
	countries_areas_csv = './output/un_country_area.csv'
	countries_areas_data_frame = data['country_area_name'].drop_duplicates().sort_values()
	countries_areas_data_frame.to_csv(countries_areas_csv, sep='\t', encoding='utf-8', index=False)
	logging.info(msg[4].format(os.path.abspath(countries_areas_csv)))


if __name__ == '__main__':
	sys.exit(main())