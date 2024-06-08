new_str = "The cow jumped over the moon."
new_str.split()```
Output is:
```Python
['The', 'cow', 'jumped', 'over', 'the', 'moon.']```

#. Here  the separator is space, and the maxsplit argument is set to 3.
    ```Python
    new_str.split(' ', 3) ```
    Output is:
    ```Python
['The', 'cow', 'jumped', 'over the moon.']```

#. Using '.' or period as a separator.
```Python
new_str.split('.')```
Output is:
```Python
['The cow jumped over the moon', '']```

#4. Using no separators but having a maxsplit argument of 3.
    ```Python
    new_str.split(None, 3)```
    Output is:
    ```Python
['The', 'cow', 'jumped', 'over the moon.']```
