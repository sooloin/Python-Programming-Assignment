#사용자 정의 함수
def get_integer(prompt):
  C=int(input(prompt))
  return C

def exchange(C):
  M=(C//500)
  N=(C%500)//100
  O=((C%500)%100)//50
  P=(((C%500)%100)%50)//10
  print(f"500원 동전의 개수 : {M}")
  print(f"100원 동전의 개수 : {N}")
  print(f"50원 동전의 개수 : {O}")
  print(f"10원 동전의 개수 : {P}")

#주 프로그램부
C=get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(C)
