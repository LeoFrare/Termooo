import os
import sys
from wordfreq import top_n_list
import random
vocabulario = top_n_list('pt', 100000)
palavras = top_n_list('pt', 10000, wordlist='small')
palavras_5_letras = [
    palavra for palavra in palavras if len(palavra) == 5 and palavra.isalpha() and palavra.isascii()
]
termooo = random.choice(palavras_5_letras)
ac_er = []
n_sequencia = 1
tentativas = 0
sobra = 4
def mostrar():
       for i, a in enumerate(ac_er):
            print(*ac_er[i]['jgr'], sep=' | ')
            print(*ac_er[i]['tst'], sep='| ')
print(f'Tentativas = {sobra + 1}')
print('Tente adivinhar a palavra: ')
while True:
      acertos_n = []
      possui_n = []
      jgr = input('')
      jgr = jgr.lower()
      for numero, ltr_tentativa in enumerate(jgr):
            for indice, ltr_termo in enumerate(termooo):
                  if ltr_tentativa == ltr_termo and numero == indice:
                        acertos_n.append(indice)
      for numero, ltr_tentativa in enumerate(jgr):
            for indice, ltr_termo in enumerate(termooo):
                  if ltr_tentativa == ltr_termo and numero != indice and indice not in acertos_n and numero not in acertos_n:
                        possui_n.append(numero)
      if len(jgr) == 5 and jgr[0] * 5 != jgr and jgr in vocabulario:
            possui_n = list(set(possui_n))
            tst = []
            for num, ch in enumerate(jgr):
                  if num in acertos_n:
                        tst.append('🟩')
                  elif num in possui_n:
                        tst.append('🟨')
                  else:
                        tst.append('🟥')
            ac_er.append({'jgr': jgr, 'tst': tst,})
            os.system('cls')
            if tentativas >= 4 and termooo != jgr:
                  os.system('cls')
                  print(f'Tentativas = {sobra}')
                  mostrar()
                  print('='*22)
                  print(f'Perdeu\n\nA palavra era: {termooo}')
                  print('='*22)
                  sys.exit()
            if jgr == termooo:
                  os.system('cls')
                  print(f'Tentativas = {sobra}')
                  mostrar()
                  print('='*22)
                  print(f'Parabens, você venceu!\nA palavra era: {termooo}')
                  sys.exit()
            print(f'Tentativas = {sobra}')
            for num in range(n_sequencia):
                  print(*ac_er[num]['jgr'], sep=' | ')
                  print(*ac_er[num]['tst'], sep='| ')
            tentativas += 1
            sobra -= 1
            n_sequencia += 1
      else:
             os.system('cls')
             print(f'Tentativas = {sobra + 1}')
             mostrar()