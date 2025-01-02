# Standard modules
are files containing functions that do more special operations than the functions included in the global Python namespace.

```
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
```

---
### import time:
Standard modules can be imported using an import statement just like local modules are imported.

---
### time.strftime("%b %d, %Y %H:%M:%S"):
Standard module functions can be called using the "**module.function()**" syntax.