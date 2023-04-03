# First Come First Serve (FCFS)
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  
import matplotlib.pyplot as plt
from operator import itemgetter

def getList(dict):
    a = []
    for key in dict:
        a.append(key[0])
    return a
    
def FCFS(arrival_times, burst_times, text_type):
    print("\n\nFIRST COME FIRST SERVE SCHEDULLING")
    print("--------------------------------")
    n = len(arrival_times)
    d = dict()
    
    for i in range(n):
        key = "P"+str(i+1)
        a = arrival_times[i]
        b = burst_times[i]
        l = []
        l.append(a)
        l.append(b)
        d[key] = l
    
    d = sorted(d.items(), key=lambda item: item[1][0])
    
    ET = []
    for i in range(len(d)):
        # first process
        if(i==0):
            ET.append(d[i][1][1])
    
        # get prevET + newBT
        elif d[i][1][0] > ET[i-1]:
            ET.append(d[i][1][0] + d[i][1][1])
        else:
            ET.append(ET[i-1] + d[i][1][1])
    
    TAT = []
    for i in range(len(d)):
        TAT.append(ET[i] - d[i][1][0])
    
    WT = []
    for i in range(len(d)):
        WT.append(TAT[i] - d[i][1][1])
    
    avg_WT = 0
    for i in WT:
        avg_WT +=i
    avg_WT = (avg_WT/n)
    
    avg_TAT = 0
    for i in TAT:
        avg_TAT +=i
    avg_TAT = (avg_TAT/n)
    
    print("Process | Arrival | Burst | Completion | Turn Around | Wait |")
    for i in range(n):
        print("   ",d[i][0],"   |   ",d[i][1][0]," |    ",d[i][1][1]," |    ",ET[i],"  |    ",TAT[i],"  |   ",WT[i],"   |  ")
    
    print("Average Waiting Time: ",avg_WT)
    print("Average Turn Around Time: ",avg_TAT)

    
    df = pd.DataFrame({'Task': list(getList(d)), 'Start': [0] + ET[:-1], 'Finish': ET})
    
    fig = go.Figure()
    
    # Add trace for Gantt chart
    fig.add_trace(go.Bar(x=df['Task'], y=df['Finish']-df['Start'], base=df['Start'],
                         marker={'color': 'lightskyblue'}, name='Task Duration'))
    
    # Update layout for Gantt chart
    fig.update_layout(xaxis={'title': 'Time'}, yaxis={'title': 'Task'}, title='FCFS Gantt Chart')
    

    # Save plot
    fig.write_image('output_images/fcfs/FCFS_gantt_'+ text_type + '.png')