import pandas as pd
import os
import glob

root_directory = "Participants"

for participant in os.listdir(root_directory): # loop through all the participant folders
    pID = participant.split("_")[1]

    big_df = pd.DataFrame()


    directory = "Participants" + "/Pilot_" + pID + "/6 - Empatica EmbracePlus"
    for day in os.listdir(directory): # loop through subdirectories by day
        rootdir = directory+"/"+day

        if os.path.isfile(rootdir):
            break
        
        # access data files
        eda_files = glob.glob(rootdir + '/**/digital_biomarkers/aggregated_per_minute/*_eda.csv', recursive = True)
        movement_files = glob.glob(rootdir + '/**/digital_biomarkers/aggregated_per_minute/*_movement-intensity.csv', recursive = True)
        prv_files = glob.glob(rootdir + '/**/digital_biomarkers/aggregated_per_minute/*_prv.csv', recursive = True)
        pulse_files = glob.glob(rootdir + '/**/digital_biomarkers/aggregated_per_minute/*_pulse-rate.csv', recursive = True)

        if eda_files:
            eda = pd.read_csv(eda_files[0])
            eda.rename(columns={'missing_value_reason': 'missing_value_reason_eda'}, inplace=True)
        else:
            eda = pd.DataFrame()

        if movement_files:
            movement = pd.read_csv(movement_files[0])
            movement.rename(columns={'missing_value_reason': 'missing_value_reason_movement'}, inplace=True)
        else:
            movement = pd.DataFrame()
       
        if prv_files:
            prv = pd.read_csv(prv_files[0])
            prv.rename(columns={'missing_value_reason': 'missing_value_reason_prv'}, inplace=True)
        else:
            prv = pd.DataFrame()
        
        if pulse_files:
            pulse = pd.read_csv(pulse_files[0])
            pulse.rename(columns={'missing_value_reason': 'missing_value_reason_pulse'}, inplace=True)
        else:
            pulse = pd.DataFrame()

        # combine data into one table
        df1 = pd.concat([eda, movement], axis=1)
        df2 = pd.concat([pulse, prv], axis=1)
        big_merge = pd.concat([df1, df2], axis=1)

        big_merge = big_merge.T.drop_duplicates().T
        
        big_df = big_df.append(big_merge.reset_index(drop=True))

    # add column with participant id
    big_df.insert(0, "Participant ID", participant)
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_6_Embrace_processed.csv")):
        big_df.to_csv("data_processing/ProcessedFiles/_6_Embrace_processed.csv", mode='a', header=False, index= False)
    else:
        big_df.to_csv("data_processing/ProcessedFiles/_6_Embrace_processed.csv", index=False)
    


    

