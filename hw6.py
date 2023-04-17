#사용자 정의 함수부
def display_multiplication_table(start,end):
  for i in range(1, 10):
    for j in range(start, end+1):
      print(f'{j}*{i}={j*i:2d}', end="\t\t")
    print()
  print()

#주 프로그램부
display_multiplication_table(2,5)
display_multiplication_table(6,9)
