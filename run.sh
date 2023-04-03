rm output_images/*
rm screenshots/*
clear

python3 index.py < fcfs/long.txt
clear
import -window root screenshots/fcfs/long.png

python3 index.py < fcfs/medium.txt
clear
import -window root screenshots/fcfs/medium.png

python3 index.py < fcfs/short.txt
clear
import -window root screenshots/fcfs/short.png

python3 index.py < sjf/long.txt
clear
import -window root screenshots/sjf/long.png

python3 index.py < sjf/medium.txt
clear
import -window root screenshots/sjf/medium.png

python3 index.py < sjf/short.txt
clear
import -window root screenshots/sjf/short.png

python3 index.py < srtf/long.txt
clear
import -window root screenshots/srtf/long.png

python3 index.py < srtf/medium.txt
clear
import -window root screenshots/srtf/medium.png

python3 index.py < srtf/short.txt
clear
import -window root screenshots/srtf/short.png

python3 index.py < rr/long.txt
clear
import -window root screenshots/rr/long.png

python3 index.py < rr/medium.txt
clear
import -window root screenshots/rr/medium.png

python3 index.py < rr/short.txt
clear
import -window root screenshots/rr/short.png

python3 index.py < pnp/long.txt
clear
import -window root screenshots/pnp/long.png

python3 index.py < pnp/medium.txt
clear
import -window root screenshots/pnp/medium.png

python3 index.py < pnp/short.txt
clear
import -window root screenshots/pnp/short.png

python3 index.py < pp/long.txt
clear
import -window root screenshots/pp/long.png

python3 index.py < pp/medium.txt
clear
import -window root screenshots/pp/medium.png

python3 index.py < pp/short.txt
clear
import -window root screenshots/pp/short.png