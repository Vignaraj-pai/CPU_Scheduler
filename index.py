# Menu driven program implementing various CPU scheduling algorithms
# 1. First Come First Serve (FCFS)
# 2. Shortest Job First (SJF)
# 3. Shortest Remaining Time First (SRTF)
# 4. Round Robin (RR)
# 5. Priority non-preemptive 
# 6. Priority preemptive

from fcfs import FCFS
from sjf import SJF
from srtf import SRTF
from rr import RR
from pnp import PNP
from pp import PP
import sys

Switcher = {
    1 : FCFS,
    2 : SJF,
    3 : SRTF,
    4 : RR,
    5 : PNP,
    6 : PP
}


def switch(choice, arrival_times, burst_times, text_type):
    return Switcher.get(choice, lambda: "Invalid choice")(arrival_times, burst_times, text_type)

if __name__ == "__main__":
    
    text_type = input("Enter input type : (long, medium, short first? )");
    
    N = int(input("Enter number of processes: "))

    arrival_times = []

    for i in range(N):
        arrival_times.append(int(input("Enter arrival time of process {}: ".format(i+1))))

    burst_times = []
    
    for i in range(N):
        burst_times .append(int(input("Enter burst time of process {}: ".format(i+1))))

    switch(int(input("Enter choice: ")), arrival_times, burst_times, text_type)

