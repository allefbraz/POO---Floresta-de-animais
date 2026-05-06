
# Floresta de Animais

Simulação interativa de uma floresta onde diferentes animais se movimentam, interagem e entram em conflito com base em regras definidas.

---

## Link da apresentação Canva

https://canva.link/bbkmbls2w45f49j

---

## Descrição

Este projeto foi desenvolvido com o objetivo de aplicar conceitos de Programação Orientada a Objetos (POO) em Python, utilizando uma simulação de um ecossistema simplificado.

Cada animal possui características próprias como peso, estamina e velocidade, podendo se mover pelo ambiente e interagir com outros animais ao ocupar a mesma posição.

---

## Objetivos do Projeto

* Aplicar conceitos fundamentais de Programação Orientada a Objetos
* Criar interação entre objetos
* Simular regras de comportamento em um sistema dinâmico
* Desenvolver uma interface em terminal

---

## Conceitos de POO Utilizados

### Herança

A classe `Animal` serve como base para as demais classes:

* Leão
* Cachorro
* Gato
* Vaca
* Lobo
* Coelho
* Javali
* Urso

---

### Encapsulamento

* Uso de atributos protegidos (`_atributo`)
* Uso de atributo privado (`__estamina`)
* Métodos `@property` e `@setter` para controle de acesso

---

### Polimorfismo

O método `fazer_som()` é sobrescrito por cada classe, permitindo comportamentos distintos com a mesma interface.

---

## Funcionamento do Sistema

### Ambiente

* Tabuleiro de dimensão 10x10
* Cada animal possui uma posição representada por coordenadas `(x, y)`

---

### Movimentação

* A cada rodada, um animal é movimentado
* Rodadas ímpares movimentam no eixo Y
* Rodadas pares movimentam no eixo X
* A velocidade do animal depende do seu peso

---

### Estamina

* Reduz a cada movimento realizado
* Quando chega a zero, o animal não pode mais se mover

---

### Interações e Conflitos

Quando dois animais ocupam a mesma posição:

* O leão vence qualquer outro animal
* Em confronto entre leões, vence o mais velho
* O cachorro vence o gato
* Nos demais casos, não ocorre conflito

---

## Menu do Sistema

O sistema possui um menu interativo com as seguintes opções:

```python
1 - Movimentar animal
2 - Mostrar animais
3 - Acessar atributos
4 - Tutorial
5 - Créditos
0 - Sair
```

---

## Funcionalidades

* Movimentação de animais no ambiente
* Sistema de detecção de colisões
* Regras de combate entre animais
* Alteração de atributos (peso e estamina)
* Exibição de informações dos animais
* Menu com tutorial e créditos
* Uso de cores para melhor visualização no terminal

---

## Tecnologias Utilizadas

* Python 3
* Biblioteca padrão `time`

---

## Autores

* Fábio Heitor Bezerra Pires
* Állef Braz da Silva Santos
* Isaías Marques da Silva

---

## Orientação

* Professora: Priscilla Suene

---

## Observações

Este projeto foi desenvolvido com fins educacionais como atividade da disciplina de Programação Orientada a Objetos.

