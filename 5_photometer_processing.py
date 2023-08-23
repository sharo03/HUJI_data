import pandas as pd
import datetime as dt

import os

directory = "Participants"

for participant in os.listdir(directory): # loop through all participant folders
    pID = participant.split("_")[1]

    # access data files
    df = pd.read_csv(directory + "/Pilot_" + pID + "/5 - HOBO Photometer/" + pID + "p.csv", skiprows=[0])

    # convert to 24 hour time
    df["Time, GMT+03:00"] = pd.to_datetime(df["Time, GMT+03:00"]).dt.strftime('%H:%M:%S')

    # combine date and time columns
    df["GMT+03:00 DATE TIME"] = df["Date"] + " " + df["Time, GMT+03:00"]

    # remove redundant columns
    del df["Time, GMT+03:00"]
    del df["Date"]
    del df["#"]

    # add column with participant id
    df.insert(0, "Participant ID", participant)
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_5_Photometer_processed.csv")):
        df.to_csv("data_processing/ProcessedFiles/_5_Photometer_processed.csv", mode='a', header=False, index= False)
    else:
        df.to_csv("data_processing/ProcessedFiles/_5_Photometer_processed.csv", index=False)
