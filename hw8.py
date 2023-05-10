#사용자 정의 함수부
def buy(shopping_bag):
  print('[구입]')
  item = input('상품명? ')
  if item == '' :
    return False

  else :
    am = int(input('수량은? '))
    shopping_bag[item]=am
    print(f'장바구니에 {item} {am}개가 담겼습니다.\n')
    return True

def show(shopping_bag) :
  print(f'\n>>> 장바구니 보기:{shopping_bag}')

def find(shopping_bag):
  print('\n[검색]') 
  f = input('장바구니에서 확인하고자 하는 상품은? ')
  if f in shopping_bag:
    idx = shopping_bag[f] 
    print(f'{f}은(는) {idx}개 담겨있습니다.')

  else :
    print(f'{f}은(는) 장바구니에 없습니다.')


#주 프로그램부
shopping_bag={} #장바구니
while True :
  if buy(shopping_bag) == False :
    break
show(shopping_bag)
find(shopping_bag)
