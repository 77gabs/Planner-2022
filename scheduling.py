from user import *
import os
import calendar
class scheduling():
  
  def __init__(self,tipoAgenda):
    self.formaAgenda = tipoAgenda
    
  def verAgendamento(self):
    tipoAgenda = input('O senhor deseja criar algum agendamento?\nR: ')
    os.system('clear')
    if tipoAgenda == 'sim':
      self.formaAgenda = input("selecione o tipo de agendamento:\n\n----------\n  Dia\n  Mês\n  Ano\n----------\nR: ")
      if self.formaAgenda == 'dia':
        pass
      elif self.formaAgenda == 'mês':
        pass
      elif self.formaAgenda == 'ano':
        pass
      else:
        try:
          (rfwer234sas)
        except:
          print('\033[1;31mEstá opção não é válida senhor(a).\033[0;0m')
        else:
          print('erro')
        finally:
          quit()

  def verificAgend(self):
    print('\n\033[1;92mforma de agendamento selecionado:',self.formaAgenda,'\n\033[0;0m')
    
  def getValidacaoAgend(self):
    return self.formaAgenda
    
GabrielYasminViny = scheduling("")
GabrielYasminViny.verAgendamento()
GabrielYasminViny.verificAgend()
GabrielYasminViny.getValidacaoAgend()