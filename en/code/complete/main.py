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

# pets_chart.render()   # Render a pie chart (commented out)
pets_bars.render()  # Render a bar chart instead