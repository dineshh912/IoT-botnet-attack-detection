import pandas as pd
import os
from glob import glob


# This function will read all the csv file and load into dataframe.
def load_device_data(PATH, EXT, type=3, device_id=False):
    """
    Creates a data frame consisting of all the .csv-files in a given directory. The directory should
    be where the unzipped data files are stored. Assumes the file structurce is
        device name
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    PATH : str
        The directory in which the data files are stored. 
    EXT : str
        Extension of the file
    type : int
        How many dataframe like to return
        
    Returns
    -------
    benign_data : pandas data frame 
        consisting of all the bengin data.
    mirai_data : pandas data frame
        consisting of all the mirai data.
    gafgyt_data : pandas data frame
        consisting of all the gafgyt data.
    df : pandas data frame
        consisting of all the data combined
    """
    benign_dfs = []
    mirai_dfs = []
    gafgyt_dfs = []
    if device_id == False:
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                if 'benign_traffic' in file:
                    data = pd.read_csv(file)
                    data['label'] = 'Benign'
                    data['device'] = file.split('\\')[1]
                    benign_dfs.append(data)
                if 'mirai_attacks' in file:
                    data = pd.read_csv(file)
                    data['label'] = 'Mirai_'+file.split('\\')[3].split('.')[0]
                    data['device'] = file.split('\\')[1]
                    mirai_dfs.append(data)
                if 'gafgyt_attacks' in file:
                    data = pd.read_csv(file)
                    data['label'] = 'Gafgyt_'+file.split('\\')[3].split('.')[0]
                    data['device'] = file.split('\\')[1]
                    gafgyt_dfs.append(data)
        if type == 3:
            benign_data = pd.concat(benign_dfs, ignore_index=True)
            mirai_data = pd.concat(mirai_dfs, ignore_index=True)
            gafgyt_data = pd.concat(gafgyt_dfs, ignore_index=True)

            return benign_data, mirai_data, gafgyt_data
        if type == 1:
            dfs = [benign_df, mirai_df, gafgyt_df]
            df = pd.concat(dfs)
            
            return df
    else:
        device_list = ['Danmini_Doorbell', 'Ecobee_Thermostat', 
                        'Ennio_Doorbell', 'Philips_B120N10_Baby_Monitor',
                        'Provision_PT_737E_Security_Camera', 'Provision_PT_838_Security_Camera',
                        'Samsung_SNH_1011_N_Webcam', 'SimpleHome_XCS7_1002_WHT_Security_Camera',
                        'SimpleHome_XCS7_1003_WHT_Security_Camera']
        for path, subdir, files in os.walk(base_directory):
            for file in glob(os.path.join(path, file_extension)):
            if file.split('\\')[1] == device_list[device_id]:
                if 'benign_traffic' in file:
                    data = pd.read_csv(file)
                    data['label'] = 'Benign'
                    data['device'] = file.split('\\')[1]
                    benign_dfs.append(data)
                if 'mirai_attacks' in file:
                    data = pd.read_csv(file)
                    data['label'] = 'Mirai_'+file.split('\\')[3].split('.')[0]
                    data['device'] = file.split('\\')[1]
                    mirai_dfs.append(data)
                if 'gafgyt_attacks' in file:
                    data = pd.read_csv(file)
                    data['label'] = 'Gafgyt_'+file.split('\\')[3].split('.')[0]
                    data['device'] = file.split('\\')[1]
                    gafgyt_dfs.append(data)
        if type == 3:
            benign_data = pd.concat(benign_dfs, ignore_index=True)
            mirai_data = pd.concat(mirai_dfs, ignore_index=True)
            gafgyt_data = pd.concat(gafgyt_dfs, ignore_index=True)

            return benign_data, mirai_data, gafgyt_data
        if type == 1:
            dfs = [benign_df, mirai_df, gafgyt_df]
            df = pd.concat(dfs)
            
            return df