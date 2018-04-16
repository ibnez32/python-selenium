# python-selenium

- Install Python, use this guide - http://docs.python-guide.org/en/latest/starting/installation/
- Use virtual environments, use this guide - http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref
- Install pip - ```brew install pip``` (assuming you have homebrew installed from the python installation guide)
- Assuming virtual environment is installed, create virtual environment ```virtualenv python-selenium```
- Activate the environment by ```source python-selenium/bin/activate```
- Once virtualenv is activated you start installing required packages
- Use ```pip install package-name``` to install this packages - ex. ```pip install pytest```
  - pytest
  - pytest-randomly
  - pytest-xdist
  - selenium
- Run the tests using ```py.test```
- Run a specific browser ```py.test --browser=chrome```
- For parallel execution ```py.test -n 2``` - the number being the number of processes we want to use
- For running markers ```py.test -m smoke```
