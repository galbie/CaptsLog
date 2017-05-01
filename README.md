# CaptsLog
[![codecov](https://codecov.io/gh/jaehoonhwang/CaptsLog/branch/master/graph/badge.svg)](https://codecov.io/gh/jaehoonhwang/CaptsLog) [![Build Status](https://travis-ci.org/jaehoonhwang/CaptsLog.svg?branch=master)](https://travis-ci.org/jaehoonhwang/CaptsLog)

Journal Application using python

## Specific package information:

- **Python 2.7**
- PyQt4
- Pyside
- Pymongo
- Markdown

## Project Documentation

[Github Page](http://jaehoonhwang.me/CaptsLog/html/)

### Documentation 

CaptsLog uses `sphinx` for its documentation need with extension of **napoleon**(google docstring convention).

Github offers github pages. Github pages for CaptsLog can be access through this [url](http://jaehoonhwang.me/CaptsLog/html/) or to view source code go to `gh-pages` branch of this documentation.

After following [google docstring convention](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

Go to `docs/` directory on the repository and run following command:

**Linux/OS X**

```bash
$ make html
```

**Windows**

```bash
$ makefile.bat html
```

#### Attention Contributors (Documentation)

Contributors should run following command after they have chagned/created snippets with documentation.

This command should be run while contributors are in `docs` directory.

```sh
sphinx-apidoc -f -o source/ ../captslog
```
