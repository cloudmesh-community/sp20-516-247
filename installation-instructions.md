# All installation instructions for quick reference

Using `Windows 10 edu`

## Install `MongoDB` and run it using command-line
1. Run `mongo --version`. If it says: `MongoDB shell version v4.2.3` or something similar, you're all set. If it doesn't, there are 2 possibilities:
   - You have either not installed it. To install it: Go to their [official downloads page](https://www.mongodb.com/download-center/community), download an msi and run it.
   - You have installed it but not added the correct variable to `PATH`. To add to `PATH`, find the folder which contains `mongo.exe` and `mongod.exe` files. For me, they're in `C:\Program Files\MongoDB\Server\4.2\bin`. So I go to `System properties -> Environment Variables -> System Variables -> Path -> New`. Paste the value of the path there.
2. Close the command-line and restart it. The `mongo --version` command should work now.

## Run `cl` in `cmd`
- Go to [installation page](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)
- Download `Build Tools for Visual Studio 2019`
- For correct installation: Watch first 3 mins of [e516-cloudmesh-on-windows](https://www.youtube.com/watch?v=5GpwfSjM9Lg) - Rhonda explained it well
- May have to redo the `ENV3` setup after this

## Update
- `pip install pip -U` (ENV3, home dir)
- `pip install cloudmesh-installer -U` (ENV3, home dir)
