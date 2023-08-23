import pandas as pd
import os
import glob

directory = "Participants"

for participant in os.listdir(directory): # loop through all the participant folders
    pID = participant.split("_")[1]

    result = pd.DataFrame()
    
    # access data file
    files = glob.glob(directory + "/Pilot_" + pID + '/2 - wGT3X_Accelerometer/*.csv', recursive = True)
    for file in files:
        if "bouts" in file.lower():
            print(file)
            df = pd.read_csv(file)
            result = result.append(df)

    
    # add column with participant id
    result.insert(0, "Participant ID", participant)
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_2_Accelerometer_processed.csv")):
        result.to_csv("data_processing/ProcessedFiles/_2_Accelerometer_processed.csv", mode='a', header=False, index= False)
    else:
        result.to_csv("data_processing/ProcessedFiles/_2_Accelerometer_processed.csv", index=False)