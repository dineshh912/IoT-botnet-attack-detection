import pandas as pd
import os
from glob import glob



def load_device_data_v2(file_path, file_ext, device, labels=3, size=1):
    """
    This function helps to crate a data frame contain only the device specified.
    The directory should be where the unzipped data files are stored. Assumes the file structurce is
        device name(folder)
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    file_path : str
        The directory in which the data files are stored. 
    file_ext : str
        Extension of the file.
    device: str
        Device name (Folder Name).
    label : integer
        Benign, mirai, gafgyt (bashlite) or 11 Classes.
    size : float
        All the data or only sample data.
        
    Returns
    -------
    device_data : pandas dataframe containg the data 
    """
    try:
        # Generate Empty list to hold data
        dfs = [] 

        # Loop Through all the file associated with the data
        for path, subdir, files in os.walk(file_path):
            for file in glob(os.path.join(path, file_ext)):
                # Check the device name and retrive only those files.
                if file.split("\\")[1] == device:
                    # Reading csv file.
                    data = pd.read_csv(file)
                    label = file.split('\\')
                    data['device'] = label[1]
                    # Check whether only 3 class or 11 class
                    if labels == 3:
                        data['label'] = label[2].split('_')[0]
                        
                    else:
                        # Benign data file usually outside of the folder
                        if len(label) == 3:
                            data['label'] = label[2].split('_')[0]
                        else:
                            data['label'] = label[2].split('_')[0] + '_' \
                                            + label[3].split('.')[0]

                    # Check load all the data or only sample of data
                    if size != 1:
                        sample_data = data.sample(frac=size)
                        dfs.append(sample_data)
                    else:
                        dfs.append(data)

        device_data = pd.concat(dfs, ignore_index = True)

        return device_data
    except Exception as e:
        return str(e)



def load_all_data_v2(file_path, file_ext, device, labels=3, size=1):
    """
    This function helps to crate a data frame contain all the device data.
    The directory should be where the unzipped data files are stored. Assumes the file structurce is
        device name(folder)
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    file_path : str
        The directory in which the data files are stored. 
    file_ext : str
        Extension of the file.
    device: str
        Device name (Folder Name).
    label : integer
        Benign, mirai, gafgyt (bashlite) or 11 Classes.
    size : float
        All the data or only sample data.
        
    Returns
    -------
    device_data : pandas dataframe containg the data 
    """
    try:
        # Generate Empty list to hold data
        dfs = [] 

        # Loop Through all the file associated with the data
        for path, subdir, files in os.walk(file_path):
            for file in glob(os.path.join(path, file_ext)):
                    # Reading csv file.
                data = pd.read_csv(file)
                label = file.split('\\')
                data['device'] = label[1]
                # Check whether only 3 class or 11 class
                if labels == 3:
                    data['label'] = label[2].split('_')[0]
                    
                else:
                    # Benign data file usually outside of the folder
                    if len(label) == 3:
                        data['label'] = label[2].split('_')[0]
                    else:
                        data['label'] = label[2].split('_')[0] + '_' \
                                        + label[3].split('.')[0]

                # Check load all the data or only sample of data
                if size != 1:
                    sample_data = data.sample(frac=size)
                    dfs.append(sample_data)
                else:
                    dfs.append(dat)

        device_data = pd.concat(dfs, ignore_index = True)

        return device_data
    except Exception as e:
        return str(e)


def load_data_labels(PATH, EXT):
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
        
    Returns
    -------
    benign_data : pandas data frame 
        consisting of all the bengin data.
    mirai_data : pandas data frame
        consisting of all the mirai data.
    gafgyt_data : pandas data frame
        consisting of all the gafgyt data.
    """
    try:
        benign_dfs = []
        mirai_dfs = []
        gafgyt_dfs = []
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

        benign_data = pd.concat(benign_dfs, ignore_index=True)
        mirai_data = pd.concat(mirai_dfs, ignore_index=True)
        gafgyt_data = pd.concat(gafgyt_dfs, ignore_index=True)

        return benign_data, mirai_data, gafgyt_data
    except Exception as e:
        return str(e)


def load_device_data(PATH, EXT, device):
    """
    Creates a data frame consisting of individual device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
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
    device : str
        Device Name
        
    Returns
    -------
    device_data : pandas data frame consisting of specific device data with 3 classes.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                if file.split('\\')[1] == device:
                    data = pd.read_csv(file)
                    data['label'] = file.split('\\')[2].split('_')[0]
                    data['device'] = file.split('\\')[1]
                    dfs.append(data)
                        
        device_data = pd.concat(dfs, ignore_index=True)
        
        return device_data
        
    except Exception as e:
        return str(e)



def load_device_data_multi_label(PATH, EXT, device):
    """
    Creates a data frame consisting of individual device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
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
    device : str
        Device Name
        
    Returns
    -------
    device_data : pandas data frame consisting of specific device 
                  data with 11 different classes.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                if file.split('\\')[1] == device:
                    data = pd.read_csv(file)
                    label = file.split('\\')
                    if len(label) == 3:
                        data['label'] = label[2].split('_')[0]
                    else:
                        data['label'] = label[2].split('_')[0] + '_' + label[3].split('.')[0]
                    data['device'] = file.split('\\')[1]
                    dfs.append(data)
                        
        device_data = pd.concat(dfs, ignore_index=True)
        
        return device_data
        
    except Exception as e:
        return str(e)


def load_all_data(PATH, EXT):
    """
    Creates a data frame consisting of all the device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
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
        
    Returns
    -------
    device_data : pandas data frame contain all the device data with 11 classes
                which is device specified.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                data = pd.read_csv(file)
                label = file.split('\\')
                if len(label) == 3:
                    data['label'] = label[1] + '_' + label[2].split('_')[0]
                else:
                    data['label'] = label[1] + '_' + label[2].split('_')[0] + '_' + label[3].split('.')[0]
                
                data['device'] = file.split('\\')[1]
                dfs.append(data)
        device_data = pd.concat(dfs, ignore_index = True)
        
        return device_data
    except Exception as e:
        return str(e)


def load_all_data_class(PATH, EXT):
    """
    Creates a data frame consisting of all the device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
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
        
    Returns
    -------
    device_data : pandas data frame contain all the device data with 3 classes
                which is Not device specified.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                data = pd.read_csv(file)
                label = file.split("\\")
                if len(label) == 3:
                    data['label'] = label[2].split('_')[0]
                else:
                    data['label'] = label[2].split('_')[0]
                data['device'] = file.split('\\')[1]
                sampled_data = data.sample(frac=0.15)
                dfs.append(sampled_data)
        device_data = pd.concat(dfs, ignore_index = True)
        return device_data
    
    except Exception as e:
        return(str(e))

    
def load_all_data_multi_class(PATH, EXT):
    """
    Creates a data frame consisting of all the device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
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
        
    Returns
    -------
    device_data : pandas data frame contain all the device data with 11 classes
                which is Not device specified.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                data = pd.read_csv(file)
                label = file.split('\\')
                if len(label) == 3:
                    data['label'] = label[2].split('_')[0]
                else:
                    data['label'] = label[2].split('_')[0] + '_' + label[3].split('.')[0]
                
                data['device'] = file.split('\\')[1]
                sampled_data = data.sample(frac=0.15)
                dfs.append(sampled_data)
        device_data = pd.concat(dfs, ignore_index = True)
        
        return device_data
    except Exception as e:
        return str(e)