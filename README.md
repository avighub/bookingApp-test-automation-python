
## Python Test Automation Framework
#### Tech stack
- Language: Python
- Test Runner: pytest
- http lib: requests
- Utility Libs: names

#### Pre requisites
- Install Python
	- verify version : ```python --version``` or ```python3 --version```
-  Clone project
	- ```git clone git@github.com:avighub/bookingApp-test-automation.git```
- [Optional] Setup virtual environment
	- If you don't want to create a isolated python environment and want to use the common shared python environment then skip this step.
 Read more about python virtual environment [here](https://docs.python.org/3/tutorial/venv.html)
	- Install virtualenv: ```pip install virtualenv ```
	- Create virtual env
		- Navigate to the project root directory. For us it is ```/bookingApp-test-automation```
		```virtualenv .venv ``` 
		- Check current python environment location: ```which python ``` - It will give shared python env location
		- Activate virtualenv: ```source .venv/bin/activate ```
		- Check again for  python environment location: ```which python``` - It will give the current new venv location
- Install dependencies
	- Option 1: Using requirements.txt
		- 	```pip install -r requirements.txt```
	- Option 2: Using ```pipenv```
		- Install pipenv: ``pip install pipenv ``
		- Install dependencies : ``pipenv install `` - This will install all dependencies mentioned in ``pipfile``
		- If you want to install particular version of any dependency : ``pipenv dependencyName=x.x.x``


#### Running tests (Command Line)
- Run all Tests from RestApi.py file : ```pytest com/users/RestApi.py```

#### Running tests (Using IDE)
- Pycharm
  - Open the project
  - Go to File --> Settings --> Python Interpreter
    - Select/Add Python Environment 
      - if you are using venv, select the venv created in above pre requisites steps
      - If using shared environment then select the one from user directory
  - Configure Test runner
    - Go to File --> Settings -->Tools-->Python Integrated tools-->Default Test runner-->pytest
