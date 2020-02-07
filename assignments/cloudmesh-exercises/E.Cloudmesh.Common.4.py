# #sp20-516-247 E.Cloudmesh.Common.4

# Develop a program that demonstrates the use of cloudmesh.common.Shell.

from cloudmesh.common.Shell import Shell

class TryStuff:

    def run(self):
        result = Shell.execute('pwd')
        print(result)

        result = Shell.execute('ls', ["-l", "-a"])
        print(result)

        result = Shell.execute('ls', "-l -a")
        print(result)

if __name__ == "__main__":
    trystuff = TryStuff()
    trystuff.run()

