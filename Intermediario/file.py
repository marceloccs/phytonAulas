arquivo = open("files/test.txt")
path = "files/"
nome_arquivo_nome = "testes.txt"

arquivo_info = arquivo.readlines()

print(arquivo_info)

w = open(path + nome_arquivo_nome,"a")
w.write("\nLollas paluzas")
w.close()