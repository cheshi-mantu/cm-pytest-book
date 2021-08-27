The project `tasks_proj` is used in much of the book.

The test code changes over the course of the book, but the source code changes (will change) only once.

The test code for a package really ought to be part of the package.
However, it really seems wasteful to copy the project source code into every chapter just to watch the test code change.

Therefore, we won't.

The directory `tasks_proj` will be used for at least chapters 1-6.
The directory `tasks_proj_v2` contains a fix for running tasks with mongo.

There other `ch[2-6]/tasks_proj` directories maintain the directory structure through `tests` and the `tests` subdirectories, but won't contain the package under test.

Therefore, you can `pip install tasks_proj` at the top level and use it for testing the chapters 1-6.

--------------------------------------------
Regarding CHANGELOG.rst and version numbers:
--------------------------------------------

Versions for tasks *mostly* follow `Semantic Versioning`.

Normally, that means ...

Given a version number MAJOR.MINOR.PATCH, the:

- MAJOR versions are the only place where incompatible API changes are made. 
- MINOR versions can add functionality in a backwards-compatible manner.  
- PATCH versions will have backwards-compatible bug fixes or minor tweaks to implementation.  

Also, since we don't have version control to rely on for tasks:

- MINOR versions will increment with changes to src (``tasks_proj/src``).
- PATCH versions will increment with any other change.

A CHANGELOG.rst file is present in the "tasks_proj" directories with 
more detail than is often present in change log.
In place of version control, I'll list every file that's different 
from previous directories.

