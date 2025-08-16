from lexerPy import lexer  # ou como você renomeou o lexer
from parserPy import parser      # seu parser
from interpreter import execute

def main():
    import sys
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.imglang")
        return

    filename = sys.argv[1]

    # abre o arquivo em modo binário e detecta encoding
    with open(filename, "rb") as f:
        raw = f.read()

    if raw.startswith(b'\xff\xfe'):          # UTF-16 LE
        code = raw.decode('utf-16')
    elif raw.startswith(b'\xfe\xff'):        # UTF-16 BE
        code = raw.decode('utf-16-be')
    else:                                    # UTF-8 padrão
        try:
            code = raw.decode('utf-8')
        except UnicodeDecodeError:
            code = raw.decode('latin1')      # fallback para Windows-1252

    print("Conteúdo lido do arquivo:")
    print(repr(code))  # só pra checar

    tokens = lexer(code)
    if not tokens:
        raise SyntaxError("Nenhum token encontrado. Verifique o arquivo.")
    
    ast = parser(tokens)
    execute(ast)

if __name__ == "__main__":
    main()
