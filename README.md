# Pygame-Platformer
This is a 2D-Platformer Game using sprites and elements of the sourcecode by [russ123](https://github.com/russs123/Platformer/tree/master).
The goal of this project is to educate beginners on how to use python and structues such as classes in OOP-fashion.

Pygame is a necessary library used widely throughout the project.


<div align="right">&darr; <a href="#botto" title="Table of Contents">Documentation and more at the bottom</a></div>

___
### Controls:
|         Key           |         Action         | 
| :-------------------- | :--------------------: |
| &larr; Left-Arrow Key |       Move Left        |
| &rarr; Righ-Arrow Key |       Move Right       |
| Spacebar              |          Jump          |
| Tab Key               |    Shoot projectiles   |
| P                     |       Pause Game       | 

## Getting Started
___
### First Step:
Installing Pycharm Edu is pretty straightforward and can be done without Windows' admin-privileges by denying administrator-authentification when executing the installer.

#### [JetBrains](https://www.jetbrains.com/help/pycharm/installation-guide.html) further instructions on how to install and get started in Pycharm

#### [Python 3.11](https://www.python.org/ftp/python/3.11.0/) select the correct build of Python for your OS and follow the instructions below.

The project was written in the [64 Bit Version of Python 3.11](https://docs.python.org/3.11/using/windows.html#the-full-installer) for Windows .

(Download for this Version can be found at the bottom of this document) 


#### [Installing Python](https://docs.python.org/3.11/using/windows.html#the-full-installer)

Important: Windows-users without Admin-Privileges need to **<ins>uncheck</ins>** the installer Option: ````Add Python to PATH````

- [x] ~~Add Python to PATH~~
- [ ] Add Python to PATH

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/e13c5455-5736-45ad-b8e6-5d5838b21bf7"
width="50%" height="50%" border="10" /></a>
___
### Second Step:
Start Pycharm Pycharm and create a new project.
Select virtuelenv as the environment and Python 3.11 as base interpreter. 


**Be Sure to check the option "<ins>inherit global site-packages</ins>"** :white_check_mark:


- [ ] ~~inherit global site-packages~~

- [x] <ins>inherit global site-packages </ins>

<a><img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/e4658d22-4cd6-4fbc-8059-96e21476e06c.jpg" 
width="50%" height="50%" border="10" /></a>

If Python 3.11 does not appear as a base interpreter in the dropdown-menu, you can manually set the installationpath. For Windows-Users, the path can be found under:

````
C:\Users\%username%\AppData\Local\Programs\Python\Python311\python.exe
````

In the bottom right corner of Pycharm, the existing Python-Interpreter can be edited and a new one created, should the inheritance of global packages be missing etc. 
___
### Third Step:

All Project files can be moved to the project simply by selecting them in file-explorer and drag-and-drop to the project folder on the left side of PyCharm.
 

A New Configuration for the project should be created next by clicking the "Add Configuration"-button at the top-left of the PyCharm Window. Choose Python as standard-config.

<a width="50%" height="50%" border="10">![Screenshot 2023-07-11 113509](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/6f88f3be-3141-4b6f-92d7-bead388a4c79)
</a>

Add a new Configuration by clicking the <code>+</code> symbol in the top-left corner of the Configuration-Window

Select __init__.py as the initalization-script.

<a>![selectinit](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/070bd7e1-6bbe-4ac9-9d17-8b84846bf5d8)
<img src="[https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/4565c1b6-1d5f-4427-9b64-a6604acf5d98](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/daf70024-dd28-409a-a725-eaba76a786e7).jpg" 
width="50%" height="50%" border="10" /></a>
___
### Fourth Step
Pygame can be installed via pip online-distribution with the following command:
````
pip install pygame

pip install pygame==2.3.0
````
Add this parameter to install a specific version (2.3.0)

* * * 
Should there be a problem installing Pygame this way and pip cannot fetch the library from the package index, follow the instruction for a manual installation below.
* * * 

Wheel file for manual istallation: [pygame 2.3.0.whl](https://github.com/pygame/pygame/releases/download/2.3.0/pygame-2.3.0-cp311-cp311-win_amd64.whl)

<img src="[https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/4565c1b6-1d5f-4427-9b64-a6604acf5d98](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/daf70024-dd28-409a-a725-eaba76a786e7).jpg" 
width="50%" height="50%" border="10" />

</a>After downloading the wheel file the following commands install the library from a local source.

````
> pip install pygame-2.3.0-cp311-cp311-win_amd64.whl
or
> python - m pip install pygame-2.3.0-cp311-cp311-win_amd64.whl
````

Either install using the complete filepath:
````
> C:\Users\%username%\Downloads\pygame-2.3.0-cp311-cp311-win_amd64.whl
```` 
or use the command prompt to navigate to the folder that contains the file 
If you have problems installing pygame. These parameters might help:
````
> --disable-pip-version-check

> --force-reinstall
````
Read the [PIP Documentation](https://pip-python3.readthedocs.io/en/latest/news.html) for further help.
___
## Last Step
To include the pygame-module in the interpreter, click on the Python-Version in the bottom-right corner of the Pycharm-Window to edit the Python Interpreter for the project.

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/5f399dfd-9220-4e13-b8c7-c0b3d38ea697" 
width="50%" height="50%" border="10" /></a>

Select "Add a new Interpreter"

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/a27b3075-186f-4431-b64e-fabbde58ebb6.jpg" 
width="70%" height="70%" border="10" /></a>

Make sure to check "inherit global site-packages to include the pygame-library that was installed earlier

[x] "inherit global site-packages" | [x] "Make available to all projects"

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/d26b2d13-2139-4f7e-bf2b-1e1c00c650b8.jpg" 
width="50%" height="50%" border="10" /></a>
___
## Finally
The project can be executed, either by clicking the triangular "Run"-button near the configuration dropdown-menu or pressing "SHIFT + F10".

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/5b6075af-4ed4-427c-8dbb-c607e0d4f931.jpg" 
width="50%" height="50%" border="10" /></a>


___
# All links
<div id="botto"></div>

[Python-Documentation](https://docs.python.org/3/)

[Official Pygame Documentation](https://www.pygame.org/docs/)

[Pygame Developer-Notes](https://devdocs.io/pygame-pygame/)

[PIP Documentation](https://pip-python3.readthedocs.io/en/latest/news.html)

## Project was built using these versions of Python and PyGame

[[Python 3.11](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)] Windows AMD64

[[pygame 2.3.0](https://github.com/pygame/pygame/releases/download/2.3.0/pygame-2.3.0-cp311-cp311-win_amd64.whl)] Windows AMD64

[Instructions]([https://docs.python.org/Documentation](https://docs.python.org/3/))

[Pycharm-Edu 2022](https://www.jetbrains.com/pycharm/download/other.html) IDE used throughout the project.

