### IMPORTING ###
from os import listdir, chdir
from os.path import isfile
chdir("C:\\Users\\annal\\Downloads\\BACS1SE_practice") # set working directory to responses folder
allfiles = [f for f in listdir() if isfile(f)] # get all file names

import pandas as pd
all_data = []
column_names = ['trial_type', 'time_elapsed', 'internal_node_id', 'sbj_ID', 'study_id', 'session_id', 'rt', 'response', 'stimulus', 'slider_start', 'character1', 'character2', 'name']
for f in allfiles:
    df = pd.read_csv(f, index_col=1) # separate into each line
    temp = df.to_dict("split")
    temp = dict(zip(temp["index"], temp["data"]))
    temp_length = len(temp.values())
    for x in range(temp_length): # replace response by column: reponse dictionary
        values = [i for i in temp.values()]
        value = values[x]
        value2 = {column_names[x]: value[x] for x in range(len(column_names))}
        temp[x] = value2
    all_data.append(temp)
    
### DEMOGRAPHIC QUESTIONNAIRE ###
import json
demo_data = []
for x in range(len(all_data)): # extract demographic responses
    participant_data = all_data[x]
    participant_demo_data = []
    for y in participant_data.keys():
        line = participant_data[y]
        if line['trial_type'] == 'survey-html-form':
            response_line = json.loads(line['response']) # convert from string to dict
            if  'consent1' not in response_line.keys():
                participant_demo_data.append(response_line)
    demo_data.append(participant_demo_data)
    
demo_dataframe = pd.DataFrame()
for participantn in range(len(demo_data)):
    participant_data = demo_data[participantn]
    sbj_ID = participant_data[0]['ID']
    participant_data = {k:[v] for k,v in participant_data[1].items()} # avoiding index error
    participant_data = pd.DataFrame(participant_data)
    participant_data.insert(0, 'sbj_ID', sbj_ID)
    demo_dataframe = pd.concat([demo_dataframe, participant_data])
    
### SIMILARITY TASK ###
similarity_data = []
for x in range(len(all_data)): # extract demographic responses
    participant_data = all_data[x]
    participant_similarity_data = []
    for y in participant_data.keys():
        line = participant_data[y]
        if line['trial_type'] == 'html-slider-response':
            participant_similarity_data.append(line)
    similarity_data.append(participant_similarity_data)