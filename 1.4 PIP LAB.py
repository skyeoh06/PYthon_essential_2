# How to use pip
pip help
>> The list produced by pip summarizes all the available operations, and the last of them is help

#know more about any of the listed operations, you can use the following form of pip invocation:
#pip help operation
#Example
pip help install
>> will show you detailed information about using and parameterizing the install command.
#want to know what Python packages have been installed so far, you can use the list operation
pip list

>>there are two columns in the list, one showing the name of the installed package, and the other showing the version of the package. 
>>The list contains the two lines : pip and setuptools.

#a command that  about any of the installed packages
#pip show package_name
pip show pip
>>the information appearing on the screen is taken from inside the package being shown. In other words, the package's creator is obliged to equip it with all the needed data (or to express it more precisely – metadata).
# Look at the two lines at the bottom of the output. They show:
# which packages are needed to successfully utilize the package (Requires:)
# which packages need the package to be successfully utilized (Required-by:)
# As you can see, both properties are empty.

# One of these cases occurs when you want to search through PyPI in order to find a desired package. This kind of search is initiated by the following command:

# pip search anystring


# The anystring provided by you will be searched in:

# the names of all the packages;
# the summary strings of all the packages.

# Be aware of the fact that some searches may generate a real avalanche of data, so try to be as specific as possible. For example, an innocent-looking query like this one:

# pip search pip

# produces more than 100 lines of results (try it yourself – don't take our word for it). By the way – the search is case insensitive.
# use pip to install the package onto your computer.

# Two possible scenarios may be put into action now:

# you want to install a new package for you only – it won't be available for any other user (account) existing on your computer; this procedure is the only one available if you can’t elevate your permissions and act as a system administrator;
>> pip uses a dedicated option named --user (note the double dash). The presence of this option instructs pip to act locally on behalf of your (non-administrative) user.
>> pip install --user pygame
# you’ve decided to install a new package system-wide – you have administrative rights and you're not afraid to use them.
>> pip install pygame

# Example Simple Program
# import pygame 
import pygame

run = True #the program will run as long as the run variable is True
# determine the window's size
width = 400
height = 100
pygame.init() # initialize the pygame environment
# prepare the application window and set its size
screen = pygame.display.set_mode((width, height))
# make an object representing the default font of size 48 points
font = pygame.font.SysFont(None, 48)
# make an object representing a given text – the text will be anti-aliased (True) and white (255,255,255)
text = font.render("Welcome to pygame", True, (255, 255, 255))
# insert the text into the (currently invisible) screen buffer
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# flip the screen buffers to make the text visible
pygame.display.flip()
# the pygame main loop starts here
while run:
    for event in pygame.event.get(): # get a list of all pending pygame events
      #check whether the user has closed the window or clicked somewhere inside it or pressed any key
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False #if yes, stop executing the code.

# The pip install has two important additional abilities:

# able to update a locally installed package(to make sure that you’re using the latest version of a particular package)

# pip install -U package_name

# where -U means update. Note: this form of the command makes use of the --user option for the same purpose as presented previously

# able to install a user-selected version of a package (pip installs the newest available version by default)
# pip install package_name==package_version (note the double equals sign) 

# pip install pygame==1.9.2

#Remove Package
pip uninstall package_name
>> pip uninstall pygame

# Where does the name "The Cheese Shop" come from?
>> It's a reference to an old Monty Python's sketch of the same name.

#Why should I ensure which one of pip and pip3 works for me?
>>When Python 2 and Python 3 coexist in your OS, it's likely that pip identifies the instance of pip working with Python 2 packages only.

#How can I determine if my pip works with either Python 2 or Python 3?
>>pip --version will tell you that.

#Unfortunately, I don't have administrative right. What should I do to install a package system-wide?
>>You have to ask your sysadmin - don't try to hack your OS!



