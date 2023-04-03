import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  
import matplotlib.pyplot as plt
from operator import itemgetter


def SRTF(arrival_times, burst_times):
    print("SHORTEST REMAINING TIME FIRST SCHEDULLING")
    process_data = []
    for i in range(len(arrival_times)):
        temporary = []
        process_id = "P" + str(i + 1)
        arrival_time = arrival_times[i]
        burst_time = burst_times[i]
        temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])

        process_data.append(temporary)
        
    start_time = []
    exit_time = []
    s_time = 0
    sequence_of_process = []
    process_data.sort(key=lambda x: x[1])

    while 1:
        ready_queue = []
        normal_queue = []
        temp = []
        for i in range(len(process_data)):
            if process_data[i][1] <= s_time and process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                ready_queue.append(temp)
                temp = []
            elif process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])

            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(ready_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                process_data[k][3] = 1
                process_data[k].append(e_time)
        if len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(normal_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:        #If Burst Time of a process is 0, it means the process is completed
                process_data[k][3] = 1
                process_data[k].append(e_time)
                
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][5] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)

    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][4]

        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)

    print("Process_ID \tArrival_Time\tRem_Burst_Time\tCompleted\tOrig_Burst_Time\tCompletion_Time\tTurnaround_Time\tWaiting_Time")
    for i in range(len(process_data)): 
        for j in range(len(process_data[i])):
            print(process_data[i][j], end="\t\t")
        print()
    print(f'Average Turnaround Time: {average_turnaround_time}')
    print(f'Average Waiting Time: {average_waiting_time}')
    print(f'Sequence of Process: {sequence_of_process}')

    # Plotting Gantt Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, start_time[0]], y=[0, 0], mode='lines', name=sequence_of_process[0]))
    for i in range(1, len(start_time)):
        fig.add_trace(go.Scatter(x=[start_time[i-1], start_time[i]], y=[0, 0], mode='lines', name=sequence_of_process[i]))
    fig.update_layout(title='Gantt Chart', xaxis_title='Time', yaxis_title='Process')
    
    # save the figure
    fig.write_image("output_images/SRTF_gantt.png")