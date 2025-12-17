from parser import NumNode, BinOpNode

class Interpreter:
    def evaluate(self, node):
        """Avalia a AST e retorna o valor numérico da expressão."""
        if isinstance(node, NumNode):
            return node.value
        
        elif isinstance(node, BinOpNode):
            left_val = self.evaluate(node.left)
            right_val = self.evaluate(node.right)
            
            if node.op == '+':
                return left_val + right_val
            elif node.op == '*':
                return left_val * right_val
            else:
                raise Exception(f"Operador desconhecido: {node.op}")
        
        else:
            raise Exception(f"Nó AST desconhecido: {type(node)}")