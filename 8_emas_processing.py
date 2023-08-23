import pandas as pd
import os
import glob

directory = "Participants"

for participant in os.listdir(directory): # loop through all the participant folders
    pID = participant.split("_")[1]

    result = pd.DataFrame() 

    # access data file
    files = glob.glob(directory + "/Pilot_" + pID + '/8 - EcoEmoTracker/*.csv', recursive = True)
    result = pd.DataFrame()
    
    for file in files:
        if "ema" in file.lower():

            df = pd.read_csv(file, engine='python')
            
            result = result.append(df[["Participant ID", "Survey ID", "Form ID", "Response date"]])

    
    # add column with participant id 
    result.insert(0, "Participant ID", participant)
    result['Response.time'] = result['Response.date'].str.split(" ", expand=True)[1]
    result['Response.day'] = result['Response.date'].str.split(" ", expand=True)[0]
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_8_EMAs_processed.csv")):
        result.to_csv("data_processing/ProcessedFiles/_8_EMAs_processed.csv", mode='a', header=False, index= False)
    else:
        result.to_csv("data_processing/ProcessedFiles/_8_EMAs_processed.csv", index=False)

    break