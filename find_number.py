import random as r

def machine_guess(x=10):
  pc_guess = r.randint(1, x)
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
  print(f"Siz {taxminlar} ta taxmin bilan topdingiz")
  return taxminlar

def person_guess(yuqori=10):
  input(f"1 dan 10 gacha son o'ylang va istalgan tugmani bosing. Men topaman: ")
  quyi = 1
  yuqori = 10
  taxminlar = 0
  while True:
    taxminlar += 1
    if yuqori != quyi:
      taxmin = r.randint(quyi, yuqori)
    else:
      taxmin = yuqori
      
    javob = input(f"Siz {taxmin} sonini o'yladingiz: true(t), {taxmin}dan katta(+), kichik(-): ").lower() # 5 # 3
    if javob == True:
      print(f"Siz {taxminlar} ta taxmin bilan topdingiz")
      
    elif javob == '+': 
      quyi = taxmin + 1
    elif javob == '-':
      yuqori = taxmin - 1
    else:
      break
  print(f"men {taxminlar} ta taxmin bilan topdim")
  return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_pc = machine_guess(x)
        taxminlar_user = person_guess(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Men {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))

play()

