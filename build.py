import subprocess

try:
    import pyperclip
except ImportError:
    subprocess.call(['python', '-m', 'pip', 'install', 'pyperclip'])