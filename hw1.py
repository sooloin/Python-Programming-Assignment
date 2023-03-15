# 사용자 정의 함수부
def get_radius(prompt):
  r=int(input(prompt))
  return r  #입력한 정수값을 반환

def get_circle_area(r):
  area=3.14*(r**2)
  return area

# 주 프로그램부
r=get_radius("넓이를 구하고자 하는 원의 반지름은? ")
print(f"반지름이 {r}인 원의 넓이 = 3.14 x {r}*{r} =  {get_circle_area(r)}")
#출력형 f string 사용

