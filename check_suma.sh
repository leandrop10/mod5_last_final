#!/usr/bin/bash
# Este script busca encontrar cuando la suma de dos números entre 0 y 100 de como resultado un número menor a 20

SUMA=$((/usr/bin/python3 /home/ubuntu/mod5_last_final/test_randomsum.py) | awk '{ print $9 }')
DATE=$(date)

echo $DATE >> /home/ubuntu/mod5_last_final/log.txt

if [ $SUMA -lt 20 ];
then
	echo "La suma dio $SUMA. Es menor que 20!!" >> log.txt
else 
	echo "Sigue intentando, la suma dio $SUMA" >> log.txt
fi
