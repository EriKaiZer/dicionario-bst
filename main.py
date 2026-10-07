class NoTermo:
    def __init__(self, palavra, definicao):
        self.palavra = palavra.strip().lower()
        self.definicao = definicao.strip()
        self.esquerda = None
        self.direita = None


class DicionarioBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, palavra, definicao):
        novo = NoTermo(palavra, definicao)

       
        if self.raiz is None:
            self.raiz = novo
            return

        atual = self.raiz
        while True:
            if novo.palavra == atual.palavra:
               
                atual.definicao = novo.definicao
                return
            elif novo.palavra < atual.palavra:
                
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita

    def buscar(self, palavra):
        palavra = palavra.strip().lower()
        atual = self.raiz

        while atual is not None:
            if palavra == atual.palavra:
                return atual.definicao
            elif palavra < atual.palavra:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return "Termo não encontrado."

    def listar_alfabetico(self):
        if self.raiz is None:
            print("O glossário está vazio.")
        else:
            self._em_ordem(self.raiz)

    def _em_ordem(self, no_atual):
        if no_atual is not None:
           
            self._em_ordem(no_atual.esquerda)
            print(f"{no_atual.palavra}: {no_atual.definicao}")
            self._em_ordem(no_atual.direita)


def main():
    dicionario = DicionarioBST()

    while True:
        print("\n=== GLOSSÁRIO TÉCNICO DE TI ===")
        print("1. Cadastrar termo")
        print("2. Buscar termo")
        print("3. Listar todos os termos (A-Z)")
        print("4. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            palavra = input("Palavra: ").strip()
            definicao = input("Definição: ").strip()

            if not palavra or not definicao:
                print("Preencha a palavra e a definição.")
                continue

            dicionario.inserir(palavra, definicao)
            print("Termo cadastrado ou atualizado com sucesso!")
        elif opcao == "2":
            palavra = input("Termo para busca: ")
            print(f"Resultado: {dicionario.buscar(palavra)}")
        elif opcao == "3":
            print("\n--- Glossário ---")
            dicionario.listar_alfabetico()
        elif opcao == "4" or opcao == "0":
            
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
