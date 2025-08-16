class ASTNode: pass

class OpenNode(ASTNode):
    def __init__(self, path):
        self.path = path

def parser(tokens):
    if not tokens:
        raise SyntaxError("Arquivo vazio ou nenhum token encontrado")
    if tokens[0][0] == "OPEN":
        if len(tokens) > 1 and tokens[1][0] == "STRING":
            path = tokens[1][1].strip('"')
            return OpenNode(path)
        else:
            raise SyntaxError("Esperado um caminho de arquivo após 'open'")
    else:
        raise SyntaxError("Comando desconhecido")