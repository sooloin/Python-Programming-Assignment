shopping_bag={} #장바구니
print('[구입]')
while True:
  item = input('상품명? ')
  if item == '' :
    break
  am = int(input('수량은? '))
  shopping_bag[item]=am
  print(f'장바구니에 {item} {am}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기:{shopping_bag}')

print('\n[검색]') 
f = input('장바구니에서 확인하고자 하는 상품은? ')
if f in shopping_bag:
  idx = shopping_bag[f] 
  print(f'{f}은(는) {idx}개 담겨있습니다.')

else :
  print(f'{f}은(는) 장바구니에 없습니다.')
