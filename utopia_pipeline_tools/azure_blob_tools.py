""" Azure Blob Tools Module

This module contains a class that takes in the output dataframe of PVPRO and
contains methods to process the dataset, perform signal decompositions to model
degradation trends, analyze how well the models fit, and visualize the trends.

"""

# imports

import numpy as np
import pandas as pd
from azure.storage.blob import BlobServiceClient

# functions

def upload_images_to_blob():
    # Write this function ! ####################################################################################
    pass

def list_containers_in_blob(connection_string):
    """
    Returns a list of the ifcb image containers in the specified Azure Blob storage.

    :param connection_string: The blob connection string
    :type connection_string: str
    """
    # connect to the Azure Blob
    blob_service_client = BlobServiceClient.from_connection_string(
        conn_str=connection_string)
    container_info = blob_service_client.list_containers()
    blob_containers = []

    # list the dataset containers in the blob (all except files)
    # excluding files since the only containers of interest in this 
    # context are the ones with ifcb images
    for item in container_info:
        if item['name'] == 'files':
            pass
        else:
            blob_containers.append(item['name'])
    
    return blob_containers

def list_files_in_blob(container, connection_string, png_only=True):
    """
    Returns a Pandas dataframe of image filepaths if png_only parameter is true. Otherwise, 
    this function returns a list of the filepaths of all files in the blob container. 

    :param container: Specifies the name of the blob container
    :type container: str
    :param connection_string: The blob connection string
    :type connection_string: str
    :param png_only: Indicates whether to retrieve all files (False), or images only (True); default value is True
    :type png_only: bool, optional
    """
    # connect to Azure blob
    blob_service_client = BlobServiceClient.from_connection_string(
        conn_str=connection_string)
    container_client = blob_service_client.get_container_client(container)

    # List all blobs in the container
    blob_list = container_client.list_blobs()
    filepaths = [blob.name for blob in blob_list]

    if png_only is True:
        # select only the image files
        png_list = [x for x in filepaths if '.png' in x]
        png_df = pd.DataFrame({'filepath': png_list})

        return png_df
    
    else:
        return filepaths