import time

TAMANHO_TABULEIRO = 10


class Cores:
    RESET = "\033[0m"
    VERMELHO = "\033[91m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    AZUL = "\033[94m"
    MAGENTA = "\033[95m"
    CIANO = "\033[96m"
    NEGRITO = "\033[1m"


def mostrar_banner():
    print(f"{Cores.AZUL}{Cores.NEGRITO}")
    print("FLORESTA DE ANIMAIS")
    print(f"{Cores.RESET}")
    time.sleep(1)


def mostrar_tutorial():
    while True:
        print(f"\n{Cores.NEGRITO}{Cores.AZUL}=== TUTORIAL ==={Cores.RESET}\n")

        print("Objetivo: Simular uma floresta com animais interagindo.\n")
        time.sleep(0.5)
        print("Movimentacao:")
        print("- Tabuleiro 10x10")
        print("- Rodadas impares -> eixo Y")
        print("- Rodadas pares -> eixo X\n")
        time.sleep(0.5)
        print("Velocidade:")
        print("- Baseada no peso (mais pesado = mais lento)\n")
        time.sleep(0.5)
        print("Estamina:")
        print("- Diminui a cada movimento")
        print("- Ao zerar, o animal para\n")
        time.sleep(0.5)
        print("Conflitos:")
        print("- Mesmo local -> ocorre interacao")
        print("- Leao mata qualquer animal")
        print("- Leao vs Leao -> mais velho vence")
        print("- Cachorro mata gato")
        print("- Outros casos -> nada acontece\n")
        time.sleep(0.5)
        print("0 - Voltar")
        op = input(">> ")

        if op == "0":
            break


def mostrar_creditos():
    while True:
        print(f"\n{Cores.NEGRITO}{Cores.AZUL}=== CREDITOS ==={Cores.RESET}\n")

        print("Projeto: Floresta de Animais")
        time.sleep(0.5)
        print("Disciplina: POO\n")
        time.sleep(0.5)
        print("Desenvolvido por:")
        print("- Fabio Heitor Bezerra Pires")
        print("- Állef Braz da Silva Santos")
        print("- Isaías Marques da Silva")
        time.sleep(0.5)
        print("Professora:")
        print("- Priscilla Suene\n")
        time.sleep(0.5)
        print("Sistema baseado em conceitos de:")
        print("Heranca, Encapsulamento e Polimorfismo\n")
        time.sleep(0.5)
        print("0 - Voltar")
        op = input(">> ")

        if op == "0":
            break


def calcular_velocidade(peso):
    if peso > 150:
        return 1
    elif peso >= 80:
        return 2
    elif peso >= 30:
        return 3
    else:
        return 4


class Animal:
    def __init__(self, nome, cor, sexo, peso, estamina, x, y):
        self._nome = nome
        self._cor = cor
        self._sexo = sexo
        self._peso = peso
        self._velocidade = calcular_velocidade(peso)
        self.__estamina = estamina
        self._x = x
        self._y = y
        self._vivo = True
        self._dir_x = 1
        self._dir_y = 1

    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} fez um som.{Cores.RESET}")
        time.sleep(0.4)

    def checar_colisao(self, outro):
        return self._x == outro._x and self._y == outro._y

    @property
    def estamina(self):
        return self.__estamina

    @estamina.setter
    def estamina(self, valor):
        if valor >= 0:
            self.__estamina = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        if valor > 0:
            self._peso = valor
            self._velocidade = calcular_velocidade(valor)

    @property
    def nome(self):
        return self._nome

    def andar(self, rodada):
        if not self._vivo or self.estamina == 0:
            print(f"{Cores.VERMELHO}{self._nome} nao pode se mover.{Cores.RESET}")
            time.sleep(0.5)
            return

        print(f"{Cores.CIANO}{self._nome} esta se movendo...{Cores.RESET}")
        time.sleep(0.4)

        if rodada % 2 != 0:
            self._y += self._velocidade * self._dir_y
            if self._y >= TAMANHO_TABULEIRO:
                self._y = TAMANHO_TABULEIRO - 1
                self._dir_y *= -1
            elif self._y <= 0:
                self._y = 0
                self._dir_y *= -1
        else:
            self._x += self._velocidade * self._dir_x
            if self._x >= TAMANHO_TABULEIRO:
                self._x = TAMANHO_TABULEIRO - 1
                self._dir_x *= -1
            elif self._x <= 0:
                self._x = 0
                self._dir_x *= -1

        self.estamina -= 1

        print(f"{Cores.VERDE}{self._nome} andou para ({self._x}, {self._y}){Cores.RESET}")
        time.sleep(0.5)

    def __str__(self):
        return (f"{Cores.AMARELO}[{type(self).__name__}]{Cores.RESET} "
                f"{self._nome} | Pos: ({self._x},{self._y}) | "
                f"Peso: {self._peso} | Vel: {self._velocidade} | "
                f"Estamina: {self.estamina}")


class Leao(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, idade):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._idade = idade

    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} rugiu{Cores.RESET}")
        time.sleep(0.4)


class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, raca, idade):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._raca = raca
        self._idade = idade

    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} latiu{Cores.RESET}")
        time.sleep(0.4)


class Gato(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, raca):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._raca = raca

    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} miou{Cores.RESET}")
        time.sleep(0.4)


class Vaca(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, raca):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._raca = raca

    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} mugiu{Cores.RESET}")
        time.sleep(0.4)


class Lobo(Animal):
    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} uivou{Cores.RESET}")
        time.sleep(0.4)


class Coelho(Animal):
    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} correu{Cores.RESET}")
        time.sleep(0.4)


class Javali(Animal):
    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} grunhiu{Cores.RESET}")
        time.sleep(0.4)


class Urso(Animal):
    def fazer_som(self):
        print(f"{Cores.MAGENTA}{self._nome} rosnou{Cores.RESET}")
        time.sleep(0.4)


def verificar_colisoes(animais):
    copia = list(animais)

    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            a1 = copia[i]
            a2 = copia[j]

            if a1 not in animais or a2 not in animais:
                continue

            if a1._vivo and a2._vivo and a1.checar_colisao(a2):
                print(f"\n{Cores.NEGRITO}{Cores.AZUL}=== Encontro entre {a1.nome} e {a2.nome} ==={Cores.RESET}")
                time.sleep(0.5)
                resolver_conflito(a1, a2, animais)


def resolver_conflito(a1, a2, animais):
    a1.fazer_som()
    a2.fazer_som()
    time.sleep(0.5)

    if isinstance(a1, Leao) and not isinstance(a2, Leao):
        return matar(a1, a2, animais)

    if isinstance(a2, Leao) and not isinstance(a1, Leao):
        return matar(a2, a1, animais)

    if isinstance(a1, Leao) and isinstance(a2, Leao):
        return matar(a1, a2, animais) if a1._idade > a2._idade else matar(a2, a1, animais)

    if isinstance(a1, Cachorro) and isinstance(a2, Gato):
        return matar(a1, a2, animais)

    if isinstance(a2, Cachorro) and isinstance(a1, Gato):
        return matar(a2, a1, animais)

    print(f"{Cores.AMARELO}Nada aconteceu...{Cores.RESET}")
    time.sleep(0.5)


def matar(assassino, vitima, animais):
    vitima._vivo = False
    assassino.peso += 1

    if vitima in animais:
        animais.remove(vitima)

    print(f"{Cores.VERMELHO}{assassino.nome} matou {vitima.nome}!{Cores.RESET}")
    time.sleep(0.7)


def escolher_animal(animais):
    print(f"\n{Cores.NEGRITO}Escolha um animal:{Cores.RESET}")
    for i, a in enumerate(animais):
        print(f"{Cores.CIANO}{i}{Cores.RESET} - {a}")

    try:
        idx = int(input(">> "))
        if 0 <= idx < len(animais):
            return animais[idx]
    except:
        pass

    print(f"{Cores.VERMELHO}Escolha invalida.{Cores.RESET}")
    return None


def menu_get_set(animais):
    animal = escolher_animal(animais)
    if not animal:
        return

    while True:
        print(f"\n{Cores.NEGRITO}Atributos de {animal.nome}{Cores.RESET}")
        print("1 - Ver estamina")
        print("2 - Alterar estamina")
        print("3 - Ver peso")
        print("4 - Alterar peso")
        print("0 - Voltar")

        op = input(">> ")

        if op == "1":
            print(f"{Cores.VERDE}Estamina: {animal.estamina}{Cores.RESET}")
        elif op == "2":
            animal.estamina = int(input("Nova estamina: "))
        elif op == "3":
            print(f"{Cores.VERDE}Peso: {animal.peso}{Cores.RESET}")
        elif op == "4":
            animal.peso = int(input("Novo peso: "))
        elif op == "0":
            break


def main():
    mostrar_banner()

    animais = [
        Leao("Simba", "amarelo", "M", 150, 15, 5, 5, 8),
        Cachorro("Bolt", "marrom", "M", 30, 20, 2, 2, "vira-lata", 4),
        Gato("Mimi", "branco", "F", 10, 20, 1, 1, "siames"),
        Vaca("Mimosa", "branca", "F", 200, 10, 3, 3, "holandesa"),
        Lobo("Akira", "cinza", "M", 70, 15, 6, 6),
        Coelho("Pip", "cinza", "M", 5, 20, 8, 8),
        Javali("Brutus", "marrom", "M", 90, 15, 7, 7),
        Urso("Touro", "marrom", "M", 180, 10, 4, 4)
    ]

    rodada = 1

    while True:
        print(f"\n{Cores.NEGRITO}{Cores.AZUL}=== FLORESTA DE ANIMAIS ==={Cores.RESET}")
        print("1 - Movimentar animal")
        print("2 - Mostrar animais")
        print("3 - Acessar atributos")
        print("4 - Tutorial")
        print("5 - Creditos")
        print("0 - Sair")

        op = input(">> ")

        if op == "1":
            animal = escolher_animal(animais)
            if animal:
                animal.andar(rodada)
                verificar_colisoes(animais)

                print(f"\n{Cores.NEGRITO}Estado atual:{Cores.RESET}")
                for a in animais:
                    print(a)

                rodada += 1

        elif op == "2":
            for a in animais:
                print(a)

        elif op == "3":
            menu_get_set(animais)

        elif op == "4":
            mostrar_tutorial()

        elif op == "5":
            mostrar_creditos()

        elif op == "0":
            break


if __name__ == "__main__":
    main() 