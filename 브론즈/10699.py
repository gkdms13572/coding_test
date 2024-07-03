# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
from datetime import datetime

today = datetime.today()

print(today.strftime("%Y-%m-%d"))

# strftime 메소드를 사용하면 날짜와 시간을 다양한 형식으로 출력할 수 있습니다.
# print(today.strftime('%d/%m/%Y'))  # '03/07/2024'
# print(today.strftime('%A, %B %d, %Y'))  # 'Wednesday, July 03, 2024'
# print(today.strftime('%I:%M %p'))  # '12:30 PM'
