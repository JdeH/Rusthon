Introduction
------------
PythonJS is a transpiler written in Python that converts Python into fast JavaScript.  It can be run with regular Python, or fully self-hosted within NodeJS using Empythoned.  PythonJS has been designed with speed and easy integration with existing JavaScript code in mind.

Installing
-------------
	npm install python-js

NodeJS Quick Example
--------------

```
var pythonjs = require('python-js');
var pycode = "a = []; a.append('hello'); a.append('world'); print(a)";
var jscode = pythonjs.translator.to_javascript( pycode );
eval( pythonjs.runtime.javascript + jscode );

```

JavaScript API
----------
```
var pythonjs, output;
pythonjs = require('python-js');
output = pythonjs.translator.to_javascript( input );
output = pythonjs.translator.to_javascript_module( input );
output = pythonjs.translator.to_dart( input );
output = pythonjs.translator.to_coffee( input );
output = pythonjs.translator.to_lua( input );

pythonjs.runtime.javascript // runtime required by translator output

```

Example Projects
----------------
[https://github.com/PythonJS/pythonjs-demo-server-nodejs](https://github.com/PythonJS/pythonjs-demo-server-nodejs)
[https://github.com/PythonJS/pypubjs](https://github.com/PythonJS/pypubjs)


Speed
---------------
PythonJS allows you to select which features you need for
each section of your code, where you need performance you
can disable operator overloading, and other slow operations.
Features can be switched off and on for blocks of code using
`pythonjs.configure()` or the special `with` statements and
decorators described below.  When PythonJS is run in fastest
mode (javascript mode) it beats native PyPy in the Richards, and N-Body benchmarks.

N-Body benchmark
![nbody](http://2.bp.blogspot.com/-pylzspKRu6M/UqbAv3qIGTI/AAAAAAAAAkE/NnsAM5DZ_8M/s400/nbody.png)



translator.py
------------
To simply convert your python script into javascript, git clone this repo, and use translator.py located in the "pythonjs" directory.  You can give it a list of python files to translate at once.  It will output the translation to stdout.  The default output type is JavaScript.

Usage::

	translator.py [--dart|--coffee|--lua] file.py

Example::

	cd PythonJS/pythonjs
	./translator.py myscript.py > myscript.js


Supported Features
================

####Language
	
	classes
	multiple inheritance
	operator overloading
	function and class decorators
	getter/setter function decorators
	list comprehensions
	yield (generator functions)
	regular and lambda functions
	function calls with *args and **kwargs



####builtins

	type
	hasattr
	getattr
	setattr
	issubclass
	isinstance
	dict
	list
	tuple
	int
	float
	str
	round
	range
	sum
	len
	map
	filter
	min
	max
	abs
	ord
	chr
	open  (nodejs only)

####List

	list.append
	list.extend
	list.remove
	list.insert
	list.index
	list.count
	list.pop
	list.__len__
	list.__contains__
	list.__getitem__
	list.__setitem__
	list.__iter__
	list.__getslice__

####Set

	set.bisect
	set.difference
	set.intersection
	set.issubset

####String

	str.split
	str.splitlines
	str.strip
	str.startswith
	str.endswith
	str.join
	str.upper
	str.lower
	str.index
	str.find
	str.isdigit
	str.format
	str.__iter__
	str.__getitem__
	str.__len__
	str.__getslice__

####Dict

	dict.copy
	dict.clear
	dict.has_key
	dict.update
	dict.items
	dict.keys
	dict.get
	dict.set
	dict.pop
	dict.values
	dict.__contains__
	dict.__iter__
	dict.__len__
	dict.__getitem__
	dict.__setitem__

####Libraries

	time.time
	time.sleep
	math.sin
	math.cos
	math.sqrt
	os.path.dirname
	bisect.bisect
	random.random
	threading.start_new_thread

------------------------------

Regression Tests
================

The best way to see what features are currently supported with each of the backends
is to run the automated regression tests in PythonJS/regtests.  To test all the backends
you need to install NodeJS, CoffeeScript, and Dart2JS.  You should download the Dart SDK,
and make sure that the executeable `dart2js` is in `~/dart-sdk/bin/`

####Run Regression Tests

	cd PythonJS/regtests
	./run.py


Community
---------

[https://groups.google.com/forum/#!forum/pythonjs](https://groups.google.com/forum/#!forum/pythonjs)

irc freenode::

	#pythonjs


![bitdeli](https://d2weczhvl823v0.cloudfront.net/PythonJS/pythonjs/trend.png)
