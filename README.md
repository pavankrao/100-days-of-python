# 100-days-of-python
100 days of Python Projects

# Scan project for all required dependencies

```shell
# Install pipreqs package
pip install pipreqs

# Nav to project
cd /path/to/your/project

# gather project requirements
pipreqs .

# (optional) You can use pipenv to install requirements. Covered in next section
pipenv install -r requirements.txt

```
# Setup python virtual environment

This project recommends using `pipenv` tool to manage your python virtual environments.

```shell
# Install pipenv
sudo apt install -y pipenv

# Add pipenv to PATH if needed
export PATH=$HOME/.local/bin:$PATH
echo 'export PATH=$HOME/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

# Verify pipenv installation
python3 -m pip install --user --upgrade pipenv
which pipenv
pipenv --version

# Navigate to your project directory (change this path)
cd /path/to/your/project

# Initialize pipenv with Python 3
pipenv --python 3

# Install dependencies from requirements.txt if it exists
pipenv install -r requirements.txt

# Install a separate package (example: flask)
pipenv install flask

# Activate the virtual environment
pipenv shell

# Exit virtualenv
<exit-shell>
```
