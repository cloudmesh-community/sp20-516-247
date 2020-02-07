# #sp20-516-247 E.Cloudmesh.Common.1

# Develop a program that demonstrates the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.util import HEADING, banner
from cloudmesh.common.debug import VERBOSE

class TryStuff:
    def __init__(self):
        self.bannerText = "I am a fancy banner!"
        self.headingText = "I am a normal heading!"
        self.verboseText = "I am better than print :)"

    def printBanner(self):
        banner(self.bannerText)

    def printHeading(self):
        HEADING()
        print(self.headingText)

    def printVerbose(self):
        VERBOSE(self.verboseText)

if __name__ == "__main__":
    trystuff = TryStuff()
    trystuff.printBanner()
    trystuff.printHeading()
    trystuff.printVerbose()

