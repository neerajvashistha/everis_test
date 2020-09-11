from src.classify import classify
import argparse

if __name__ == '__main__':
	my_parser = argparse.ArgumentParser(description='list the product description for given product_id')
	my_parser.add_argument('product_id',
							metavar='product_id',
							type=int,
							help='product_id for description')
	args = my_parser.parse_args()
	product_id = args.product_id
	obj = classify()
	print(obj.get_classification(product_id))