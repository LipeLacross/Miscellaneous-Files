list_words = ['espeon', 'eevee', 'umbreon', 'vaporeon', 'jolteon', 'flareon', 'glaceon', 'leafeon', 'sylveon',]


def order_words(low):
  for w in range(len(low)):
    for l in range(len(low) - 1 - w):
      if low[l] > low[l + 1]:
        temp = low[l]
        low[l] = low[l+1]
        low[l+1] = temp
  print(low)

order_words(list_words)

assert list_words == ['eevee', 'espeon', 'flareon', 'glaceon', 'jolteon', 'leafeon', 'sylveon', 'umbreon', 'vaporeon']


# Não sabemos se é comum de outras linguagens, já organiza as palavras em ordem alfabetica
# Além da desordem adicionamos eevee e espeon apara testar além da primeira letra
