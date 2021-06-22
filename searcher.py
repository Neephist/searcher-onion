from googlesearch import search

input('Pressione ENTER para continuar')
print("Conteúdos: Hacking, eBooks, Forum, etc...")
conteudo = str(input("Qual conteúdo deseja? "))

dork = f'{conteudo} site:onion.link | site:onion.cab | site:onion.sh | site:tor2web.fi | site:onion.direct'

def menu():
    print("0 - NÃO")
    print("1 - SIM")


while True:
    menu()
    menus = int(input("Deseja prosseguir? "))
    if menus == 0:
        print("Volte sempre")
        break
    elif menus == 1:
        with open("sites.txt", "w") as stream:
            for url in search(dork, stop=100 or 1):
                print(url, file=stream)
                print("O link foi salvo (sites.txt)")
    else:
        print("[-] Opção inválida")
