## Read data from a file

It's useful to be able to store data in a file rather than having to include it in your code.

--- task ---

Add a new file to your project and call it `pets.txt`:

![screenshot](images/pets-file.png)
![shows the dialogue box for naming a file](images/name-file.png)

--- /task ---

--- task ---

Now add data to the file. You can use the favourite pets data that you collected or the example data.

--- code ---
---
language: python
filename: animals.txt
line_numbers: true
line_number_start: 
line_highlights: 
---
Dog 6
Cat 4
Hamster 3
Fish 2
Snake 1
--- /code ---

--- /task ---

--- task ---

Switch back to `main.py` and comment out the lines that render (display) charts and graphs (so that they aren't displayed):

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 9, 17
---
piechart.add('Snake', 1)
#piechart.render()

barchart = pygal.Bar(title = 'Favourite Pet')
barchart.add('Dog', 6)
barchart.add('Cat', 4)
barchart.add('Hamster', 3)
barchart.add('Fish', 2)
barchart.add('Snake', 1)
#barchart.render()
--- /code ---

--- /task ---

--- task ---

Now read the data from the file.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 19
line_highlights: 19-24
---
file = open('pets.txt', 'r')

for line in file.read().splitlines():
    print(line)

file.close()
--- /code ---

The `for` loop will loop over the lines in the file. `splitlines()` removes the newline character from the end of the line as you don't want that.

--- /task ---

--- task ---

Each line needs to be separated into a label and a value:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 22
---
for line in file.read().splitlines():
        label, value = line.split(' ')
        print(label, value)
--- /code ---

This will split the line at the spaces so don't include spaces in the labels. (You can add support for spaces in labels later.)

--- /task ---


You might get an error like this:

![screenshot](images/pets-error.png)

This happens if you have an empty line at the end of your file.

You can fix the error by only getting the label and value if the line isn't empty.

--- task ---

Indent the code inside your `for` loop and add the code `if line:` above it:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 22
---
for line in file.read().splitlines():
    if line:
        label, value = line.split(' ')
        print(label, value)
--- /code ---

--- /task ---

--- task ---

Remove the `print(label, value)` line now everything is working, and add the label and value to a new Pie Chart and render it:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 19
line_highlights: 19, 26, 30
---
piechart2 = pygal.Pie()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))

file.close

piechart2.render()
--- /code ---

Note that `add` expects the value to be a number, `int(value)` turns the value from a string into an integer.

If you wanted to use decimals such as 3.5 (floating point numbers) you could use `float(value)` instead.

--- /task ---

