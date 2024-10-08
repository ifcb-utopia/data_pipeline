from setuptools import setup
import utopia_pipeline_tools

setup(
    name='utopia_pipeline_tools',
    version=utopia_pipeline_tools.__version__,    
    description='A Python package for managing data in the ifcbUTOPIA project',
    url='https://github.com/ifcb-utopia/data_pipeline',
    author='Claire Berschauer',
    author_email='ckb22@uw.edu',
    license='GPLv3', 
    packages=['utopia_pipeline_tools'], 
    install_requires=['numpy', 
                      'jupyter',
                      'ipykernel',
                      'numpy>=1.2',
                      'pandas>=1.4',
                      'scikit-learn>=1.2',
                      'matplotlib>=3.5',
                      'imageio',
                      'tensorflow==2.16.2',
                      'pip',
                      'tqdm',
                      'pylint',
                      'modAL',
                      'azure-storage-blob',
                      'azure-mgmt-compute',
                      'azure-identity',
                      'azure-mgmt-storage',
                      'opencv-python',
                      'pymssql>=2.2',
                      'plotly',
                      'umap-learn',
                      'marimo',
                      'seaborn',
                      'IPython',
                      'streamlit==1.29',
                      'keras'                 
                      ],  ## all the dependencies

    classifiers=[
        'Development Status :: 1 - Planning',
        'Topic :: Scientific/Engineering :: Oceanography',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',  
        'Operating System :: Microsoft :: Windows :: Windows 11',
        'Programming Language :: Python :: 3.10',
    ],  
)