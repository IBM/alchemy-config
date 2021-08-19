# aconfig-py
Configuration framework in Python for Watson-NLU services.

# How to Get Started

1. Make sure you have `pip3` installed.
2. Sync with project using `pip3`:
```
# make sure you are in aconfig-py directory

# install requirements
pip3 install -r requirements.txt
```

# Run unit tests

1. Run:
```
./ci/run_tests.sh
```

# Corner-case Behavior

You CAN set builtin method names as attributes on the `config`. However, you should only access/delete them via dictionary access methods.

For example:

```
c = {'update': True}

config = Config(c)

# DO NOT DO THIS:
config.update

# DO THIS INSTEAD:
config['update']
```

This is because there is no way in Python to tell whether you want the method or the attribute `'update'` when "getting" it from the object.
