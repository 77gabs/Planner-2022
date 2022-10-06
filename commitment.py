from scheduling import *

class Compromisso():
  def __init__(self,dataCompromisso,horaCompromisso,qCompromisso,localCompromisso):
    self.date = dataCompromisso
    self.hora = horaCompromisso
    self.comp3 = qCompromisso
    self.local = localCompromisso
        
  def Vercompromisso(self):
    self.date = input("\nescolha a data do compromisso: ")
    GSD = self.date.split()
    print('compromisso agendado para:',GSD)
    self.hora = input("\nescolha a hora do compromisso: ")
    self.comp3 = input('Qual será seu compromisso?\nR:')
    self.local = input("insira o local do compromisso: ")
    file = open ('compromissos.txt', 'a+')
    file.write (f'\ncompromisso:{self.comp3}\ndata: {self.date}\nhora: {self.hora}\nlocal: {self.local}')
         
  def validarcompromisso(self):
    print('\n\033[1;93mdia',self.date,", as",self.hora,'você tera um(a)',self.comp3,'na(o)',self.local,'.','\033[0;0m	')
  
GabrielYasmimViny = Compromisso("","","","")
GabrielYasmimViny.Vercompromisso()
GabrielYasmimViny.validarcompromisso()