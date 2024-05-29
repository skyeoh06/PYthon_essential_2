# Summary
#You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?
import sys

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()

#Some additional and necessary packages are stored inside the D:\Python\Project\Modules directory. 
#Write a code ensuring that the directory is traversed by Python in order to find all requested modules.
import sys
sys.path.append("D:\\Python\\Project\\Modules")

#The directory mentioned in the previous exercise contains a sub-tree of the following structure:
abc
 |__ def
      |__ mymodule.py
#Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, write an import directive letting you use all the mymodule entities.
import abc.def.mymodule
