# Pygame-Platformer
This is a 2D-Platformer Game using sprites and elements of the sourcecode by [russ123](https://github.com/russs123/Platformer/tree/master).
The goal of this project is to educate beginners on how to use python and structues such as classes in OOP-fashion.

Pygame is a necessary library used widely throughout the project and it's documentation can be found here:

## Instructions on how to start working on the project.
All Links
## First Step:
Installing Pycharm Edu is pretty straightforward and can be installed without admin-privileges by denying admin-authentification after starting the installer.

[JetBrains](https://www.jetbrains.com/help/pycharm/installation-guide.html) has further instructions on how to install and get started in Pycharm


[Python 3.11](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe) should be installed next, so PyCharm has the correct version of Python installed. 
[Instructions](https://docs.python.org/3.11/using/windows.html#the-full-installer) on the setup and more can be found here.
#Important: Users without Admin-Privileges need to uncheck the installer Options 


[x] "Install for all Users" and [x] "Add Python to PATH" ==> [ ] "Install for all Users" and [ ] "Add Python to PATH"
Uncheck both options: ![image](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/4565c1b6-1d5f-4427-9b64-a6604acf5d98)

## Second Step:
After Starting Pycharm for the first time, a new project can be created.
![image](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/daf70024-dd28-409a-a725-eaba76a786e7)


Virtuelenv should be selected as an environment and Python 3.11 as the Base Interpreter for the Project
![image](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/e4658d22-4cd6-4fbc-8059-96e21476e06c)


If Python 3.11 can not be selected in the dropdown-menu, the installation should be found under (Windows only):

C:\Users\"Your Username"\AppData\Local\Programs\Python --> Select the python.exe in the subfolder "Python311"

Global-site packages can also be inherited

## Third Step:

All Project files can be moved to the project simply by selecting them in file-explorer followed by drag-and-drop to the project folder on the left of the PyCharm-Window.

A New Configuration for the project should be created next by clicking "Add Configuration" on the top of the PyCharm Window. Choose Python as standard-config.
![Screenshot 2023-07-11 113509](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/1925c1e4-c0bf-478d-8b75-e4c1f3c103d7)

Select __init__.py as the initalization-script.
![selectinit](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/070bd7e1-6bbe-4ac9-9d17-8b84846bf5d8)


## Fourth Step
Pygame manual installation:
[pygame 2.3.0](https://github.com/pygame/pygame/releases/download/2.3.0/pygame-2.3.0-cp311-cp311-win_amd64.whl) should've been downloaded and can be installed by typing the following command in the pycharm-Terminal:

# pip install pygame-2.3.0-cp311-cp311-win_amd64.whl
or python - m pip install pygame-2.3.0-cp311-cp311-win_amd64.whl
either install from path: C:\Users\Username\Downloads\pygame-2.3.0-cp311-cp311-win_amd64.whl (example)
or navigate the command prompt to the folder containing the pygame wheel-file.

If you have problems installing pygame, like me. These parameters might help:
--disable-pip-version-check

pip install pygame-2.3.0-cp311-cp311-win_amd64.whl --disable-pip-version-check

--force-reinstall

pip install pygame-2.3.0-cp311-cp311-win_amd64.whl --disable-pip-version-check --force-reinstall

Read the [PIP Documentation](https://pip-python3.readthedocs.io/en/latest/news.html) for further help.

## Last Step
The Pygame-module will most likely not be inherited correctly by the interpreter. To Configure the interpreter again, navigate to the settings.
![image](https://github.com/MauriceWagner224/Pygame-Platformer/assets/79831881/a6d4681f-0c7e-48fb-a0ec-4a3227b24750)


### All links

# [Pygame-Documentation](https://www.pygame.org/docs)

https://www.jetbrains.com/pycharm/download/other.html


## Versions used in my case


[Pycharm-Edu 2022](https://www.jetbrains.com/pycharm/download/other.html) was the IDE used throughout the project.

[pygame releases]() can be found on Github or directly downloaded by the pip command: pip install pygame==2.3.0

[pygame 2.3.0](https://github.com/pygame/pygame/releases/download/2.3.0/pygame-2.3.0-cp311-cp311-win_amd64.whl) for Python 3.11 and compiled for AMD64 is the version i used.

[Python 3.11](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe) for 64-Bit Windows is the version I used.
