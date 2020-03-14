from install_apps import install_apps
from validate import validate
from setup_workspace import setup_workspace

def main():
    validate()
    setup_workspace()
    install_apps()

if __name__ == '__main__':
    main()
