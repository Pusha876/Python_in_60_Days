# local-models

## Code
can be kept more organized if it is distributed across different Python files. Usually, function definitions are placed in one file, and the frontend interface in another. this is especially useful for larger programs.

---
```
from functions import get_todos, write_todos
todos - get_todos()
```
### from functions import get_todos, write_todos:
One Python file can be imported into another Python file using a "from module import object" syntax.

---
### todos - get_todos():
The imported function can be called in the file where it is imported.

---
```
import functions

todos = functions.get_todos()
```
### import functions:
Another way to import a file is to use the "import module" syntax.

---
### todos = functions.get_todos():
Once the module is imported through the "import module" method, the functions of that module can be called by referencing the module first.