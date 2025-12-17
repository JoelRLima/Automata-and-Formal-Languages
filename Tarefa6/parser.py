from lexer import TokenType

# Nós da árvore sintática
class NumNode: 
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Num({self.value})"


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op   
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op} {self.right})"

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.next_token()

    def error(self, msg="Erro sintático"):
        raise Exception(f"Erro sintático: {msg} na posição {self.current_token.position}")


    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.next_token()
        else:
            self.error(f"Esperado token '{token_type}', encontrado '{self.current_token.type}'")

    # GRAMÁTICA (E, E', T, T', F)

    def parse_E(self):
        node = self.parse_T()
        node = self.parse_Ep(node)
        return node

    def parse_Ep(self, left):
        if self.current_token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            right = self.parse_T()
            new_left = BinOpNode(left, '+', right)
            return self.parse_Ep(new_left)
        else:
            return left  # produção ε

    def parse_T(self):
        node = self.parse_F()
        node = self.parse_Tp(node)
        return node

    def parse_Tp(self, left):
        if self.current_token.type == TokenType.TIMES:
            self.eat(TokenType.TIMES)
            right = self.parse_F()
            new_left = BinOpNode(left, '*', right)
            return self.parse_Tp(new_left)
        else:
            return left  # produção ε

    def parse_F(self):
        tok = self.current_token

        if tok.type == TokenType.NUM:
            self.eat(TokenType.NUM)
            return NumNode(tok.value)

        elif tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.parse_E()
            self.eat(TokenType.RPAREN)
            return node

        else:
            self.error("Token inesperado em F()")

    # Função principal
    def parse(self):
        node = self.parse_E()

        if self.current_token.type != TokenType.EOF:
            self.error("Tokens sobrando após o fim da expressão")

        return node
