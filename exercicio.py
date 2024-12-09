def registrar_material(stock):
  nome = str(input("Insira o nome do material que quer registrar: "))
  if nome in stock:
    print ("Este material já está registrado!")
  else:
    quantidade = int(input("Insira a quantidade que tem: "))
    stock[nome] = quantidade
    print (f"o item {nome} foi adicionado ao stock!")

def verificar_stock(stock):
  nome = input("Insira o nome do item que você quer consultar: ")
  if nome in stock:
    print (f"O stock atual de {nome} é: {stock[nome]}")
  else:
    print ("Esse item não está registrado!")

def atualizar_stock(stock):
    nome = str(input("Nome do material que você quer utilizar: "))
    if nome in stock:
        operacao = str(input("Você deseja adicionar (A) ou remover (R)")).upper()
        quantidade = int(input("Quantidade: "))
        if operacao == "A":
            stock[nome] += quantidade
            print (f"{quantidade} unidade(s) adicionada(s) ao stock de {nome}")
        elif operacao == "R":
            if quantidade <= stock[nome]:
                stock[nome] = stock - quantidade
                print (f"{quantidade} unidade(s) adicionada(s) ao stock de {nome} ")
            else:
                print ("Você quer remover mais do que você tem!")
        else:
          print ("Operação inválida")
    else:
        print ("O nome não foi encontrado no stock")


def mostrar_stock(stock, filename='Stock.txt'):
  with open(filename, 'w') as file:
      file.write("Estado Geral do Stock:\n")
      file.write("Material\tQuantidade\n")
      file.write("-" * 30 + "\n")
      for material, quantidade in stock.items():
          file.write(f"{material}\t\t{quantidade}\n")




def main():
  stock = {}
  while True:
    print ("Programa de Gestão de Stock")
    print ("1. Registrar Material")
    print ("2. Verificar Stock de um material")
    print ("3. Atualizar o Stock")
    print ("4. Verificar Stock Geral")
    print ("5. Sair")
    opcao = str(input("Insira uma opção: "))
    if opcao == "1":
      registrar_material(stock)
    elif opcao == "2":
      verificar_stock(stock)
    elif opcao == "3":
      atualizar_stock(stock)
    elif opcao == "4":
      mostrar_stock(stock)
    elif opcao == "5":
      print ("A encerrar o programa...")
      break
    else:
      print ("Insira uma opção válida")



if __name__ == "__main__":
    main()





