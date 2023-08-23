import pandas as pd
import os

import os

root_directory = "Participants"

for participant in os.listdir(root_directory): # loop through all the participant folders
    pID = participant.split("_")[1]

    big_df = pd.DataFrame()

    directory = "Participants" + "/Pilot_" + pID + "/7 - Dreem EEG"

    for file in os.listdir(directory): # loop through files in directory
        rootdir = directory+"/"+file

        # only use trials not including depreciated report
        if "@dreemtrial.com_" not in file:
            pass
        
        if ".csv" not in os.path.splitext(file)[-1]:
            pass
            
        elif "depreciated_report" not in file:
            # access data file
            source = pd.read_csv(rootdir, header=None)
            # combine tables
            big_df = big_df.append(source.T)


    big_df = big_df.drop_duplicates()

    # write data to new file
    big_df.to_csv("data_processing/ProcessedFiles/" + pID + "_7_DreamEEG_processed.csv", index=False)
    result = pd.read_csv("data_processing/ProcessedFiles/" + pID + "_7_DreamEEG_processed.csv", skiprows=[0])
    os.remove("data_processing/ProcessedFiles/" + pID + "_7_DreamEEG_processed.csv")

    # add column with participant id
    result.insert(0, "Participant ID", participant)
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_7_DreamEEG_processed.csv")):
        result.to_csv("data_processing/ProcessedFiles/_7_DreamEEG_processed.csv", mode='a', header=False, index= False)
    else:
        result.to_csv("data_processing/ProcessedFiles/_7_DreamEEG_processed.csv", index=False)




