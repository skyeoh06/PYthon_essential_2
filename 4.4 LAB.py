#1.2
#Before you create your first directory structure, you'll see how you can get information about the current operating system. This is really easy because the os module provides a function called uname, which returns an object containing the following attributes:

#systemname — stores the name of the operating system;
#nodename — stores the machine name on the network;
#release — stores the operating system release;
#version — stores the operating system version;
#machine — stores the hardware identifier, e.g., x86_64.
import os
print(os.uname())
>> posix.uname_result(sysname='Linux', nodename='73775ce9f6ca', release='4.4.0-210-generic', version='#242-Ubuntu SMP Fri Apr 16 09:57:56 UTC 2021', machine='x86_64')

#the uname function returns an object containing information about the operating system. 
#the uname function only works on some Unix systems. If you use Windows, you can use the uname function in the platform module, which returns a similar result.
#The os module allows you to quickly distinguish the operating system using the name attribute, which supports one of the following names:

#posix — you'll get this name if you use Unix;
#nt — you'll get this name if you use Windows;
#java — you'll get this name if your code is written in Jython.
print(os.name)
>> posix

#On Unix systems, there's a command called uname that returns the same information (if you run it with the -a option) as the uname function.

#1.3
#Creating directories in Python
#The os module provides a function called mkdir, which, like the mkdir command in Unix and Windows, allows you to create a directory. The mkdir function requires a path that can be relative or absolute. Let's recall what both paths look like in practice:

#my_first_directory — this is a relative path which will create the my_first_directory directory in the current working directory;
#./my_first_directory — this is a relative path that explicitly points to the current working directory. It has the same effect as the path above;
#../my_first_directory — this is a relative path that will create the my_first_directory directory in the parent directory of the current working directory;
#/python/my_first_directory — this is the absolute path that will create the my_first_directory directory, which in turn is in the python directory in the root directory.
import os

os.mkdir("my_first_directory")
print(os.listdir())
>> ['exam_results.csv', 'my_first_directory', 'function.pckl', 'contacts.csv', 'multidata.pckl', 'forecast.xml', 'example.txt', 'books.xml', 'cipher.txt', 'cucumber.pckl', 'mess.ini', 'ccipher.txt', 'message.txt', 'config.ini', 'cars.xml', 'module.py', 'cars.json', 'tzop.txt', 'text.txt']

#It shows an example of how to create the my_first_directory directory using a relative path. This is the simplest variant of the relative path, which consists of passing only the directory name.
#The mkdir function creates a directory in the specified path. Note that running the program twice will raise a FileExistsError.
#This means that we cannot create a directory if it already exists. In addition to the path argument, the mkdir function can optionally take the mode argument, which specifies directory permissions. However, on some systems, the mode argument is ignored.
#To change the directory permissions, we recommend the chmod function, which works similarly to the chmod command on Unix systems.
#another function provided by the os module named listdir is used. The listdir function returns a list containing the names of the files and directories that are in the path passed as an argument.
#If no argument is passed to it, the current working directory will be used (as in the example above). It's important that the result of the listdir function omits the entries '.' and '..', which are displayed, e.g., when using the ls -a command on Unix systems.
#NOTE: In both Windows and Unix, there's a command called mkdir, which requires a directory path. The equivalent of the above code that creates the my_first_directory directory is the mkdir my_first_directory command.


#1.4
#Recursive directory creation
#The mkdir function is very useful, but what if you need to create another directory in the directory you've just created. Of course, you can go to the created directory and create another directory inside it, 
#but fortunately the os module provides a function called makedirs, which makes this task easier.
#The makedirs function enables recursive directory creation, which means that all directories in the path will be created.
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
>> ['my_second_directory']


#The code creates two directories. The first of them is created in the current working directory, while the second in the my_first_directory directory.
#You don't have to go to the my_first_directory directory to create the my_second_directory directory, because the makedirs function does this for you. 
#To move between directories, you can use a function called chdir, which changes the current working directory to the specified path. As an argument, it takes any relative or absolute path. In our example, we pass the first directory name to it.
#NOTE: The equivalent of the makedirs function on Unix systems is the mkdir command with the -p flag, while in Windows, simply the mkdir command with the path:
#Unix-like systems:

mkdir -p my_first_directory/my_second_directory

#Windows:

mkdir my_first_directory/my_second_directory

#1.5
#the os module provides a function that returns information about the current working directory.
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())
>>
/tmp/iqAbdky2MLRuZdZZASWa/files/my_first_directory
/tmp/iqAbdky2MLRuZdZZASWa/files/my_first_directory/my_second_directory

#In the example, we create the my_first_directory directory, and the my_second_directory directory inside it. In the next step, we change the current working directory to the my_first_directory directory, 
#and then display the current working directory (first line of the result).
#Next, we go to the my_second_directory directory and again display the current working directory (second line of the result). As you can see, the getcwd function returns the absolute path to the directories.
#NOTE: On Unix-like systems, the equivalent of the getcwd function is the pwd command, which prints the name of the current working directory.

#1.6
#Deleting directories in Python
#The os module also allows you to delete directories. It gives you the option of deleting a single directory or a directory with its subdirectories. 
#To delete a single directory, you can use a function called rmdir, which takes the path as its argument.

import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())
>>
['exam_results.csv', 'my_first_directory', 'function.pckl', 'contacts.csv', 'multidata.pckl', 'forecast.xml', 'example.txt', 'books.xml', 'cipher.txt', 'cucumber.pckl', 'mess.ini', 'ccipher.txt', 'message.txt', 'config.ini', 'cars.xml', 'module.py', 'cars.json', 'tzop.txt', 'text.txt']
['exam_results.csv', 'function.pckl', 'contacts.csv', 'multidata.pckl', 'forecast.xml', 'example.txt', 'books.xml', 'cipher.txt', 'cucumber.pckl', 'mess.ini', 'ccipher.txt', 'message.txt', 'config.ini', 'cars.xml', 'module.py', 'cars.json', 'tzop.txt', 'text.txt']

#The above example is really simple. First, the my_first_directory directory is created, and then it's removed using the rmdir function. 
#The listdir function is used as proof that the directory has been removed successfully. In this case, it returns an empty list. When deleting a directory, make sure it exists and is empty, otherwise an exception will be raised.

#To remove a directory and its subdirectories, you can use the removedirs function, which requires you to specify a path containing all directories that should be removed:
import os

os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())
>> ['exam_results.csv', 'function.pckl', 'contacts.csv', 'multidata.pckl', 'forecast.xml', 'example.txt', 'books.xml', 'cipher.txt', 'cucumber.pckl', 'mess.ini', 'ccipher.txt', 'message.txt', 'config.ini', 'cars.xml', 'module.py', 'cars.json', 'tzop.txt', 'text.txt']

#As with the rmdir function, if one of the directories doesn't exist or isn't empty, an exception will be raised.
#NOTE: In both Windows and Unix, there's a command called rmdir, which, just like the rmdir function, removes directories. What's more, both systems have commands to delete a directory and its contents. In Unix, this is the rm command with the -r flag.

#1.7
#The system() function
#All functions presented in this part of the course can be replaced by a function called system, which executes a command passed to it as a string.
#The system function is available in both Windows and Unix. Depending on the system, it returns a different result.
#In Windows, it returns the value returned by the shell after running the command given, while in Unix, it returns the exit status of the process.

import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
>> 0

#The above example will work in both Windows and Unix. In our case, we receive exit status 0, which indicates success on Unix systems.
#This means that the my_first_directory directory has been created. As part of the exercise, try to list the contents of the directory where you created the my_first_directory directory.

#1.9
#What is the output of the following snippet if you run it on Unix?

import os
print(os.name)
>> posix

#What is the output of the following snippet?

import os

os.mkdir("hello")
print(os.listdir())
>> ['hello']

