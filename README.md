# Animated Texts
A tool to animate text.


## Required Modules
- OS (It is already installed on Windows.)
- Time (It is already installed on Windows.)


## Usage
```python

var1 = at(text, cooldown,mode)

# var1 = variable name, you can choose anything.

# text = the text you want animated.

# cooldown = waiting time for the new letter. (second)

# mode = mode. there are 3 modes:
# mode 1 => letters are printed on the screen in order.
# mode 2 => letters are printed with a "-" sign between them.
# mode 3 => letters are printed from right to left.

```

## Example Usage
```python
import  animate
variable = animate.at("Hello world!", 0.05, 1)
variable.animate()
```
