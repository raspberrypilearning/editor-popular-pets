<h2 class="c-project-heading--task">Create a bar graph</h2>

--- task ---
Create a bar graph using the same data from <code>pets.txt</code>. You will need to **comment out** the line that renders the chart, and add one to render the bar graph instead.
--- /task ---

You can make a bar graph in the same way as a pie chart — the main difference is the chart type.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4, 12, 14-15
---
import pygal  # Create charts in Python

pets_chart = pygal.Pie(title='Popular pets')
pets_bars = pygal.Bar(title='Popular pets')  # Create a bar chart

with open('pets.txt', 'r') as file:
    for line in file.read().splitlines():
        line = line.strip()
        if line:
            label, value = line.split(': ')
            pets_chart.add(label, int(value))
            pets_bars.add(label, int(value))  # Add data to the bar chart

# pets_chart.render()   # Comment this line to skip it when the code runs
pets_bars.render()  # Render a bar chart instead

--- /code ---
</div>

--- task ---
**Test:** Click **Run**.

You should see a bar graph created from the same data.

--- /task ---

<div class="c-project-output">
<pre>
  <img src="images/pets-finished.png"
       alt="A bar graph showing multiple types of pets."></pre>
</div>