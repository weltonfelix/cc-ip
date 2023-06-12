spider_name = input()
machine_frequency = int(input())

if spider_name == "Miles Morales":
  if machine_frequency >= 2400:
        print("Essa frequência é desconhecida para o Miles! Com certeza vai achar encrenca!")
  elif machine_frequency >= 800:
        print("Miles será enviado para a praça do Harlem! O Rino e o Prowler estão causando problemas demais essa hora do dia!")
  else:
        print("Miles está mais livre e pode passar pra visitar sua mãe Rio em seu apartamento!")
elif spider_name == "Spider-Gwen":
  if machine_frequency >= 3000:
      print("Sabemos que a Gwen está mais habituada pra viajar entre Universos mas essa frequência é perigosa até para ela!!")
  elif machine_frequency >= 600:
      print("A Gwen deve ir dar um basta nas operações da Tinkerer, ajustaremos a Máquina para a Times Square!")
  else:
      print("A Gwen está liberada pra tomar Sorvete no Central Park, esse será seu Destino")
elif spider_name == "Miranha-Furacão":
  if machine_frequency > 0:
      print("A Carreta Furacão sai desgovernada pra animar mais uma rua em Cabrobó!")
  else:
      print("Mas o que é isso?! Esse bregueço deve ta quebrado, Miranha-Furacão, Pica-Pau, Pikachu, Mickey e Cascão vão continuar treinando seu número em casa!")
elif spider_name == "Homem-Aranha do PS4" or spider_name == "Homem-Funko-Pop":
  print("Maceió! Há rumores de um Vilão misterioso nas praias, alguns Aranhas devem ir pra lá!")
elif spider_name == "Porco-Aranha":
  print("O destino será a Fazendinha do Plaza!")
else:
  print("Quê?! Ou esse Aranha não existe ou não deve ser enviado em nenhuma missão pelo Dikastisverso!")
