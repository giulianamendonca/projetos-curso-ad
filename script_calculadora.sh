#!/bin/bash

# cria o script calculadora.sh
nano calculadora.sh

# edita as permissões do arquivo para torná-lo executável e restringir a edição
chmod 733 calculadora.sh

# instala Python (SN), para permitir a execução da calculadora
sudo apt install python3

python3 ../modulo_1/calculadora.py



