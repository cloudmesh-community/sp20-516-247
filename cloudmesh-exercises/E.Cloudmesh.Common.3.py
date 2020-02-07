# #sp20-516-247 E.Cloudmesh.Common.3

# Develop a program that demonstrates the use of FlatDict.

from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.debug import VERBOSE

class TryStuff:
    def __init__(self):
        self.obj = {
            "name": "Polar Bear",
            "address": {
                "city": "North pole",
                "state": "Earth"
            }
        }

    def run(self):
        newobj = FlatDict(self.obj, sep=".")

        VERBOSE(f"I flattened {newobj}")

if __name__ == "__main__":
    trystuff = TryStuff()
    trystuff.run()

