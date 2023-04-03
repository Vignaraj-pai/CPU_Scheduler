# Priority Preemptive Scheduling Algorithm
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  
import matplotlib.pyplot as plt
from operator import itemgetter

def PP(arrival_times, burst_times, text_type):
    process_data = []
    for i in range(len(arrival_times)):
        temporary = []
        process_id = "P" + str(i + 1)

        arrival_time = arrival_times[i]

        burst_time = burst_times[i]

        priority = int(input(f"Enter Priority for Process {process_id}: "))

        temporary.extend([process_id, arrival_time, burst_time, priority, 0, burst_time])

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
            if process_data[i][1] <= s_time and process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][3],
                                process_data[i][5]])
                ready_queue.append(temp)
                temp = []
            elif process_data[i][4] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4],
                                process_data[i][5]])
                normal_queue.append(temp)
                temp = []
        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break
        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[3], reverse=True)
            start_time.append(s_time)
            s_time = s_time + 1
            e_time = s_time
            exit_time.append(e_time)
            sequence_of_process.append(ready_queue[0][0])
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][2] = process_data[k][2] - 1
            if process_data[k][2] == 0:       #if burst time is zero, it means process is completed
                process_data[k][4] = 1
                process_data[k].append(e_time)
        if len(ready_queue) == 0:
            normal_queue.sort(key=lambda x: x[1])
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
            if process_data[k][2] == 0:        #if burst time is zero, it means process is completed
                process_data[k][4] = 1
                process_data[k].append(e_time)


    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][6] - process_data[i][5]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)



    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][2]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)



    process_data.sort(key=lambda x: x[0])
    '''
    Sort processes according to the Process ID
    '''
    print("Process_ID  Arrival_Time  Rem_Burst_Time   Priority        Completed  Orig_Burst_Time Completion_Time  Turnaround_Time  Waiting_Time")
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            print(process_data[i][j], end="\t\t")
        print()


    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')

    print(f'Sequence of Process: {sequence_of_process}')
    
    #plotting the gantt chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='text', text='0'))
    for i in range(len(sequence_of_process)):
        fig.add_trace(go.Scatter(x=[start_time[i], exit_time[i]], y=[0, 0], mode='lines', name=sequence_of_process[i]))
        fig.add_trace(go.Scatter(x=[exit_time[i]], y=[0], mode='text', text=exit_time[i]))
    fig.update_layout(title='Gantt Chart', xaxis_title='Time', yaxis_title='Process')
    
    # save figure
    fig.write_image("output_images/pp/gantt_chart_" + text_type + ".png")