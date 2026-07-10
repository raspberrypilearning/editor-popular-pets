## Read data from a file

It is useful to be able to store data in a file, rather than having to include it in your code.

## Step 1

Add a new file to your project and call it `pets.txt`:

![The 'Add file' button highlighted in the 'Project files' menu.](images/pets-file.png)
![The 'Name your file' dialogue box with pets.txt in the text field.](images/name-file.png)

## Step 2

Now, add data to the file. You can use the favourite pets data that you collected or the example data here.

```python filename="pets.txt" line_numbers="true"
Dog 6
Cat 4
Hamster 3
Fish 2
Snake 1
```

## Step 3

Switch back to `main.py` and comment out the lines that render (display) charts (so that they are not displayed):

```python filename="main.py" line_numbers="true" line_number_start="8" line_highlights="9,17"
piechart.add('Snake', 1)
#piechart.render()

barchart = pygal.Bar(title = 'Favourite Pet')
barchart.add('Dog', 6)
barchart.add('Cat', 4)
barchart.add('Hamster', 3)
barchart.add('Fish', 2)
barchart.add('Snake', 1)
#barchart.render()
```

## Step 4

Now, read the data from the file.

```python filename="main.py" line_numbers="true" line_number_start="19" line_highlights="19-24"
file = open('pets.txt', 'r')

for line in file.read().splitlines():
    print(line)

file.close()
```

The `for` loop will loop over the lines in the file. `splitlines()` will remove the newline character from the end of each line, as you do not want those.

## Step 5

You need to separate each line into a label and a value:

```python filename="main.py" line_numbers="true" line_number_start="21" line_highlights="22-23"
for line in file.read().splitlines():
    label, value = line.split(' ')
    print(label, value)
```

This will split the line at the spaces, so do not include spaces in the labels. (You can add support for spaces in labels later.)

You might get an error like this:

![An error message in the output area: "ValueError: not enough values to unpack (expected at least 2, got 1) on line 22 of main.py".](images/pets-error.png)

This happens if you have an empty line at the end of your file.

You can fix the error by only getting the label and value if the line is not empty.

## Step 6

Indent the code inside your `for` loop and add the code `if line:` above it:

```python filename="main.py" line_numbers="true" line_number_start="21" line_highlights="22-24"
for line in file.read().splitlines():
    if line:
        label, value = line.split(' ')
        print(label, value)
```

## Step 7

Now that everything is working, remove the `print(label, value)` line, and add the label and value to a new pie chart and render it:

```python filename="main.py" line_numbers="true" line_number_start="19" line_highlights="19,26,30"
piechart2 = pygal.Pie()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
    if line:
        label, value = line.split(' ')
        piechart2.add(label, int(value))

file.close()

piechart2.render()
```

Note that `add` expects the value to be a number. `int(value)` turns the value from a string into an integer.

If you wanted to use decimals such as 3.5 (floating-point numbers), you could use `float(value)` instead.

## Now run your code

You should see a chart created from the data in `pets.txt`.
