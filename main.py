import sys
sys.path.insert(0, './aluno1')
sys.path.insert(0, './aluno2')
sys.path.insert(0, './aluno3')
from aluno1 import soma,subtracao
from aluno2 import multiplicacao,divisao
from aluno3 import exponencia

while True:
    try:
        v1 = float(input("Insira o primeiro valor: "))
        v2 = float(input("Insira o segundo valor: "))
        operacoes = {"+":soma(v1,v2),
                "-":subtracao(v1,v2),
                "*":multiplicacao(v1,v2),
                "/":divisao(v1,v2)
                "**":exponencia(v1,v2)}
        op = input("Insira a operação (+.-,*,/, **): ")
        print(operacoes[op])
    except ValueError:
        print("Valor inválido")
    except KeyError:
        print("Operação inválida")
    except KeyboardInterrupt:
        print("\nSaindo...")
        break