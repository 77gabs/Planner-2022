import os
atividade = {}
class atividade():
  def __init__(self, atividade, horaComeecooo, horaTtermino):
    self.atividade = atividade
    self.Hcomeco = horaComeecooo
    self.Htermino = horaTtermino
    
  def fazerAtividade(self):
    self.atividade = input("\nAdicione o nome da sua atividade: ")
    self.Dcomeco = input("Adicione o a data do começo da sua atividade(DD/MM/AAAA): ")
    self.Hcomeco = input('Adicione a hora do começo da sua atividade(00:00): ')
    self.Dtermino = input("Adicione o data de conclusão da sua atividade(DD/MM/AAAA): ")
    self.Htermino = input('Adicione a hora de conclusão da sua atividade(00:00): ')
    file = open ('atividades.txt', 'a+')
    file.write (f'\nNome: {self.atividade}\nComeça: {self.Dcomeco}\nHora começo: {self.Hcomeco}\nTermino: {self.Dtermino}\nHora termino: {self.Htermino}')

    
  def validarAtividade(self):
    print('\n\033[1;93mA atividade',self.atividade,'começa dia',self.Dcomeco,'as',self.Hcomeco,'e termina dia',self.Dtermino,'as',self.Htermino,'.','\033[0;0m')
      
GabrielYasminViny = atividade('','','')
GabrielYasminViny.fazerAtividade()
GabrielYasminViny.validarAtividade()