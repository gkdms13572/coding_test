# 만 나이 구하기
birth = "020705"
today = "240704"


b_int = int(birth[:2])
t_int = int(today[:2])

if b_int > 24:
    year_b = b_int + 1990
else:
    year_b = b_int + 2000

if t_int > 24:
    year_t = t_int + 1990
else:
    year_t = t_int + 2000
age1 = (year_t - year_b)

age = age1+1

m_b = int(birth[2:])
m_t = int(today[2:])

if m_t > m_b:
    print(age - 1)
else:
    print(age -2)