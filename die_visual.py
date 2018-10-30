from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)
die_3 = Die(12)
results = [die_1.roll() + die_2.roll() + die_3.roll() for  roll_num in range(50000)]
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(min(results), max_result+1)]
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = list(range(min(results), max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')