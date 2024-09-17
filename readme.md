# Python - CSV to SQL SERVER Example

## What is it?
This is a script that simply takes an example CSV file an imports it into SQL Server using pandas with Python.  The table is created automatically if it does not already exist.

## Pre-Install if Python environment is needed
### Windows:
Install [Anaconda](https://www.anaconda.com/download/success)

Install [Powershell 7](https://github.com/PowerShell/PowerShell/releases/download/v7.4.5/PowerShell-7.4.5-win-x64.msi)

Open the Anaconda terminal and run
```
conda init powershell
```
Open Powershell and check that it is version 7
```
$PSVersionTable
```

### Linux (Debian/Ubuntu)
Download conda installation script and run it
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
bash Anaconda3-2023.09-0-Linux-x86_64.sh
source ~/.bashrc
```

### Create Python environment (Windows or Linux after above steps)

Create Python Environment with Python 3.12
```
conda create -n py3.12 python=3.12 anaconda
```

Activate the environment
```
conda activate py3.12
````

## Install modules
Install the requirements
```
pip install -r requirements.txt
```

## Executing the program

Ensure you have set the variables in the script as neccessary

```
  _server = 'sh-dev-db-2'
  _database = 'PeterTest'
  _table_name = 'TestCSV'
  _username = None
  _password = None
  file_path = 'test.csv'
```

Run the program (Windows)
```
python .\importer.py
```

**OR**

Run the program (Linux)
```
chmod +x importer.py
./importer.py
```

