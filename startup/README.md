# IPython startup directory
```
This is the IPython startup directory

.py and .ipy files in this directory will be run *prior* to any code or files specified
via the exec_lines or exec_files configurables whenever you load this profile.

Files will be run in lexicographical order, so you can control the execution order of files
with a prefix, e.g.::

    00-first.py
    50-middle.py
    99-last.ipy
```


`~/.ipython/profile_default/startup`


- [00-misc.py](./00-misc.py)
    - [Rich adds support for Jupyter Notebooks](https://www.willmcgugan.com/blog/tech/post/rich-adds-support-for-jupyter-notebooks/)

- [01-chia.py](./01-chia.py)
- [02-chia-custom](./02-chia-custom.py)