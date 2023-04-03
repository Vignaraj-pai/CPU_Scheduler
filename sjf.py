import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  
import matplotlib.pyplot as plt
from operator import itemgetter

def SJF(arrival_times, burst_times, text_type):
    print("SHORTEST JOB FIRST SCHEDULLING")
    process_data = []
    for i in range(len(arrival_times)):
        temporary = []
        process_id = "P" + str(i + 1)

        arrival_time = arrival_times[i]

        burst_time = burst_times[i]
        temporary.extend([process_id, arrival_time, burst_time, 0])

        process_data.append(temporary)

    start_time = []
    exit_time = []
    s_time = 0
    process_data.sort(key=lambda x: x[1])
    for i in range(len(process_data)):
        ready_queue = []
        temp = []
        normal_queue = []

        for j in range(len(process_data)):
            if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                ready_queue.append(temp)
                temp = []
            elif process_data[j][3] == 0:
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
            '''
            Sort the processes according to the Burst Time
            '''
            start_time.append(s_time)
            s_time = s_time + ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][3] = 1
            process_data[k].append(e_time)

        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time = s_time + normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][3] = 1
            process_data[k].append(e_time)

    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][4] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)
    '''
    average_turnaround_time = total_turnaround_time / no_of_processes
    '''

    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][5] - process_data[i][2]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)


    print("Process ID\tArrival Time\tBurst Time\tCompleted\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            print(process_data[i][j], end="\t\t")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')

    print(f'Average Waiting Time: {average_waiting_time}')

    # Plotting the Gantt Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0], y=[0], mode='text', text='0'))
    for i in range(len(process_data)):
        fig.add_trace(go.Scatter(x=[start_time[i], exit_time[i]], y=[0, 0], mode='lines+text', name=process_data[i][0],
                                 text=[process_data[i][0], process_data[i][4]], textposition='top center'))
    fig.update_layout(title='Gantt Chart', xaxis_title='Time', yaxis_title='Processes')
    fig.write_image("output_images/sjf_gantt" + text_type + ".png")
                  