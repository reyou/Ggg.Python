//=============================================================================
// https://docs.python.org/3/installing/index.html#installing-index
// https://packaging.python.org/
//=============================================================================
var pip = {
    "Pip not installed": "python -m ensurepip --default-pip",
    "list": "pip list",
    "list-legacy": "pip list --format=legacy",
    "list-columns": "pip list --format=columns",
    // pip freeze will produce a similar list of the installed packages
    "freeze": "pip freeze > requirements.txt",
    "requirements": "pip install -r requirements.txt",
    "search": "pip search request",
    "install": "pip install SomePackage",
    "uninstall": "pip uninstall SomePackage",
    "show": "pip show requests",
    "specific version": "pip install SomePackage==1.0.4",
    "minimum version": 'pip install "SomePackage>=1.0.4"',
    "upgrade": 'pip install --upgrade SomePackage',
    "just for the current user": 'pip install SomePackage --user',
}
//=============================================================================