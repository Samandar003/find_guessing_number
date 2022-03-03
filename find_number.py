import random as r

pc_guess = r.randint(1, 10)
print('1 dan 10 gacha son o\'yladim topolasizma? ')

taxminlar = 0
while True:
  taxminlar += 1
  user_guess = int(input('>>>> '))
  if pc_guess > user_guess:
    print(user_guess, ' dan katta yana urining')
    continue
  elif pc_guess < user_guess:
    print(user_guess, ' dan kichik  yana urining')
    continue
  else:
    print('topdingiz')
    break
print(taxminlar)



