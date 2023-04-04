#사용자 정의 함수부
def rep_char(c,n):
  print(c*n)

#사용자 정의 함수부
def draw_line_string(msg):
  nstr=len(msg)

  rep_char('-', nstr*2+4)
  print(f'Hello {msg},\nWelcome to Seoul. ')
  rep_char('-', nstr*2+4)

#주 프로그램부
draw_line_string(input("Input his/her name: "))
