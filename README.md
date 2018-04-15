# python-selenium

- Install Python, use this guide - http://docs.python-guide.org/en/latest/starting/installation/
- Use virtual environments, use this guide - http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref
- Install pip - ```brew install pip``` (assuming you have homebrew installed from the python installation guide)
- Use ```pip install package-name``` to install this packages - ex. ```pip install pytest```
  - pytest
  - pytest-randomly
  - pytest-xdist
  - selenium
- Assuming virtual environment is set up, activate the environment by ```source my_project/bin/activate```
- Run the tests using ```py.test```
- Run a specific browser ```py.test --browser=chrome```
- For parallel execution ```py.test -n 2``` - the number being the number of processes we want to use
- For running markets ```py.test -m smoke```
