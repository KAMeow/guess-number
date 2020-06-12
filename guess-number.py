import random
r = random.randint(1, 100)
count = 0
count = int(count)
while True:
	count += 1
	que = input('please guessing number: ')
	que = int(que)
	if que == r:
		print('Your number is correct!')
		break
	elif que > r:
		print('your number is bigger than the answer.')
	elif que < r:
		print('your number is smaller than the answer.')
	print('you has guessing', count, 'times.')