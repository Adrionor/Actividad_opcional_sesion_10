# Activity: Unit and Integration Tests
In this activity, you will create the unit tests to validate the functions defined in [operations.py](app/operations.py) script. Follow the instructions below to run the script. Then, create the tests.

## Deliverables
**Unit tests:**
Tests for addition, subtraction, multiplication, division and the one that converts fractions to numbers.

**Integration testing:**
Carry out the test for the following mathematical operation:
(num1 + num2) * (num3 - num4)

with the following numbers
(5+5)*(1.25-0.75) = (10)*(0.5) = 5
(8+7/5)*(15-3/8) = (9.4)*(14.625) = 137.475

## Preconditions
It is assumed that you already have Python 3+ installed in its system. If not, please install it.

Check this link according to your operating system:
[Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)

## Virtual Environment Installation
Open a terminal, go to the project root folder, and install `venv` with the following command.

```bash
pip3 install virtualenv
```

Then, run the following commands to create the virtual environment.
```bash
python3 -m venv ./venv
```

Activate the virtual environment.
```bash
source env/bin/activate
```

**Note**  
Disable the virtual environment using this command at the end of its example.
```bash
deactivate
```

## Library Installation
To install the necessary libraries, use this command:
```
pip3 install -r requirements.txt
```

Ready, the configuration is ready for the check the script!

## Running the code
Change the directory and run the following command
```bash
cd session-10/pytest/calculator/app/
```
Then run
```bash
python example.py
```
I should see the following data output
```bash
1.5
0.5
2.0
0.5
```


## Execute unit
C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10>C:\Users\jorge.guzman\AppData\Local\Programs\Python\Python37\python.exe -m venv myenv

C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10>C:\Users\jorge.guzman\AppData\Local\Programs\Python\Python310\python.exe -m venv myvenv

C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10>C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\myvenv\Scripts\activate
"C:\Users\jorge.guzman\Actividad" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10>cd C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\myvenv\Scripts

C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\myvenv\Scripts>activate

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\myvenv\Scripts>cd C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator>pip install requirements.txt
ERROR: Could not find a version that satisfies the requirement requirements.txt (from versions: none)
HINT: You are attempting to install a package literally named "requirements.txt" (which cannot exist). Consider using the '-r' flag to install the packages listed in requirements.txt
ERROR: No matching distribution found for requirements.txt

[notice] A new release of pip available: 22.3.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator>pip3 install -r requirements.txt
Collecting pytest
  Downloading pytest-7.4.0-py3-none-any.whl (323 kB)
     ---------------------------------------- 323.6/323.6 kB 2.0 MB/s eta 0:00:00
Collecting colorama
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting pluggy<2.0,>=0.12
  Using cached pluggy-1.2.0-py3-none-any.whl (17 kB)
Collecting packaging
  Using cached packaging-23.1-py3-none-any.whl (48 kB)
Collecting tomli>=1.0.0
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting exceptiongroup>=1.0.0rc8
  Using cached exceptiongroup-1.1.2-py3-none-any.whl (14 kB)
Collecting iniconfig
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Installing collected packages: tomli, pluggy, packaging, iniconfig, exceptiongroup, colorama, pytest
Successfully installed colorama-0.4.6 exceptiongroup-1.1.2 iniconfig-2.0.0 packaging-23.1 pluggy-1.2.0 pytest-7.4.0 tomli-2.0.1

[notice] A new release of pip available: 22.3.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator>python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\jorge.guzman\actividad opcional sesion 10\actividad_opcional_sesion_10\myvenv\lib\site-packages (22.3.1)
Collecting pip
  Using cached pip-23.2.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3.1
    Uninstalling pip-22.3.1:
      Successfully uninstalled pip-22.3.1
Successfully installed pip-23.2.1

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator>C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator\app
"C:\Users\jorge.guzman\Actividad" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator>cd C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator\app

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator\app>python example.py
res_sum: 1.5
res_substract: 0.5
res_divide: 2.0
res_multiply: 0.25

(myvenv) C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator\app>pytest ./tests/test_itesm_mlops.py::test_csv_file_existence -v
===================================================== test session starts =====================================================
platform win32 -- Python 3.10.9, pytest-7.4.0, pluggy-1.2.0 -- C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\myvenv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\jorge.guzman\Actividad opcional sesion 10\Actividad_opcional_sesion_10\activity\calculator\app
collected 0 items

> **Note**  
Check this [auxiliar_commands](auxiliar_commands.md) to see more Pytest commands 