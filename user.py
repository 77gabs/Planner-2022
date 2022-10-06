#-=-=-=-=-=-=-=-=-=-=-=-=-=#
#        ____________      #
#        Planner 2.0       #
#        ‾‾‾‾‾‾‾‾‾‾‾‾      #
#                          #
#         Alunos:          #
#     Gabriel Carvalho     #
#      Vinycius Vieira     #
#       Yasmin Leal        #
#                          #
#       Turma: 2° Ano      #
#   Informática matutino   #
#-=-=-=-=-=-=-=-=-=-=-=-=-=#

#Bibliotecas
import os
import calendar
import time
import random

#Dicionário
user = {}
#CLASSE usuario
class usuarioLOG():
  def __init__(self,nome,sobrenome,senha,telefone,email):
    self.__nome = nome
    self.__sobrenome = sobrenome
    self.__senha = senha
    self.__telefone = telefone
    self.__email = email

# DEF E GET
  def getemail(self):
    return self.__email
  def getsenha(self):
    return self.__senha

  #4 bimestre
  # def exitconta(self): 
  #   user.pop(self.__email)
  #   del self

# DICIONÁRIO com 
  dicio = {'Nome':'Gabriel','Sobrenome':'Carvalho','Telefone':'993208342','Email':'g@gmail.com','Senha':'123'}
# CADASTRO USUÁRIO
  def cadastro(self):
    print('\033[1;32mby: GYV\033[0;0m')
    print('-'*30)
    print('   CADASTRO NO PLANNER')
    print('-'*30)
    self.__nome = input('Digite seu primeiro nome: ')
    self.__sobrenome = input('Digite seu sobrenome: ')
    self.__telefone = int(input('Digite seu telefone: '))
    self.__email = input ('Digite seu email: ')
    while '@gmail.com' not in self.__email:
      self.__email = input('\033[1;31mEste email não é aceito. Digite um email no formato "@gmail.com": \033[0;0m')
    # PARA O 4BIMESTRE
    # while self.email in user:
    #   self.email = input('Email já existe. Digite um email válido: ')
    self.__senha = input('Digite sua senha: ')
    while '123' in self.__senha:
      self.__senha = input('\033[1;31mesta senha não é segura. Digite uma melhor:\033[0;0m ')
    email = self.__email
    email = usuarioLOG(self.__nome,self.__sobrenome, self.__telefone, self.__email, self.__senha)
    user[email.getemail()] = email
    file = open ('user.txt', 'a+')
    file.write (f'\nNome: {self.__nome} {self.__sobrenome}\nTelefone: {self.__telefone}\nEmail: {self.__email}\nSenha: {self.__senha}')
    os.system('clear')

# VISUALIZAR DADOS USUÁRIO
  def dados(self):
    deseja = input('\nDeseja ver seus dados?\nR: ')
    os.system('clear')
    if deseja == 'sim':
      print('\n\n           \033[1;93mDADOS CADASTRADOS\033[0;0m')
      print('-'*40)
      print('nome completo:', self.__nome,self.__sobrenome)
      print('-'*40)
      print(f'Telefone: (69) {self.__telefone}')
      print('-'*40)
      print('Email:', self.__email)
      print('-'*40)
      print('Senha: ---------')
      print('-'*40)

      ops = input('\nDeseja sair desta aba e ir para o painel da agenda?\nr: ')
      os.system('clear')
      if ops == 'sim':
        pass
      else:
        print(f'Ok senhor(a) {self.__nome}, obrigado pela preferência, volte sempre.')
        exit()
    else:
      pass
  
# LOGIN USUÁRIO 
  def login(self):
    os.system('clear')
    print('-'*30)
    print('      LOGIN PLANNER 2.0')
    print('-'*30)
    self.__email1 = input("Insira o seu email: ")
    self.__senha2 = input("Insira sua senha: ")
    if self.__email1 == self.__email and self.__senha2 == self.__senha:
      print('\033[1;94m\nLogin efetuado\n\033[0;0m')
      print('\nVocê já pode começar as atividades em nossa plataforma!')
      pass
    else:
      print('\033[1;31m\nAcesso negado\n\033[0;0m')
      self.__email1 = input('Digite seu email novamente: ')
      self.__senha2 = input('Digite sua senha novamente: ')
      if self.__email1 == self.__email and self.__senha2 == self.__senha:
        print('\033[1;94m\nLogin efetuado\n\033[0;0m')
        pass
      else:
        print('\033[1;31m\nAcesso negado\n\033[0;0m')
        self.__email1 = input('Digite seu email novamente: ')
        self.__senha2 = input('Digite sua senha novamente: ')
        if self.__email1 == self.__email and self.__senha2 == self.__senha:
          print('\033[1;94m\nLogin efetuado\n\033[0;0m')
          pass
        else:
          print('\033[1;31m\nAcesso negado\n\033[0;0m')
          #ALTERAÇÃO DE SENHA
          NovaSenha = input('\nVocê esqueceu sua senha?\nr: ')
          os.system('clear')
          if NovaSenha == 'sim':
            print('-' * 25)
            print('\033[1;94mVamos resolver isso agora\033[0;0m')
            print('-' * 25)
            troca1 = input('Digite seu email: ')
            
            #aqui
            if troca1 == self.__email:
              print('enviamos um código, verifique este email')
              a = random.randint(1000,9999)
              print('-'*20)
              print('\033[1;31m	Código:', a)
              print('\033[0;0m-'*20)
              cod = int(input('Digite o código: '))
              if cod == a:
                print('-'*20)
                NovaSenha2 = input('Digite sua nova senha: ')
                print('-'*20)
                if NovaSenha2 == self.__senha:
                  while NovaSenha2 == self.__senha:
                    print('\n\033[1;31msenha não pode ser identica a anterior\033[0;0m\n')
                    NovaSenha2 = input('Digite novamente uma nova senha: ')
                elif NovaSenha2 != self.__senha:
                  print('\nmudança de senha efetuada\n')
                self.__senha = NovaSenha2
                file = open ('user.txt', 'a+')
                file.write (f'\nNovaSenha: {NovaSenha2}')
                
              elif cod != a:
                cod = input('código inválido.')
                quit()
                  
            #ate aqui
            elif troca1 != self.__email:
              print('email inválido.')
              quit()
          elif NovaSenha == 'não':
            print(f'ok {self.__nome}, mas se não digitou a senha corretamente, não poderá acessar sua agenda.')
            quit()
          else:
            print(f'Opção inválida {self.__nome}')
            exit()

        
    
  def atvpessoa(self):
    print(f'\nBem vindo {self.__nome}, vamos as atividades:\n')
    time.sleep(1)
    print('                    Calendário do Ano:\n')
    from datetime import datetime
    print('Hoje é:',datetime.today().strftime('%A, %B %d, %Y %H:%M:%S\n'))
    print(calendar.calendar(2022))

 
usuario = usuarioLOG("","","","","")
print('\033[1;92m             Planner 2.0\n\033[0;0m')
menu = input("Olá senhor(a), vamos se cadastrar no planner?:\nR: ")
os.system('clear')
if menu == 'sim':
  usuario.cadastro()
  usuario.login()
  usuario.dados()
  usuario.atvpessoa()
elif menu == 'não':
  print('Ok, obrigado por acessar nosso site.')
  quit()
else:
  print('Opção inválida!')
  x = 'hello'
  if not type(x) is int:
    raise TypeError('São permitidos apenas "sim" para continuar.')
  
  x = -1
  if x < 0:
    raise Exception('Não aceitamos caracters diferentes de "sim".')
  quit()