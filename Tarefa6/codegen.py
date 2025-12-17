from parser import NumNode, BinOpNode

class CodeGenerator:
    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        """
        Gera código de três endereços a partir da AST.
        Retorna o nome do temporário (ou valor literal) onde o resultado está.
        """

        # Caso: número
        if isinstance(node, NumNode):
            return str(node.value)

        # Caso: operação binária
        elif isinstance(node, BinOpNode):
            left_place = self.generate(node.left)
            right_place = self.generate(node.right)

            temp = self.new_temp()
            self.code.append(
                f"{temp} = {left_place} {node.op} {right_place}"
            )
            return temp
        else:
            raise Exception("Nó desconhecido na geração de código")

    def get_code(self):
        return self.code
