import pandas as pd
import os
import glob
import datetime as dt

directory = "Participants"

for participant in os.listdir(directory): #loop through all the participant folders
    pID = participant.split("_")[1]
    big_df = pd.DataFrame()
    
    # access data files
    files = glob.glob(directory + "/Pilot_" + pID + '/3 - Svantek SV104/*.csv', recursive = True)

    for file in files: # loop through data files
        print("reading" + pID)
        # read data in
        source = pd.read_csv(file, skiprows=6, skipfooter=15)

        # reverse order of data by date
        df = source.iloc[::-1]


        # create blank columns to match with null data
        for i in range(df["Time;LCpeak (Ch1"].str.split(";", expand=True).columns.stop - len(df.columns)):
            df.insert(len(df.columns), "Extra" + str(i), "")
            print("blank column" + str(i))


        # split single column of data into fill table
        df[df.columns] = df["Time;LCpeak (Ch1"].str.split(";", expand=True)
        print("split done" + pID)

        if pd.to_datetime(df['Time;LCpeak (Ch1'][3]) < dt.datetime(2023, 5, 23): 
            df['Time;LCpeak (Ch1'] = pd.to_datetime(df['Time;LCpeak (Ch1']) + pd.Timedelta(days=1603, hours=17, minutes=1, seconds=0)
            print("time done")
        

        # combine all sets of data
        big_df =  pd.concat([big_df, df], axis=0)
        print("combined")

        # remove blank columns
        for column in big_df.columns:
            if "Extra" in column:
                del big_df[column]
        print("column stuff")


    
    # combine overload columns
    if " 30) [dB];Overload (Ch1);" in big_df.columns and " 30) [dB];Overload (Ch1);High vibration level;NoMotion;" in big_df.columns:
        big_df[" 30) [dB];Overload (Ch1);"].fillna(big_df[" 30) [dB];Overload (Ch1);High vibration level;NoMotion;"], inplace=True)
        del big_df[' 30) [dB];Overload (Ch1);High vibration level;NoMotion;']

    # add column with participant id
    big_df.insert(0, "Participant ID", participant)
    
    # write data to new file
    if(os.path.isfile("data_processing/ProcessedFiles/_3_Svantek_processed.csv")):
        big_df.to_csv("data_processing/ProcessedFiles/_3_Svantek_processed.csv", mode='a', header=False, index= False)
    else:
        big_df.to_csv("data_processing/ProcessedFiles/_3_Svantek_processed.csv", index=False)
    print("done" + pID)
