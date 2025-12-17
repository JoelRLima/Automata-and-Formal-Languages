import re

class TokenType:
    NUM = "NUM"
    PLUS = "PLUS"
    TIMES = "TIMES"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    EOF = "EOF"

class Token:
    def __init__(self, type_, value=None, position=0):
        self.type = type_
        self.value = value
        self.position = position

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, pos={self.position})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

        # REGEX
        self.rules = [
            (TokenType.NUM,    re.compile(r'\d+')),
            (TokenType.PLUS,   re.compile(r'\+')),
            (TokenType.TIMES,  re.compile(r'\*')),
            (TokenType.LPAREN, re.compile(r'\(')),
            (TokenType.RPAREN, re.compile(r'\)')),
        ]

    def next_token(self):
        # Ignorar espaços
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return Token(TokenType.EOF, position=self.pos)

        # Verifica as regras
        for token_type, regex in self.rules:
            match = regex.match(self.text, self.pos)
            if match:
                start = self.pos
                lexeme = match.group(0)
                self.pos = match.end()
                
                if token_type == TokenType.NUM:
                    value = int(lexeme)
                else:
                    value = lexeme

                return Token(token_type, value, start)

        # Erro léxico
        raise Exception(
            f"Erro léxico: caractere inválido '{self.text[self.pos]}' na posição {self.pos}"
        )
