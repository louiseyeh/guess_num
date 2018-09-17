#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對，印出"終於猜對了!"
#猜錯，告訴他比答案大/小

# 進階=>使用者自訂範圍
import random
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0 # 計數
while True:
	count += 1 # 簡潔版 快寫法count = count + 1
	num = input('請猜數字:')  #input為字串
	num = int(num)           #型別轉換
	if num == r:
		print('終於猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')