import pandas as pd
import os

directory = "Participants"

for participant in os.listdir(directory): # loop through all the participant folders
    pID = participant.split("_")[1]

    # access data file
    df = pd.read_csv(directory + "/Pilot_" + pID + "/4 - PCE-HT 72 Hygrometer/" + pID + "p.CSV")

    # remove unnecessary column
    del df["Number"]

    # add column with participant id
    df.insert(0, "Participant ID", participant)
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_4_Hygrometer_processed.csv")):
        df.to_csv("data_processing/ProcessedFiles/_4_Hygrometer_processed.csv", mode='a', header=False, index= False)
    else:
        df.to_csv("data_processing/ProcessedFiles/_4_Hygrometer_processed.csv", index=False)
