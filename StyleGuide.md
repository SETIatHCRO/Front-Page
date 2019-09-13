# HCRO STYLEGUIDE

## Python

Since python is widely used at the HCRO, SETI, and academia in general, this will be the most fleshed-out style guide.

You must adhear to the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/) with only a few deviations.

### Linting

> TLDR; running `pylint` on your files should have a score >= 9 

Lint your code with [pylint](https://www.pylint.org/). Install pylint with:
```
$ pip install pylint
```
And run it on your file with:
```
$ pylint myscript.py
```
Unless you are a statistical anomaly, this will show you dozens or hundreds or warnings and fixes along with a score. As a basic rule of thumb, **any score >= 9.0 passes** muster. If you find these warnings to be a little too pedantic, there are several things you can add to your config file `~/.pylintrc`.
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

### Note to Scientists 

A few pices of advice for those not trained in programming:

* Complexity is unavoidable but complicated code is optional. Try to avoid uniformly procedural programming which is programming where the execution runs through the program line by line (like how a jupyter notebook works). General advice is to write a class or function, make damn sure it works, then forget about it. This will make your programs readable and will help debugging. If you can reduce frustration while debugging, it will help you, your blood pressure, your relationships, the list goes on...
* It is much better to be over descriptive than under descriptive. Laziness isn't an excuse with modern text editors and IDEs which have auto-complete. `time_in_ms_since_jan_1970` is preferable to `t` although `time_utc` is probably ideal in this situation.
* The Python dictionary is the king of data types, know how to use them and your programs will be simpler and faster. 
