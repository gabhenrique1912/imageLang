from PIL import Image

def execute(node):
    if node.__class__.__name__ == "OpenNode":
        print(f"Abrindo imagem: {node.path}")
        img = Image.open(node.path)
        img.show()  # abre no visualizador padrão do sistema
        return img
    else:
        raise RuntimeError("Comando não implementado")
