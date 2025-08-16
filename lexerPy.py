import re

# tipos de tokens
TOKENS = [
    ("OPEN", r"open"),
    ("STRING", r'"[^"]*"'),
    ("WHITESPACE", r"\s+"),
]

def lexer(code):
    tokens = []
    while code:
        match = None
        for tok_type, pattern in TOKENS:
            regex = re.match(pattern, code)
            if regex:
                match = regex.group(0)
                if tok_type != "WHITESPACE":  # ignora espaços
                    tokens.append((tok_type, match))
                code = code[len(match):]
                break
        if not match:
            raise SyntaxError(f"Caractere inesperado: {code[0]}")
    return tokens
