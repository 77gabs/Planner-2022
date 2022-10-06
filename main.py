from user import *
from scheduling import scheduling
escolha = input("Escolha um tipo de agendamento\nMeta, atividade ou compromisso\nR: ")
if escolha == 'meta':
  from goal import *
elif escolha == 'atividade':
  from activity import *
elif escolha == 'compromisso':
  from commitment import *
else:
  print('Opção Inválida senhor(a)')
  quit()