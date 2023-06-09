rm output_images/*
rm screenshots/*
clear

python3 index.py < input_texts/fcfs/long.txt
clear
import -window root screenshots/fcfs/long.png

python3 index.py < input_texts/fcfs/medium.txt
clear
import -window root screenshots/fcfs/medium.png

python3 index.py < input_texts/fcfs/short.txt
clear
import -window root screenshots/fcfs/short.png

python3 index.py < input_texts/sjf/long.txt
clear
import -window root screenshots/sjf/long.png

python3 index.py < input_texts/sjf/medium.txt
clear
import -window root screenshots/sjf/medium.png

python3 index.py < input_texts/sjf/short.txt
clear
import -window root screenshots/sjf/short.png

python3 index.py < input_texts/srtf/long.txt
clear
import -window root screenshots/srtf/long.png

python3 index.py < input_texts/srtf/medium.txt
clear
import -window root screenshots/srtf/medium.png

python3 index.py < input_texts/srtf/short.txt
clear
import -window root screenshots/srtf/short.png

python3 index.py < input_texts/rr/long.txt
clear
import -window root screenshots/rr/long.png

python3 index.py < input_texts/rr/medium.txt
clear
import -window root screenshots/rr/medium.png

python3 index.py < input_texts/rr/short.txt
clear
import -window root screenshots/rr/short.png

python3 index.py < input_texts/pnp/long.txt
clear
import -window root screenshots/pnp/long.png

python3 index.py < input_texts/pnp/medium.txt
clear
import -window root screenshots/pnp/medium.png

python3 index.py < input_texts/pnp/short.txt
clear
import -window root screenshots/pnp/short.png

python3 index.py < input_texts/pp/long.txt
clear
import -window root screenshots/pp/long.png

python3 index.py < input_texts/pp/medium.txt
clear
import -window root screenshots/pp/medium.png

python3 index.py < input_texts/pp/short.txt
clear
import -window root screenshots/pp/short.png