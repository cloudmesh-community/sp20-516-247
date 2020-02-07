# #sp20-516-247 E.Cloudmesh.Common.2

# Develop a program that demonstrates the use of dotdict.

from cloudmesh.common.dotdict import dotdict

class TryStuff:
    def __init__(self):
        self.text = 'I am an alien but nobody notices me!'
        self.obj = {'name': 'ET'}

    def run(self):
        newobj = dotdict(self.obj)

        if newobj.name == "ET":
            print(f"I can use dot notation in {newobj}")

if __name__ == "__main__":
    trystuff = TryStuff()
    trystuff.run()

