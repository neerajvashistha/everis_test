import os
import json
import config
import argparse
import os, sys
import pandas as pd

class InvalidData(Exception):
    pass

class classify:
	"""This module provide access to records by classifying them into VIP or NO_VIP"""

	# instance attributes
	def __init__(self):
		self.data_path = os.path.join(config.DATA_DIR, "store_transactions.csv")
		self.out_path = config.OUT_DIR
		self.df = pd.read_csv(self.data_path)

	# instance method
	def get_classification(self,product_id):
		"""Returns the records for product_id and classify them into VIP if MRP >= VIP_WEIGHT else NO_VIP,
		see config.py to set VIP_WEIGHT value.

		Parameters:
		product_id (int): product id value

		Returns:
		json:records in json form

		"""
		if not isinstance(product_id, int):
			raise InvalidData('product_id has to be integer')		
		match_records = self.df[self.df['PRODUCT_ID']==product_id].copy() # get matching product_id records and make a separate copy in memory
		if match_records.empty:
			raise InvalidData('Please provide a valid product_id')
		match_records['CLASSIFICATION'] = match_records.apply(lambda x: "VIP" if x.MRP >= config.VIP_WEIGHT else "NO_VIP", axis=1)
		match_records = match_records.drop_duplicates()
		format_records = list(match_records.to_dict(orient='index').values()) # drop the index key and return records
		
		# to file
		file_path = os.path.join(self.out_path, str(product_id)+".csv")
		with open(file_path, 'w') as outfile:
			json.dump(format_records, outfile)
		return json.dumps(format_records)


if __name__ == '__main__':
	obj = classify()
	print(obj.get_classification(12254943))
