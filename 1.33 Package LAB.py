# Step 1
#Group the functions in separate modules

# Step 2
#Group the modules as below
# From the bottom up:

# the ugly group contains two modules: psi and omega;
# the best group contains two modules: sigma and tau;
# the good group contains two modules (alpha and beta) and one subgroup (best)
# the extra group contains two subgroups (good and bad) and one module (iota)

# Step 3
# assume that extra is the name of a newly created package (think of it as the package's root), it will impose a naming rule which allows you to clearly name every entity from the tree.
# For example:
# the location of a function named funT() from the tau package may be described as:

# extra.good.best.tau.funT()

# a function marked as:

# extra.ugly.psi.funP()
#comes from the psi module being stored in the ugly subpackage of the extra package.

# Step 4
#how do you transform such a tree (actually, a subtree) into a real Python package (in other words, how do you convince Python that such a tree is not just a bunch of junk files, but a set of modules)?
>> packages, like modules, may require initialization.

#where do you put the subtree to make it accessible to Python?
>> Python expects that there is a file with a very unique name inside the package's folder: __init__.py.
#The content of the file is executed when any of the package's modules is imported. If you don't want any special initializations, you can leave the file empty, but you mustn't omit it.

# Step 5
#The presence of the __init.py__ file finally makes up the package.

# Step 6
#Package zip file need to unpack it in the folder presented in the scheme.

# Step 7
#Access the funI() function from the iota module from the top of the extra package.
main2.py
from sys import path
path.append('..\\packages')

import extra.iota
print(extra.iota.funI())
# we've modified the path variable to make it accessible to Python.
# the import doesn't point directly to the module, but specifies the fully qualified path from the top of the package.

#Or
main2.py
from sys import path
path.append('..\\packages')

from extra.iota import funI
print(funI())

# Step 8
#Access to the sigma and tau modules
main2.py
from sys import path

path.append('..\\packages')

import extra.good.best.sigma
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())

#Or using aliasing
from sys import path

path.append('..\\packages')

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.funS())
print(alp.funA())

# Step 9
#Assume that we've zipped the whole subdirectory, starting from the extra folder (including it), and let's get a file named extrapack.zip. Next, we put the file inside the packages folder.
#use the zip file in a role of packages:
from sys import path

path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())
