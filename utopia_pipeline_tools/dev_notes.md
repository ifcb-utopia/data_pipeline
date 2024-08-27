# Development Documentation

## Environment and Module Issues

### ModuleNotFoundError/ImportError for keras

_Notes:_ 
- Using the miniconda3 prompt
- Tensorflow version 2.17.0
- Keras version 3.5.0
- Python version 3.10.14

_Process:_  
After I installed the utopia_pipeline_tools module locally with pip, my notebooks were unable to find the keras library, so `from tensorflow import keras` gave me an error. I tried uninstalling tensorflow then re-installing it with pip (`pip uninstall tensorflow` and `pip install tensorflow`). That didn't solve the issue, so next I tried installing tensorflow with conda (`conda install -c conda-forge tensorflow`). That alone didn't work, and I thought maybe the pip install and the conda install were interfering with each other, so I uninstalled tensorflow with pip then re-ran the conda install command. Once again, this was unsuccessful. I uninstalled tensorflow with `conda uninstall tensorflow` and tried a new method. This time, I checked my python version (`python --version`), which was 3.10.14 and tried `pip3.10 install tensorflow`. Unfortunately, this also did not work.

I did a bit of investigation in my site_packages folder and found the tensorflow folder. This folder did not contain the keras module for some reason. I thought it might be an issue with the new version of tensorflow, so I once again uninstalled tensorflow with pip and re-installed it with the previous version (`pip install tensorflow==2.16.2`) which finally worked!