from setuptools import setup

setup(
    name='utopia_pipeline_tools',
    version='0.1.0',    
    description='A Python package for managing data in the ifcbUTOPIA project',
    url='https://github.com/ifcb-utopia/data_pipeline_tools',
    author='Claire Berschauer',
    author_email='ckb22@uw.edu',
    license='BSD 2-clause', ## pick a license
    packages=['utopia_pipeline_tools'], ## include PIVOT too?
    install_requires=['mpi4py>=2.0',
                      'numpy',                     
                      ],  ## add all the dependencies

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Windows',  ## what is POSIX? Do I need to change that?
        'Programming Language :: Python :: 3.10',
    ],  # figure out what to do about the dependencies
)