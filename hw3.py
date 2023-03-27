#사용자 정의 함수
#get_fixed_price
def get_fixed_price(discount):
  d=int(input(discount))
  return d

#주 프로그램부
d= int(input("할인율은? "))
A=get_fixed_price("A상품의 할인된 가격은? ") #get_fixed_price 2번 사용하기
B=get_fixed_price("B상품의 할인된 가격은? ")


a=A/(1-(d*0.01)) #원가 구하기
b=B/(1-(d*0.01)) #원가 구하기

print(f"A상품의 정가는 {a}원")
print(f"B상품의 정가는 {b}원")
