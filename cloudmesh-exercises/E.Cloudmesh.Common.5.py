# #sp20-516-247 E.Cloudmesh.Common.5

# Develop a program that demonstrates the use of cloudmesh.common.StopWatch.

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

class TryStuff:

    def run(self):

        StopWatch.start("test")
        sleep(1)
        StopWatch.stop("test")

        print(StopWatch.get("test"))

        # StopWatch.benchmark()

if __name__ == "__main__":
    trystuff = TryStuff()
    trystuff.run()

