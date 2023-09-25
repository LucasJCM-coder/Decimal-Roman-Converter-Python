# Conversor Decimal-Romano em Python

Este é um programa em Python que permite ao usuário converter números entre notação decimal e romana. O programa suporta três formas diferentes de entrada e saída:

1. Passagem de valores diretamente pelo terminal.
2. Leitura dos valores a partir de uma entrada padrão (stdin).
3. Leitura dos valores a partir de um arquivo de texto.

## Requisitos

Certifique-se de que você tenha o Python 3.x instalado em seu sistema para executar este programa.

## Como usar

Antes de executar o programa, certifique-se de conceder permissão de execução ao arquivo Python usando o comando `chmod +x`:

```bash
chmod +x src/main.py
```

Agora você pode usar o programa de acordo com as opções mencionadas anteriormente:

## Passagem de valores pelo terminal
Você pode passar um valor diretamente pelo terminal como um argumento. Aqui está um exemplo:

```nashorn js
./src/main.py <(echo '123')
```
Isso converterá o número 123 para notação romana e exibirá o resultado na saída padrão.

## Leitura dos valores a partir da entrada padrão (stdin)
Você também pode passar o valor através da entrada padrão (stdin) usando o seguinte comando:

```bash
echo '123' | ./src/main.py
```
Isso converterá o número 123 para notação romana e exibirá o resultado na saída padrão.

## Leitura dos valores a partir de um arquivo de texto
Você pode fornecer um arquivo de texto contendo valores a serem convertidos. Certifique-se de que o arquivo contenha um valor por linha. Use o seguinte comando para ler os valores de um arquivo:

```bash
./src/main.py --input-value=/path/arquivo.txt
```
O programa lerá os valores do arquivo especificado, converterá cada um deles para notação romana e exibirá os resultados na saída padrão.

## Testes
Este programa inclui testes para garantir a precisão das conversões, tanto de número para romano quanto de romano para número. Você pode executar os testes usando o seguinte comando na raiz do projeto:

```bash
python -m pytest test/ 
```
Certifique-se de que as dependências de teste estejam instaladas no seu ambiente.

## Exemplo de saídas
### Passagem de valores pelo terminal
A saída do programa será a representação romana do valor decimal fornecido. Por exemplo:

```bash
echo '123' | ./src/main.py
```
A saída será:

```bash
123 => CXXIII
```
### Leitura dos valores a partir de um arquivo
Caso seja passado um arquivo .txt com os valores abaixo:

```text
1
2
X
XV
100
```
ao rodarmos o comando:

```bash
./src/main.py --input-value=/caminho/arquivo.txt
```
a saída será:

```text
1 => I
2 => II
X => 10
XV => 15
100 => C
```
