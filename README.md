# ABSA Subatomic User Documentation

[![Build Status](https://travis-ci.org/absa-subatomic/subatomic-documentation.svg?branch=master)](https://travis-ci.org/absa-subatomic/subatomic-documentation)
[![Requirements Status](https://requires.io/github/absa-subatomic/subatomic-documentation/requirements.svg?branch=gh-pages)](https://requires.io/github/absa-subatomic/subatomic-documentation/requirements/?branch=gh-pages)

Go to the [ABSA Subatomic User Documentation][live] 


## Getting Started

This project uses [MkDocs][]. MkDocs is a fast, simple static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file.

1. Install Python 3 on your machine.
2. Setup a Python [virtual environment][venv].
3. Navigate to the root of this project and install the dependencies using [pip][] as follows:

```
$ pip install -r requirements.txt
```

Once the dependencies are installed, you can start a local server to view the
docs:

```
$ mkdocs serve
```

[live]: http://subatomic.bison.ninja
[MkDocs]: http://www.mkdocs.org/
[Markdown]: https://daringfireball.net/projects/markdown/syntax
[venv]: https://virtualenv.pypa.io/en/stable/
[pip]: https://pip.pypa.io/en/stable/installing/