# HCRO STYLEGUIDE

## Python

Since python is widely used at the HCRO, SETI, and academia in general, this will be the most fleshed-out style guide.

You must adhear to the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/) with only a few deviations.

### Linting

Lint your code with [pylint](https://www.pylint.org/). Install pylint with:
```
$ pip install pylint
```
And run it on your file with:
```
$ pylint myscript.py
```
Unless you are a statistical anomaly, this will show you dozens or hundreds or warnings and fixes along with a score. As a basic rule of thumb, ** any score >= 9.0 passes ** muster. If you find these warnings to be a little too pedantic, there are several things you can add to your config file `~/.pylintrc`.
* disable=invalid-name  This will allow you to use variable names like `ra` and `el` but use them sparingly.
* Want to disable the warnings about tabs? Too bad, don't.


### Keepin' it Stylish   
There is a great auto-linter called [autopep8](https://pypi.org/project/autopep8/), a script that will fix all the little things it can. This will take care of the majority of the linters warnings with one command.

Install with:

```
$ pip install autopep8
```

And run the script with:

```
$ autopep8 --in-place --aggressive --aggressive myscript.py
```

Or if there's no chance in hell youll remember that, try adding an alias like so:

```
$ echo "alias mylint='autopep8 --in-place --aggressive'" >> ~/.bash_profile
$ source  ~/.bash_profile
$ mylint myscript.py
```

//TODO add section on git-hooks?
