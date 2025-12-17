from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator
from interpreter import Interpreter

def main():
    while True:
        try:
            text = input(">> ")

            if text == "exit":
                print("Saindo...")
                break

            lexer = Lexer(text)
            parser = Parser(lexer)
            ast = parser.parse()

            codegen = CodeGenerator()
            result = codegen.generate(ast)

            print("\nCódigo de três endereços:")
            for line in codegen.get_code():
                print(line)

            interpreter = Interpreter()
            finalResult = interpreter.evaluate(ast)

            print(f"\nResultado final em: {result} = {finalResult}\n")

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()