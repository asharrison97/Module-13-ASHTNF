import unittest
import datetime

# Function to test the symbol value
def test_symbol(var):
	length = len(var)
	if var.isupper():
		if length > 7 or length <= 0:
			raise Exception("INVALID SYMBOL LENGTH")
		else:
			return True
	else:
		raise Exception("LOWERCASE SYMBOL CHARACTER")

# Function to test the chart type value
def test_chart_type(var):
	if isinstance(var, int):
		if(var == 1 or var == 2):
			return True
		else:
			raise Exception("INVALID CHART INTEGER ENTERED")
	else:
		raise Exception("NOT AN INTEGER TYPE")

# Function to test the time series type value
def test_time_series(var):
	if isinstance(var, int):
		if(var >= 1 and var <= 4):
			return True
		else:
			raise Exception("INVALID TIME SERIES INTEGER ENTERED")
	else:
		raise Exception("NOT AN INTEGER TYPE")

# Function to test the start date value
def test_start_date(var):
	if isinstance(var, datetime.datetime):
		return True
	else:
		raise Exception("INVALID OBJECT TYPE")

# Function to test the end date value
def test_end_date(var):
	if isinstance(var, datetime.datetime):
		return True
	else:
		raise Exception("INVALID OBJECT TYPE")

	
class LearnTest(unittest.TestCase):

	def test_myfunc(self):
		self.assertEqual(test_symbol("IBM"),True)
	def test_chart_type(self):
		self.assertEqual(test_chart_type(1),True)
	def test_time_series(self):
		self.assertEqual(test_time_series(2),True)
	def test_start_date(self):
		x = datetime.datetime(2025, 4, 25)
		self.assertEqual(test_start_date(x),True)
	def test_end_date(self):
		y = datetime.datetime(2025, 4, 25)
		self.assertEqual(test_end_date(y),True)

if __name__ == "__main__":
	unittest.main()