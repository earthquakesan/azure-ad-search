# azure-ad-search
Example repository of a backend app searching user by name / email in Azure AD.

## Dev Setup

I am using:
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
* [VS Code](https://code.visualstudio.com/download)
* [AZ CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

Python related VS Code extensions:

```
$ code --list-extensions | xargs -L 1 echo code --install-extension | grep -i python
code --install-extension donjayamanne.python-environment-manager
code --install-extension donjayamanne.python-extension-pack
code --install-extension KevinRose.vsc-python-indent
code --install-extension ms-python.isort
code --install-extension ms-python.pylint
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
```

Setting up local env:

```
pip install virtualenvwrapper
pip install virtualenv

echo "VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "source ~/.local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc 

git clone git@github.com:earthquakesan/azure-ad-search.git && cd azure-ad-search
mkvirtualenv -p $(which python3.11) azure-ad-search
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -e .
```

Running tests:

```
pytest -s tests/azureadsearch/test.py
```

## Running in Production

Setting up Enterprise application in Azure (local az-cli or cloud shell):

```
./create-app.sh
export CLIENT_ID=appId
export CLIENT_SECRET=password
export TENANT_ID=tenant
```

See tests for usage.
