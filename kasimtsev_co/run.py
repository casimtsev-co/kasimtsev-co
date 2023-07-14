import subprocess
import sys

deps = [ "django", "django-multi-form-view" ]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main ():
    for dep in deps:
        install (dep)
    subprocess.check_call([sys.executable, "manage.py", "runserver", "84.38.184.188:80"])

if __name__ == "__main__":
    main()
