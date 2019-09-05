arquivo = open("files/log_functions.log","a")

def test(print_word):
    arquivo.write(print_word+"\n")
    print(print_word)

test("Log Paluza")
test("Nome Paluza")