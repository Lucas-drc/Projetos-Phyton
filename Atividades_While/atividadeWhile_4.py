usuario_correto = "admin"
senha_correta = "1234"
usuario = ""
senha = ""
descrip = """Bem vindo! Digite seu login e senha, por favor."""

print(descrip)

while usuario != usuario_correto or senha != senha_correta:
    usuario = input(f"Digite o nome de usuário:")
    senha = input(f"Digite sua senha:")

    if usuario != usuario_correto or senha != senha_correta:
        print(f"Usuário ou senha inválidos, tente novamente.")

    else:
        print(f"Login efetuado com sucesso!")

