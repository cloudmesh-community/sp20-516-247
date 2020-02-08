:o2: this process is not correct as you do not need `pip install virtualenv` instead youmust use 

python -m venv ENV3

python 3.8.1 comes build in with a virtualenv framework, if you need to do a separatepip install for this you use the wrong way of using it or have a proken version of python


Installing venv on `Windows 10 edu` with `Python 3.8.1` and `pip 20.0.2`:

1. Open `Git Bash` or `Cmder` and go to base directory (by default it's `C:\Users\your_username`)

2. Create a folder ENV3 using `mkdir ENV3` but don't go inside it

3. Install `virtualenv` by: `pip install virtualenv` (referred from [this](https://virtualenv.pypa.io/en/latest/installation.html) link)

3. Run `virtualenv ENV3`

4. Run `ENV3\Scripts\activate.bat` (Don't run `activate` instead of `activate.bat`)

5. You will see something like this on your terminal:

   * `C:\Users\your_username (ENV3) λ`

   * Here the `(ENV3)` means that your virtual environment is successfully activated

6. Check `python --version` and `pip --version` version to verify

7. Add to `PATH`: Refer [this](https://cloudmesh.github.io/cloudmesh-manual/installation/install.html#venv-setup-on-windows) link


Errors experienced:

1. [How to](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) correctly use your ENV3 as interpreter in Pycharm?

2. If `python` or `pip` are properly installed on your system but not on `ENV3`, try exiting the enviroment, deleting the folder using `rm -rf ENV3` and then redoing the steps from (1)



