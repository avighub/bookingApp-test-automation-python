
## Python Test Automation Framework
#### Tech stack
- Language: Python
- Test Runner: pytest
- http lib: requests
- Utility Libs: names

#### Pre requisites
- Install latest version of Python
    - verify version : ```python --version```
- Install pip
  - ```python -m install pip```
- Clone project
    - ```git clone git@github.com:avighub/bookingApp-test-automation.git```
- [Optional] Setup virtual environment
    - If you don't want to create a isolated python environment and want to use the common shared python environment then skip this step.
 Read more about python virtual environment [here](https://docs.python.org/3/tutorial/venv.html)
    - Install virtualenv: ```pip install virtualenv ```
    - Create virtual env
        - Navigate to the project root directory. For us it is ```/bookingApp-test-automation```
        ```virtualenv .venv ``` 
        - Check current python environment location: ```which python ``` - It will give shared python env location
        - Activate virtualenv: ```.venv/Scripts/activate ```
        - Check again for  python environment location: ```which python``` - It will give the current new venv location
- Install dependencies
    - Option 1: Using requirements.txt
        - 	```pip install -r requirements.txt```
    - Option 2: Using ```pipenv```
        - Install pipenv: ``pip install pipenv ``
        - Install dependencies : ``pipenv install `` - This will install all dependencies mentioned in ``pipfile``
        - If you want to install particular version of any dependency : ``pipenv dependencyName=x.x.x``

#### Creating tests
- Naming conventions
  - Python File Name must start or end with ``` test_ ``` or ``` _test ``` ,  else pytest will not pick the tests
  - test method name must start with ``` test_``` , else pytest will not pick the tests
#### Running tests (Command Line)
- Run all Tests from RestApi.py file : ```pytest path/to/the/Test/Test.py```
- To generate report :
  - XML:``` pytest -rA --junitxml="Reports\Report.xml" testFileName.py```
  - HTML: ``` pytest --html="Reports\Report.html" --self-contained-html testFileName.py```
    - [More on HTML report visit here](https://pytest-html.readthedocs.io/en/latest/user_guide.html)
- To run tests in parallel:
  - Using pytest-xdist : ```pytest --html="Reports\Report.html" --self-contained-html testFileName.py -n 2 ```

#### Running tests (Using IDE)
- Pycharm
  - Open the project
  - Go to File --> Settings --> Python Interpreter
    - Select/Add Python Environment 
      - if you are using venv, select the venv created in above pre requisites steps
      - If using shared environment then select the one from user directory
  - Configure Test runner
    - Go to File --> Settings -->Tools-->Python Integrated tools-->Default Test runner-->pytest

#### Selenium Resources
- [Python Selenium Doc](https://selenium-python.readthedocs.io/api.html)
