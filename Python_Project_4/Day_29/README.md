# App6 - Build a Weather Data API | Part 1

## Programming Tool/Concept
- HTML (In order to view live changes in VScode, Live Server extension was installed)
- Build a Website with Flask
---

### Build a Website

Certainly! The ```__name__ == "__main__"``` construct in Python is a common way to ensure that certain code is only executed when the script is run directly, and not when it is imported as a module in another script. Here's a simple example to illustrate its use:
```
# my_script.py

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```
Explanation:

- ```def main():```: This defines a function named ```main``` that contains the code you want to run.
- ```if __name__ == "__main__":```: This condition checks if the script is being run directly. If true, it calls the main function.


How it works:
- When you run ```my_script.py``` directly, ```__name__``` is set to ```"__main__"```, so the ```main``` function is executed, and "Hello, World!" is printed.

- If you import ```my_script``` in another script, the code inside the ```if``` block will not run, preventing "Hello, World!" from being printed automatically.

This construct is particularly useful for organizing code and ensuring that certain parts of your script are only executed in specific contexts.

---
### Running Multiple Apps
Flask development server by default listens on port ```5000``` so when you run a Flask app without port number it will run on ```5000```.

You can run a number of Flask app on the same machine but with the different port numbers. Let's say your scripts names are ```script1.py``` and ```script2.py```:
```
$ export FLASK_APP=script1.py
$ flask run --host 0.0.0.0 --port 5000
```
Open up a new terminal
```
$ export FLASK_APP=script2.py
$ flask run --host 0.0.0.0 --port 5001
```