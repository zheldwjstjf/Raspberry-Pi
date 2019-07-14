from datetime import datetime

# ------------------------------------
# --- class and func definition

class Get_left_time:
	# -
	def __init__(self, target_date_time):
		self.target_date_time = target_date_time

	# -
	def get_left_time_from_now(self):
		left_time = self.target_date_time - datetime.now()
		return left_time


class Get_date_num:
	# -
	def __init__(self, target_date_time, target_part):
		self.target_date_time = target_date_time
		self.target_part = target_part

	# -
	def get_datetime_nums(self):
		year_num = self.target_date_time.year
		month_num = self.target_date_time.month
		day_num = self.target_date_time.day
		hour_num = self.target_date_time.hour
		minitue_num = self.target_date_time.minute
		second_num = self.target_date_time.second
		return year_num, month_num, day_num, hour_num, minitue_num, second_num

	# -
	def get_datetime_nums2(self):
		target_part = self.target_part
		result_num = eval("self.target_date_time." + target_part)
		return result_num



# ------------------------------------
# --- class and func calling

# --- setting class vars
# -ƒ
# target_date_time = datetime(2019, 11, 21, 0, 0, 0, 0)


def get_left_time():
	#-
	print("\n\n\n=======  Select target date time  =======")
	target_date_time = input("Type a target date time [ ex) datetime(2019, 11, 21, 0, 0, 0, 0) ] \n\n Just hit Enter key for default ( current datetime ): ")

	try:
		target_date_time = eval(target_date_time)
	except Exception as e:
		target_date_time = datetime.now()
	print(">>> Selected [ target date time ] : ", target_date_time)


	# --- creating an instance on class
	# -
	my_Get_left_time = Get_left_time(target_date_time)

	# --- calling a method 
	# --- print result
	print("\n\n\n=======  Result  =======")

	# -
	left_time = str(myGet_left_time.get_left_time_from_now())
	print("\n\n\nleft time : " + str(left_time) + "\n\n\n")


def get_date_num():

	#-
	print("\n\n\n=======  Select target date time  =======")
	target_date_time = input("Type a target date time [ ex) datetime(2019, 11, 21, 0, 0, 0, 0) ] \n\n Just hit Enter key for default ( current datetime ): ")

	try:
		target_date_time = eval(target_date_time)
	except Exception as e:
		target_date_time = datetime.now()
	print(">>> Selected [ target date time ] : ", target_date_time)


	# -
	print("\n\n\n=======  Select target part  =======")
	target_part = input("type a target part ( year, month, day, hour, minute, second ) : \n\n Just hit Enter key for default ( day ): ")
	if len(target_part) == 0:
		 target_part = "day"
	print(">>> Selected [ target part ] : ", target_part)

	# --- creating an instance on class
	# -
	my_Get_date_num = Get_date_num(target_date_time, target_part)

	# --- calling a method 
	print("\n\n\n=======  Select method  =======")
	print(" 1 : Get target datetime num list ( year, month, day, hour, minute, second )")
	print(" 2 : Get target datetime num")
	mode = input("\nSelect one from above ( 1, 2) : \n\n Just hit Enter key for default ( 1 ): ")
	if len(mode) == 0:
		 mode = "1"
	mode = int(mode)
	print(">>> Selected [ target method ] : ", mode)


	# --- print result
	print("\n\n\n=======  Result  =======")
	# -
	if mode == 1:
		result_num = my_Get_date_num.get_datetime_nums()
		print("\n\n\ntarget date time num list : " + str(result_num) + "\n\n\n")

	# -
	if mode == 2:
		result_num = my_Get_date_num.get_datetime_nums2()
		print("\n\n\n"+ target_part + " : " + str(result_num) + "\n\n\n")


# get_left_time()

get_date_num()
