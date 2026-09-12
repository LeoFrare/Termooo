import os
import sys
from wordfreq import top_n_list
import random
vocabulario = top_n_list('pt', 100000)
palavras = top_n_list('pt', 10000, wordlist='small')
palavras_5_letras = [palavra for palavra in palavras if len(palavra) == 5 and palavra.isalpha() and palavra.isascii()]
while True:
      escolha = input('Modos: \n[T]ermo\n[D]ueto\n[Q]uarteto\n[P]ersonalizado\n[S]sair\nR: ')
      escolha = escolha.lower()
      if escolha == 't':
            numeros_gerais = 1
            variaveis = 0
            termooo = [random.choice(palavras_5_letras)]
            limite = 4
      elif escolha == 'd':
            variaveis = 1
            numeros_gerais = 2
            termooo = [*random.sample(palavras_5_letras, numeros_gerais)]
            limite = 5
      elif escolha == 'q':
            variaveis = 3
            numeros_gerais = 4
            limite = 8
            termooo = [*random.sample(palavras_5_letras, numeros_gerais)]
      elif escolha == 'p':
            os.system('cls')
            while True:
                  try:
                        numeros_gerais = input('Quantas palavras deseja descobrir?\n(Escolha apenas uma quantidade que caiba no seu terminal)\n[V]oltar\nR: ')
                        if numeros_gerais.lower() == 'v':
                              os.system('cls')
                              print('ok')
                              break
                        else:
                              numeros_gerais = int(numeros_gerais)
                        if numeros_gerais < 0:
                              numeros_gerais *= -1
                        if numeros_gerais == 4 or numeros_gerais > 0 and numeros_gerais < 3:
                              os.system('cls')
                              print('Essas opções já existem nos modos normais')
                              continue
                        else:
                              break
                  except:
                        os.system('cls')
                        print('apenas numeros')
                        continue
            if numeros_gerais == 'v':
                  continue
            variaveis = numeros_gerais - 1
            limite = numeros_gerais + 5 if numeros_gerais != 3 else numeros_gerais + 4
            termooo = [*random.sample(palavras_5_letras, numeros_gerais)]
      elif escolha == 's':
            os.system('cls')
            print('Ok.')
            sys.exit()
      else:
            os.system('cls')
            continue
      os.system('cls')
      ac_er = []
      acertadas = []
      for i in range(variaveis + 1):
            ac_er.append([])
      n_sequencia = 1
      tentativas = 0
      sobra = 4
      resultados = []
      def mostrar(arr):
            global resultados
            result = []
            for i in range(len(arr)):
                  resultados.append(arr[i])
                  result.append(arr[i])
            return result
      def mostrar_lado_a_lado(arr):
            os.system('cls')
            limite_horizontal = len(termooo)
            jogos_agrupados = {}
            for item in arr:
                  rodada = item[0]
                  palavra_nome = rodada['jgr']
                  if palavra_nome not in jogos_agrupados:
                        jogos_agrupados[palavra_nome] = []
                  jogos_agrupados[palavra_nome].append(rodada)
            for palavra_nome, rodadas_do_jogo in jogos_agrupados.items():
                  for i in range(0, len(rodadas_do_jogo), limite_horizontal):
                        bloco_atual = rodadas_do_jogo[i : i + limite_horizontal]
                        linhas_palavras = []
                        linhas_emojis = []
                        for rodada in bloco_atual:
                              palavra = rodada['jgr']
                              emojis = rodada['tst']
                              palavra_formatada = " | ".join(list(palavra))
                              emojis_formatados = "| ".join(emojis)
                              linhas_palavras.append(palavra_formatada)
                              linhas_emojis.append(emojis_formatados)
                              espaco_entre_letras = "       "
                              espaco_entre_jogadas = '      '
                        print(espaco_entre_letras.join(linhas_palavras))
                        print(espaco_entre_jogadas.join(linhas_emojis))
      print(f'Palavras = {len(termooo)} | Tentativas = {limite + 1}')
      print('Tente adivinhar a palavra: ')
      def calcular_certos(a, b, c, d):
            for numero, ltr_tentativa in enumerate(jgr):
                  for indice, ltr_termo in enumerate(a[d]):
                        if ltr_tentativa == ltr_termo and numero == indice:
                              b[d].append(indice)
            for numero, ltr_tentativa in enumerate(jgr):
                  for indice, ltr_termo in enumerate(a[d]):
                        if ltr_tentativa == ltr_termo and numero != indice and indice not in b[d] and numero not in b[d]:
                              c[d].append(numero)
      def validar(a, b, c):
            for num, ch in enumerate(jgr):
                  if num in a[c]:
                        tst[c].append('🟩')
                  elif num in b[c]:
                        tst[c].append('🟨')
                  else:
                        tst[c].append('🟥')
      vencer = []
      palavras_jogadas = []
      while True:
            acertos_n = []
            possui_n = []
            for i in range(numeros_gerais):
                  acertos_n.append([])
                  possui_n.append([])
            jgr = input('')
            jgr = jgr.lower()
            for i in range(variaveis + 1):
                  calcular_certos(termooo, acertos_n, possui_n, i)
            indice = 0
            if len(vencer) > 0:
                  for i, a in enumerate(vencer):
                        for _, ch in enumerate(termooo):
                              if a == ch:
                                    indice = _
                        acertos_n[indice] = []
                        possui_n[indice] = []
            if len(jgr) == 5 and jgr[0] * 5 != jgr and jgr in vocabulario and jgr not in vencer and jgr not in palavras_jogadas:
                  palavras_jogadas.append(jgr)
                  for i in range(variaveis + 1):
                        possui_n[i] = list(set(possui_n[i]))
                  tst = []
                  for i in range(numeros_gerais):
                        tst.append([])
                  for i in range(variaveis + 1):
                        validar(acertos_n, possui_n, i)
                  ac_er = [[] for _ in range(variaveis + 1)] 
                  for i in range(variaveis + 1):
                        ac_er[i].append({'jgr': jgr, 'tst': tst[i]})
                  os.system('cls')
                  for i, a in enumerate(termooo):
                        if termooo[i] == jgr:
                              acertadas.append(a)
                  mostrar(ac_er)
                  vencer = list(set(acertadas))
                  vnc = 0
                  for i in vencer:
                        for a in termooo:
                              if i == a:
                                    vnc += 1
                  if tentativas >= limite and vnc != len(termooo):
                        os.system('cls')
                        mostrar_lado_a_lado(resultados)
                        print('='*32 if len(termooo) < 3 else '='*96)
                        print(f'\nTentativas = {tentativas + 1}/{limite + 1}')
                        print(f'Perdeu\n\nA palavra era: {termooo[0]}' if len(termooo) == 1 else f'Perdeu\n\nAs palavras eram: {" - ".join(termooo)}')
                        print('='*32 if len(termooo) < 3 else '='*96)
                        sys.exit()
                  if vnc == len(termooo):
                        os.system('cls')
                        mostrar_lado_a_lado(resultados)
                        print('='*32 if len(termooo) < 3 else '='*96)
                        print(f'\nTentativas = {tentativas + 1}')
                        print(f'Parabens, você venceu!\n\nA palavra era: {termooo[0]}' if len(termooo) == 1 else f'Parabens, você venceu!\n\nAs palavras eram: {" - ".join(termooo)}')
                        print('='*32 if len(termooo) < 3 else '='*96)
                        sys.exit()
                  for num in range(n_sequencia):
                        mostrar_lado_a_lado(resultados)
                        print(f'{tentativas + 1}/{limite + 1}')
                  tentativas += 1
                  sobra -= 1
                  n_sequencia += 1
            else:
                  mostrar_lado_a_lado(resultados)
                  print(f'{tentativas}/{limite + 1}')