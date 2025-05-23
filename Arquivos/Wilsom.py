import time
import random

version = '1.0 alpha'

print("\n🐾 Brincando com o Wilsom 🐈")
print(f"Versão: {version}\n")

nome = input("Digite seu nome: ")

menu_inicial = [
    '1. Começar a brincar com Wilsom',
    '2. Sair'
]

menu_acao = [
    '1. Abraçar 🤗',
    '2. Dar beijinhos 😘',
    '3. Fazer cafuné 👋',
    '4. Brincar com ele 🪀',
    '5. Alimentar o Wilsom 🍽️',
    '6. Dar uma bebida para Wilsom 🥤',
    '7. Voltar ao menu inicial'
]

menu_comida = [
    '1. Peixe 🐟',
    '2. Ração 🥣',
    '3. Petisco 🍖',
    '4. Cancelar'
]

menu_bebida = [
    '1. Água 💧',
    '2. Leite 🥛',
    '3. Suco de peixe 🐟🍹',
    '4. Cancelar'
]

acoes_feitas = []
felicidade = 0
hidratacao = 0  # novo parâmetro

# Contadores de ações
abracos = 0
beijinhos = 0
cafunes = 0
brincadeiras = 0
alimentacoes = 0
bebidas = 0  # contador de hidratação

opcao_inicial = ''
while opcao_inicial != '2':
    print(f"\n🐈 {nome}, escolha o que deseja fazer:")
    for item in menu_inicial:
        print(item)
    opcao_inicial = input("Digite o número da opção: ")

    if opcao_inicial == '1':
        opcao_acao = ''
        while opcao_acao != '7':
            print("\n😺 Wilsom está pronto para brincar! O que você quer fazer?")
            for item in menu_acao:
                print(item)
            opcao_acao = input("Digite o número da ação: ")

            if opcao_acao == '1':
                print("💞 Você deu um abraço apertado no Wilsom...")
                time.sleep(2)
                print("🐱 Wilsom ronronou feliz!")
                acoes_feitas.append("Abraço 🤗")
                felicidade += random.randint(1, 3)
                abracos += 1

            elif opcao_acao == '2':
                print("💋 Você encheu o Wilsom de beijinhos...")
                time.sleep(2)
                print("🐱 Wilsom lambeu sua bochecha!")
                acoes_feitas.append("Beijinhos 😘")
                felicidade += random.randint(2, 4)
                beijinhos += 1

            elif opcao_acao == '3':
                print("👐 Você fez um cafuné delicioso na cabeça do Wilsom...")
                time.sleep(2)
                print("🐱 Wilsom se espreguiçou e fechou os olhos!")
                acoes_feitas.append("Cafuné 👋")
                felicidade += random.randint(3, 5)
                cafunes += 1

            elif opcao_acao == '4':
                print("🪀 Você jogou uma bolinha e Wilsom correu atrás dela!")
                time.sleep(2)
                print("🐱 Ele pulou de alegria!")
                acoes_feitas.append("Brincar 🪀")
                felicidade += random.randint(2, 5)
                brincadeiras += 1

            elif opcao_acao == '5':
                print("\n🍽️ O que você quer dar para o Wilsom comer?")
                for comida in menu_comida:
                    print(comida)
                comida_escolhida = input("Escolha o número da comida: ")

                if comida_escolhida == '1':
                    print("🐟 Você deu um peixinho fresco ao Wilsom...")
                    time.sleep(2)
                    print("🐱 Wilsom devorou tudo em segundos!")
                    acoes_feitas.append("Comeu Peixe 🐟")
                    felicidade += random.randint(4, 7)
                    alimentacoes += 1

                elif comida_escolhida == '2':
                    print("🥣 Você serviu um prato de ração...")
                    time.sleep(2)
                    print("🐱 Wilsom comeu tudo com calma.")
                    acoes_feitas.append("Comeu Ração 🥣")
                    felicidade += random.randint(2, 5)
                    alimentacoes += 1

                elif comida_escolhida == '3':
                    print("🍖 Você deu um petisco especial para o Wilsom...")
                    time.sleep(2)
                    print("🐱 Wilsom abanou o rabo de felicidade!")
                    acoes_feitas.append("Comeu Petisco 🍖")
                    felicidade += random.randint(5, 8)
                    alimentacoes += 1

                elif comida_escolhida == '4':
                    print("↩️ Alimentação cancelada.")
                else:
                    print("❌ Opção inválida.")

            elif opcao_acao == '6':
                print("\n🥤 O que você quer dar para o Wilsom beber?")
                for bebida in menu_bebida:
                    print(bebida)
                bebida_escolhida = input("Escolha o número da bebida: ")

                if bebida_escolhida == '1':
                    print("💧 Você deu água fresquinha para o Wilsom beber...")
                    time.sleep(2)
                    print("🐱 Wilsom bebeu tudo e parece revigorado!")
                    acoes_feitas.append("Bebeu Água 💧")
                    felicidade += random.randint(2, 4)
                    hidratacao += 5
                    bebidas += 1

                elif bebida_escolhida == '2':
                    print("🥛 Você deu leite para o Wilsom...")
                    time.sleep(2)
                    print("🐱 Wilsom lambuzou o focinho!")
                    acoes_feitas.append("Bebeu Leite 🥛")
                    felicidade += random.randint(3, 5)
                    hidratacao += 4
                    bebidas += 1

                elif bebida_escolhida == '3':
                    print("🐟🍹 Você deu um suco especial de peixe para o Wilsom...")
                    time.sleep(2)
                    print("🐱 Wilsom adorou a novidade!")
                    acoes_feitas.append("Bebeu Suco de Peixe 🐟🍹")
                    felicidade += random.randint(4, 7)
                    hidratacao += 6
                    bebidas += 1

                elif bebida_escolhida == '4':
                    print("↩️ Hidratação cancelada.")
                else:
                    print("❌ Opção inválida.")

            elif opcao_acao == '7':
                print("↩️ Voltando ao menu principal...")
            else:
                print("❌ Opção inválida.")

    elif opcao_inicial == '2':
        print("\n Saindo...")
    else:
        print("❌ Opção inválida.")

# Resultado final
print(f"\n✨ {nome}, veja o que você fez com o Wilsom:")
for acao in acoes_feitas:
    print("-", acao)

print(f"\n🎉 Nível de felicidade do Wilsom: {felicidade} / 100")
print(f"💧 Nível de hidratação do Wilsom: {hidratacao} / 50")

if felicidade >= 30:
    print("🐾 Wilsom te ama MUITO! Vocês são inseparáveis!")
elif felicidade >= 20:
    print("🐾 Wilsom te ama! Vocês são grandes amigos!")
elif felicidade >= 10:
    print("🐾 Wilsom gosta muito de você!")
else:
    print("🐾 Wilsom ainda está tímido. Brinque, alimente e hidrate ele mais da próxima vez!")

# 🏆 Conquistas
print("\n🏆 Conquistas desbloqueadas:")

conquistas = []

if felicidade >= 50:
    conquistas.append("🎖️ Gato mais feliz do mundo!")
if brincadeiras >= 5:
    conquistas.append("🎮 Mestre das Brincadeiras")
if alimentacoes >= 3:
    conquistas.append("🍽️ Chef do Wilsom")
if bebidas >= 3:
    conquistas.append("🥤 Mestre da Hidratação")
if abracos >= 3 and beijinhos >= 3:
    conquistas.append("❤️ Carinho Infinito")
if len(acoes_feitas) >= 10:
    conquistas.append("🌟 Amigo Dedicado")

if not conquistas:
    print("😿 Nenhuma conquista desbloqueada... mas continue tentando!")
else:
    for c in conquistas:
        print(c)