import shutil
import os
import random
import math
from copy import deepcopy

def get_img_path(folder_path, flatten=False):
    """
    Returns the path for each file inside of a folder

    Parameters
    ----------
    folder_path: str
        Path of the folder in which images are contained
    flatten : bool
        Return should be flattened

    Returns
    -------
    paths: list[list]
        List of file paths
    """
       
    paths = []
    for folder,subfolders,file in os.walk(folder_path,topdown=True):
        array = []
        for fname in file:
            full_name=os.path.join(folder,fname)
            array.append(full_name)
        paths.append(array)
        
    if flatten == True:
        flat_paths = [item for items in paths for item in items]
        return flat_paths
    else: 
        return paths
    


def move_imgs(path_image, dest_path):
    """
    Function that copies one or more images for which path is provided, to the directory of choice. 
    It is essentially a 'cp' function that creates the destination folder, or overwrites.
    
    Parameters
    ----------
    path_image : str | list[str]
        Path of the images to be moved.
    dest_path: str 
        Path of the final directory. If it already exists, 
        it will be removed with its content and a new one will be created in its place.

    Returns
    -------
        None
    """    
    new_dir=dest_path
    if os.path.exists(new_dir):
        shutil.rmtree(new_dir)
    os.mkdir(new_dir)
    
    #Copying images
    for i in path_image:
        shutil.copy(i, new_dir)
    


def splitter(compilation, train_split, val_split, test_split):
    """
    Split a compilation of items into training, validation, and test sets with custom percentages.

    This function takes a list of items and splits it into three subsets:
    training, validation, and test. The size of each subset is determined
    by the split parameters.

    Parameters
    ----------
    compilation : list
        The original list of items to be split.
    train_split : float, optional
        The fraction of items to be used for training. Default is 0.8 (80%).
    val_split : float, optional
        The fraction of items to be used for validation. Default is 0.1 (10%).
    test_split : float, optional
        The fraction of items to be used for testing. Default is 0.1 (10%).

    Returns
    -------
    tuple of lists
        A tuple containing three lists in the following order:
        - training_set : list
            The list of items for training.
        - validation_set : list
            The list of items for validation.
        - test_set : list
            The list of items for testing.

    Raises
    ------
    ValueError
        If the sum of split percentages is not equal to 1.

    Notes
    -----
    The function shuffles the input list to ensure random distribution
    across the three sets.

    Examples
    --------
    >>> data = list(range(100))
    >>> train, val, test = splitter(data, train_split=0.7, val_split=0.15, test_split=0.15)
    >>> len(train), len(val), len(test)
    (70, 15, 15)
    """
    if not math.isclose(train_split + val_split + test_split, 1.0, rel_tol=1e-5):
        raise ValueError("Split percentages must sum to 1.")

    # Create a copy of the input list to avoid modifying the original
    shuffled_compilation = deepcopy(compilation)
    random.shuffle(shuffled_compilation)

    total_items = len(compilation)
    train_size = int(total_items * train_split)
    val_size = int(total_items * val_split)

    # Split 
    training_set = shuffled_compilation[:train_size]
    validation_set = shuffled_compilation[train_size:train_size + val_size]
    test_set = shuffled_compilation[train_size + val_size:]

    return training_set, validation_set, test_set


