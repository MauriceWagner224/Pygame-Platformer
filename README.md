# Pygame-Platformer
This is a 2D-Platformer Game using sprites and elements of the sourcecode by [russ123](https://github.com/russs123/Platformer/tree/master).
The goal of this project is to educate beginners on how to use python and structues such as classes in OOP-fashion.

Pygame is a necessary library used widely throughout the project.


<div align="right">&#8673; <a href="#botto" title="Table of Contents">Documentation and more at the bottom</a></div>

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
Installing Pycharm Edu is pretty straightforward and can be installed without admin-privileges by denying admin-authentification after starting the installer.

#### [JetBrains](https://www.jetbrains.com/help/pycharm/installation-guide.html) has further instructions on how to install and get started in Pycharm

#### [Python 3.11](https://www.python.org/ftp/python/3.11.0/) select the correct version of Python for your OS and follow the instructions below.


The project was written in the [64 Bit Version of Python 3.11](https://docs.python.org/3.11/using/windows.html#the-full-installer) for Windows 

 for Windows. (Download for this Version can be found at the bottom of this document) 


#### [Installing Python](https://docs.python.org/3.11/using/windows.html#the-full-installer)

Important: Windows-users without Admin-Privileges need to **<ins>uncheck</ins>** the installer Option: ````Add Python to PATH````

~~- [x] Add Python to PATH~~
- [ ] Add Python to PATH

<a><img src=" 
width="50%" height="50%" border="10" /></a>

### Second Step:
After Starting Pycharm for the first time, a new project can be created.

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/e13c5455-5736-45ad-b8e6-5d5838b21bf7"
width="50%" height="50%" border="10" /></a>

Select virtuelenv as the environment and Python 3.11 as base interpreter for the Project and check the option "inherit global site-packages".

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/e4658d22-4cd6-4fbc-8059-96e21476e06c.jpg" 
width="50%" height="50%" border="10" /></a>

If Python 3.11 does not appear as a base interpreter in the dropdown-menu, you can manually set the path to the installation. For Windows-Users, the path can be found under:

````C:\Users\%username%\AppData\Local\Programs\Python\Python311\python.exe````

___
### Third Step:

All Project files can be moved to the project simply by selecting them in file-explorer and drag-and-drop to the project folder on the left side of PyCharm.

A New Configuration for the project should be created next by clicking "Add Configuration" on the top of the PyCharm Window. Choose Python as standard-config.

![Screenshot 2023-07-11 113509](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/1925c1e4-c0bf-478d-8b75-e4c1f3c103d7)
<img src="[https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/4565c1b6-1d5f-4427-9b64-a6604acf5d98](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/daf70024-dd28-409a-a725-eaba76a786e7).jpg" 
width="50%" height="50%" border="10" /></a>
Select __init__.py as the initalization-script.

![selectinit](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/070bd7e1-6bbe-4ac9-9d17-8b84846bf5d8)
<img src="[https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/4565c1b6-1d5f-4427-9b64-a6604acf5d98](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/daf70024-dd28-409a-a725-eaba76a786e7).jpg" 
width="50%" height="50%" border="10" /></a>
___
### Fourth Step
Pygame can be installed via pip online-distribution with the following command:
````
pip install pygame

pip install pygame==2.3.0
Add this parameter to install a specific version (2.3.0)
````
* * * 
Should there be a problem installing Pygame this way and pip cannot fetch the library from the package index, follow the instruction for a manual installation below.
* * * 

Wheel file for manual istallation: [pygame 2.3.0.whl](https://github.com/pygame/pygame/releases/download/2.3.0/pygame-2.3.0-cp311-cp311-win_amd64.whl)

<img src="[https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/4565c1b6-1d5f-4427-9b64-a6604acf5d98](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/daf70024-dd28-409a-a725-eaba76a786e7).jpg" 
width="50%" height="50%" border="10" />

</a>After downloading the wheel file the following commands install the library from a local source.

> `pip install pygame-2.3.0-cp311-cp311-win_amd64.whl` 
or > `python - m pip install pygame-2.3.0-cp311-cp311-win_amd64.whl

Either install using the complete filepath:
> `C:\Users\%username%\Downloads\pygame-2.3.0-cp311-cp311-win_amd64.whl` (example)
or use the command prompt to navigate to the folder that contains the file 
If you have problems installing pygame. These parameters might help:


> `--disable-pip-version-check` 

> `--force-reinstall`


Read the [PIP Documentation](https://pip-python3.readthedocs.io/en/latest/news.html) for further help.
___
## Last Step
To include the pygame-module in the interpreter, navigate to settings and expand the projects settings on the left to edit the interpreter.

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/a6d4681f-0c7e-48fb-a0ec-4a3227b24750.jpg" 
width="30%" height="30%" border="10" /></a>

Add a new configuration.

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/a27b3075-186f-4431-b64e-fabbde58ebb6.jpg" 
width="70%" height="70%" border="10" /></a>

Make sure to check "inherit global packages", after installing the pygame module.

[x] "inherit global site-packages" | [x] "Make available to all projects"

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/d26b2d13-2139-4f7e-bf2b-1e1c00c650b8.jpg" 
width="50%" height="50%" border="10" /></a>
___
## Finally
the project can be startet, either by clicking the triangular "Run"-button besides the configuration name or pressing "SHIFT + F10"

<img src="https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/5b6075af-4ed4-427c-8dbb-c607e0d4f931.jpg" 
width="50%" height="50%" border="10" /></a>


___
# All links
<div id="botto"></div>

[Python-Documentation](https://docs.python.org/3/)

[Official Pygame Documentation](https://www.pygame.org/docs/)

[Pygame Developer-Notes](https://devdocs.io/pygame-pygame/)

[PIP Documentation](https://pip-python3.readthedocs.io/en/latest/news.html)

## Project was built using these versionsof Python and PyGame

[[Python 3.11](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)] Windows AMD64

[[pygame 2.3.0](https://github.com/pygame/pygame/releases/download/2.3.0/pygame-2.3.0-cp311-cp311-win_amd64.whl)] Windows AMD64

[Instructions]([https://docs.python.org/Documentation](https://docs.python.org/3/))

[Pycharm-Edu 2022](https://www.jetbrains.com/pycharm/download/other.html) IDE used throughout the project.

