import pandas as pd
import os
import glob

directory = "Participants"

for participant in os.listdir(directory): # loop through all the participant folders
    pID = participant.split("_")[1]
    
    # access data file
    file = glob.glob(directory + "/Pilot_" + pID + "/1 - QStarz BT-Q1000XT/*_data_reduced.csv", recursive = True)
    df = pd.read_csv(file[0])
    
    # combine time and date columns
    df[" UTC DATE TIME"] = df[" UTC DATE"] + df[" UTC TIME"]
    df[" LOCAL DATE TIME"] = df[" LOCAL DATE"] + df[" LOCAL TIME"]

    # add column with participant id
    df.insert(0, "Participant ID", participant)


    # remove redundant columns
    del df[" UTC DATE"]
    del df[" UTC TIME"]
    del df[" LOCAL DATE"]
    del df[" LOCAL TIME"]

    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_1_Qstarz_processed.csv")):

        df.to_csv("data_processing/ProcessedFiles/_1_Qstarz_processed.csv", mode='a', header=False, index= False)
    else:
        df.to_csv("data_processing/ProcessedFiles/_1_Qstarz_processed.csv", index=False)