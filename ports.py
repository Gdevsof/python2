ports_list = ("22", "443", "70,000", "ssh", "")

def is_valid_port(number):

	try:
		port = int(number)

	except (TypeError, ValueError):

		return False

		return 0 <= port <= 65535

for number in ports_list:
	print(f'{number}:', is_valid_port (number))