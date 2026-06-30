<h2 class="c-project-heading--task">Create a pie chart</h2>

Pie charts are a useful way of showing data. 

You will do a survey of favourite pets in your Code Club and then present the data as a pie chart.

## Step 1

Ask your club leader to help organise a survey. You could record the results on a computer connected to a projector or a whiteboard that everyone can see.

Write a list of pets and make sure everyone's favourite is included.

Then, get everyone to vote for their favourite by putting their hand up when it gets called out. Only one vote each!

For example:

<div class="c-project-output">
![A list of pets and the number of votes for each one.](images/pets-favourite.png)
</div>

## Step 2

To create a pie chart to show the results of your survey, you will use the `pygal` library to do some of the hard work.

First, import the `pygal` library:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 1
---
import pygal
--- /code ---
</div>

## Step 3

Now, create a pie chart and render (display) it:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 3-4
---
import pygal

piechart = pygal.Pie()
piechart.render()
--- /code ---
</div>

Don't worry, it gets more interesting when you add data!

## Step 4

Add in the data that you collected for one of the pets.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 4
---
import pygal

piechart = pygal.Pie()
piechart.add('Dog', 6)
piechart.render()
--- /code ---
</div>

There is only one piece of data, so it takes up the whole pie chart.

<div class="c-project-output">
![A pie chart with only one slice, labelled "Dog".](images/pets-add.png)
</div>

## Step 5

Now, add the rest of the data in the same way.

For example:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 5-8
---
import pygal

piechart = pygal.Pie()
piechart.add('Dog', 6)
piechart.add('Cat', 4)
piechart.add('Hamster', 3)
piechart.add('Fish', 2)
piechart.add('Snake', 1)
piechart.render()
--- /code ---
</div>

<div class="c-project-output">
![A pie chart with slices for all the types of pets.](images/pets-add-all.png)
</div>

## Step 6

To finish your chart, add a title:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 
line_highlights: 3
---
import pygal

piechart = pygal.Pie(title = 'Favourite Pet')
piechart.add('Dog', 6)
piechart.add('Cat', 4)
piechart.add('Hamster', 3)
piechart.add('Fish', 2)
piechart.add('Snake', 1)
piechart.render()
--- /code ---
</div>

## Now run your code

You should see a pie chart showing the survey results you entered.
