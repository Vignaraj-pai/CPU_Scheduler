# Priority Non-Preemptive Scheduling
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd  
import matplotlib.pyplot as plt
from operator import itemgetter

def PNP(arrival_times, burst_times, text_types):
    print("Priority Non-Preemptive Scheduling")
    process_data = []
    for i in range(len(arrival_times)):
        temporary = []
        process_id = "P" + str(i + 1)

        burst_time = burst_times[i]

        priority = int(input(f"Enter Priority for Process {process_id}: "))

        temporary.extend([process_id, 0, burst_time, priority])
        process_data.append(temporary)

    process_data.sort(key=lambda x: x[3], reverse=True)
    '''
    Sort according to Priority considering Higher the Value, Higher the Priority
    '''
    start_time = []
    exit_time = []
    s_time = 0
    for i in range(len(process_data)):
        start_time.append(s_time)
        s_time = s_time + process_data[i][2]
        e_time = s_time
        exit_time.append(e_time)
        process_data[i].append(e_time)

    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][4] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)

    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][5] - process_data[i][2]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)

    process_data.sort(key=lambda x: x[0])

    print("\nProcess_ID\tArrival_Time\tBurst_Time\tPriority\tCompletion_Time\tTurnaround_Time\tWaiting_Time")


    for i in range(len(process_data)):
        for j in range(len(process_data[i])):
            print(process_data[i][j], end="\t \t")
        print()

    print(f'Average Turnaround Time: {average_turnaround_time}')
    print(f'Average Waiting Time: {average_waiting_time}')
    
    # plot the gantt chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, exit_time[-1]], y=[0, 0], mode='lines', name='CPU'))
    for i in range(len(process_data)):
        fig.add_trace(go.Scatter(x=[start_time[i], exit_time[i]], y=[0, 0], mode='lines', name=process_data[i][0]))
        fig.add_trace(go.Scatter(x=[start_time[i], start_time[i]], y=[0, 1], mode='lines', name=process_data[i][0]))
        fig.add_trace(go.Scatter(x=[exit_time[i], exit_time[i]], y=[0, 1], mode='lines', name=process_data[i][0]))
    fig.update_layout(
        title='Gantt Chart',
        xaxis_title='Time',
        yaxis_title='Process',
        yaxis=dict(
            tickmode='array',
            tickvals=[0, 1],
            ticktext=['CPU', 'Process']
        ),
        showlegend=False
    )
    
    
    # save the gantt chart
    fig.write_image("output_images/pnp/gantt_chart_" + text_types + ".png")

