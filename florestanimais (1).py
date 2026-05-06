TAMANHO_TABULEIRO = 10


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
        print(f"{self._nome} fez um som.")

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
            print(f"{self._nome} não pode se mover.")
            return

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
        print(f"{self._nome} andou para ({self._x}, {self._y})")

    def __str__(self):
        return f"[{type(self).__name__}] {self._nome} | Pos: ({self._x},{self._y}) | Peso: {self._peso} | Vel: {self._velocidade} | Estamina: {self.estamina}"


class Leao(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, idade):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._idade = idade

    def fazer_som(self):
        print(f"{self._nome} rugiu.")


class Cachorro(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, raca, idade):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._raca = raca
        self._idade = idade

    def fazer_som(self):
        print(f"{self._nome} latiu.")


class Gato(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, raca):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._raca = raca

    def fazer_som(self):
        print(f"{self._nome} miou.")


class Vaca(Animal):
    def __init__(self, nome, cor, sexo, peso, estamina, x, y, raca):
        super().__init__(nome, cor, sexo, peso, estamina, x, y)
        self._raca = raca

    def fazer_som(self):
        print(f"{self._nome} mugiu.")


class Lobo(Animal):
    def fazer_som(self):
        print(f"{self._nome} uivou.")


class Coelho(Animal):
    def fazer_som(self):
        print(f"{self._nome} correu.")


class Javali(Animal):
    def fazer_som(self):
        print(f"{self._nome} grunhiu.")


class Urso(Animal):
    def fazer_som(self):
        print(f"{self._nome} rosnou.")


def verificar_colisoes(animais):
    copia = list(animais)

    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            a1 = copia[i]
            a2 = copia[j]

            if a1 not in animais or a2 not in animais:
                continue

            if a1._vivo and a2._vivo:
                if a1.checar_colisao(a2):
                    print(f"\nEncontro entre {a1.nome} e {a2.nome}")
                    resolver_conflito(a1, a2, animais)


def resolver_conflito(a1, a2, animais):
    a1.fazer_som()
    a2.fazer_som()

    if isinstance(a1, Leao) and not isinstance(a2, Leao):
        return matar(a1, a2, animais)

    if isinstance(a2, Leao) and not isinstance(a1, Leao):
        return matar(a2, a1, animais)

    if isinstance(a1, Leao) and isinstance(a2, Leao):
        if a1._idade > a2._idade:
            return matar(a1, a2, animais)
        else:
            return matar(a2, a1, animais)

    regras = {
        Cachorro: [Gato, Vaca],
        Gato: [Coelho],
        Lobo: [Coelho, Gato],
        Javali: [Coelho, Gato],
        Urso: [Lobo, Javali, Vaca]
    }

    for predador in regras:
        if isinstance(a1, predador) and any(isinstance(a2, presa) for presa in regras[predador]):
            return matar(a1, a2, animais)

        if isinstance(a2, predador) and any(isinstance(a1, presa) for presa in regras[predador]):
            return matar(a2, a1, animais)

    if a1.peso >= a2.peso:
        matar(a1, a2, animais)
    else:
        matar(a2, a1, animais)


def matar(assassino, vitima, animais):
    vitima._vivo = False
    assassino.peso += 1

    if vitima in animais:
        animais.remove(vitima)

    print(f"{assassino.nome} matou {vitima.nome}")


def escolher_animal(animais):
    for i, a in enumerate(animais):
        print(f"{i} - {a}")

    try:
        idx = int(input("Escolha o número: "))
        if 0 <= idx < len(animais):
            return animais[idx]
    except:
        pass

    print("Escolha inválida.")
    return None


def menu_get_set(animais):
    animal = escolher_animal(animais)
    if not animal:
        return

    while True:
        print(f"\nAtributos de {animal.nome}")
        print("1 - Ver estamina")
        print("2 - Alterar estamina")
        print("3 - Ver peso")
        print("4 - Alterar peso")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":
            print(f"Estamina: {animal.estamina}")
        elif op == "2":
            valor = int(input("Nova estamina: "))
            animal.estamina = valor
        elif op == "3":
            print(f"Peso: {animal.peso}")
        elif op == "4":
            valor = int(input("Novo peso: "))
            animal.peso = valor
        elif op == "0":
            break


def main():
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
        print("\n=== FLORESTA DE ANIMAIS ===")
        print("1 - Movimentar animal")
        print("2 - Mostrar animais")
        print("3 - Acessar atributos")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            animal = escolher_animal(animais)
            if animal:
                animal.andar(rodada)
                verificar_colisoes(animais)
                rodada += 1

        elif op == "2":
            for a in animais:
                print(a)

        elif op == "3":
            menu_get_set(animais)

        elif op == "0":
            break


if __name__ == "__main__":
    main()