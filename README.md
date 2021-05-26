# LinkShort-python-lib

## Purpose
This library uses the [LinkShort API](https://github.com/Tch1b0/LinkShort) to shorten your links.

### Example
You can easily create shortcuts and update them. This means **you can have static links**.

You could for example write a script that automatically updates a shortcut to your newest youtube video, so people can use the same link each time you upload something.

## Code example
### Create shortcut
```py
from LinkShort import Linker

my_shortcut = Linker.create("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

print(my_shortcut)
```
```
https://ls.johannespour.de/17a76043
```
This redirects you to https://www.youtube.com/watch?v=dQw4w9WgXcQ

### Edit shortcut

```py
...

my_shortcut.edit("https://other.example.com")

print(my_shortcut)
```
```
https://ls.johannespour.de/17a76043
```
This **now** redirects you to https://other.example.com

### Delete shortcut
```py
...

my_shortcut.delete()

print(my_shortcut)
```
```
empty
```

## Install lib
You can install the lib via [pip](https://en.wikipedia.org/wiki/Pip_(package_manager))

```sh
pip install git+https://github.com/Tch1b0/LinkShort-python-lib.git#egg=LinkShort
```