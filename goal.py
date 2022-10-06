
class goal():
  def __init__(self, meta, diaLimiteE, meslimite, anolimite, horaLimiteE):
    self.goal = meta
    self.diaLimiteE = diaLimiteE
    self.mesLimiteE = meslimite
    self.anoLimiteE = anolimite
    self.horaLimiteE = horaLimiteE
    
  def Verduracao(self):
    self.goal = input("\nAdicione o nome da sua meta: ")
    self.diaLimiteE = input('Adicione o dia limite da meta: ')
    self.mesLimiteE = input("Adicione o mês limite da meta: ")
    self.anoLimiteE = input("Adicione o ano limite da meta: ")
    self.horaLimiteE = input('Adicione a hora limite da meta: ')
    file = open ('metas.txt', 'a+')
    file.write (f'\nMeta: {self.goal}\nHora: {self.horaLimiteE}\nDia: {self.diaLimiteE}\nMês: {self.mesLimiteE}\nAno: {self.anoLimiteE}')
  
    
  def Validuracao(self):
    print(f'\n\033[1;93mA meta {self.goal} termina em {self.diaLimiteE}/{self.mesLimiteE}/{self.anoLimiteE} as {self.horaLimiteE}.\033[0;0m')
      
GabrielYasminViny = goal('','','','','')
GabrielYasminViny.Verduracao()
GabrielYasminViny.Validuracao()