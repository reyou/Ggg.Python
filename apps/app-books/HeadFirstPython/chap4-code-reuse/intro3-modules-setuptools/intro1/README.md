```
$ cd mymodule
$ py -3 setup.py sdist
```

### py -3 setup.py sdist

```
$ py -3 setup.py sdist
running sdist
running egg_info
creating vsearch.egg-info
writing vsearch.egg-info\PKG-INFO
writing dependency_links to vsearch.egg-info\dependency_links.txt
writing top-level names to vsearch.egg-info\top_level.txt
writing manifest file 'vsearch.egg-info\SOURCES.txt'
reading manifest file 'vsearch.egg-info\SOURCES.txt'
writing manifest file 'vsearch.egg-info\SOURCES.txt'
running check
creating vsearch-1.0
creating vsearch-1.0\vsearch.egg-info
copying files to vsearch-1.0...
copying README.txt -> vsearch-1.0
copying setup.py -> vsearch-1.0
copying vsearch.py -> vsearch-1.0
copying vsearch.egg-info\PKG-INFO -> vsearch-1.0\vsearch.egg-info
copying vsearch.egg-info\SOURCES.txt -> vsearch-1.0\vsearch.egg-info
copying vsearch.egg-info\dependency_links.txt -> vsearch-1.0\vsearch.egg-info
copying vsearch.egg-info\top_level.txt -> vsearch-1.0\vsearch.egg-info
Writing vsearch-1.0\setup.cfg
creating dist
Creating tar archive
removing 'vsearch-1.0' (and everything under it)
```

### Build Result

![](https://i.imgur.com/fLsBy2c.png)

### Installing Packages with “pip”

Locate your newly created ZIP file under the dist folder (recall that the file is
called vsearch-1.0.zip)

```
$ cd D:\...\...\intro1\mymodules\dist
$ py -3 -m pip install vsearch-1.0.zip

The vsearch module is now installed as part of site-packages.
Now that our vsearch module has been installed, we can use import vsearch
in any of our programs, safe in the knowledge that the interpreter can now find the
module’s functions when needed.
```
