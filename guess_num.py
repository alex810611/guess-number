#產生一個隨機整數1~100 (不印出來)
#讓使用者重複輸入數字去猜
#猜對的話印出 “終於猜對了”
#猜錯要告訴他比答案大獲小
import random
r = random.randint(1, 100) # random int 
while True :
	num = input ('請猜數字')
	num = int(num)
	if num == r :
		print ('終於猜對了')
		break
	elif num < r :
		print('比答案小')

	elif num > r :
		print('比答案大')
		

