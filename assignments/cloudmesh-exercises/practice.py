'''
# console

from cloudmesh.common.console import Console

msg = 'my message'

Console.ok(msg) # prints a green message
Console.error(msg) # prints a red message proceeded with ERROR
Console.msg(msg) # prints a regular black message
Console.error(msg, prefix=False, traceflag=True) # prints error without error prefix but traceflag

# variable

from cloudmesh.common.variables import Variables

variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

# banner

from cloudmesh.common.util import banner

banner("my text")

# heading
# The invocation of the HEADING() function doit prints a banner with the name information.

from cloudmesh.common.util import HEADING

class Example(object):

    def doit(self):
        HEADING()
        print("Hello")

ex1 = Example()
ex1.doit()


# verbose
from cloudmesh.common.debug import VERBOSE

m = {"key": "value"}
VERBOSE(m)

'''
