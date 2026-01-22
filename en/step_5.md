<h2 class="c-project-heading--task">Challenges: Explore more charts</h2>

--- task ---
Create **your own graph** using a new data set:

1. Choose a topic everyone will understand.  
2. Collect the results, update <code>pets.txt</code> (or create a new file), and generate a bar or pie chart.

Ideas:
- Favourite sport  
- Favourite ice cream flavour  
- How you get to school  
- Birthday month  
- Do you play Minecraft? (yes/no)

Don’t collect personal data (for example, where people live).  
Ask your club leader if you’re unsure.

--- /task ---

--- task ---
Create a **new chart from a different data file**:

Add a new <code>.txt</code> file and use it to build a pie chart or bar graph. Some example files have been included for you: <code>butterflies.txt</code> and <code>piratesninjas.txt</code>

<img src="images/pets-pn-bar.png"
       alt="A pie chart showing multiple types of pets.">
<img src="images/pets-butterflies.png"
       alt="A pie chart showing multiple types of pets.">

<div class="c-project-callout c-project-callout--tip">

### Tip
- Create your own datafile by clicking the `Add file` button on the Project files tab:
![The project files tab in the raspberry pi editor, showing a blue Add file button circled in red.](images/add-file.png)
- To allow spaces in labels, use this format in your file: <pre>Red Admiral: 6</pre>, then split each line using: <code>line.split(': ')</code>

</div>

--- /task ---

--- task ---
Let the user **choose** which chart to see:

Ask the user whether they want a **pie chart** or a **bar graph**, then show the chart they choose.

<div class="c-project-callout c-project-callout--tip">

### Tip

- Use <code>input()</code> to ask the question
- Use <code>if</code> / <code>else</code> to decide which chart to render
</div>
--- /task ---
