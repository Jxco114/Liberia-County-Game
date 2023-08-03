import turtle
import pandas
screen = turtle.Screen()
screen.title('Liberia\'s County Game')
image = 'Liberia_location_map.svg.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('county.csv')
all_counties = data.county.to_list()
guessed_county = []

while len(guessed_county) < 15:
    answer_county = screen.textinput(title=f'{len(guessed_county)}/15 County Correct', prompt='What\'s another county\'s name?:').title()
    if answer_county == 'Exit':
        missing_county = [county for county in all_counties if county not in guessed_county]
        new_data = pandas.DataFrame(missing_county)
        new_data.to_csv('state_to_learn.csv')
        break
    if answer_county in all_counties:
        guessed_county.append(answer_county)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        county_data = data[data.county == answer_county]
        t.goto(county_data.iloc[0, 1], county_data.iloc[0, 2])
        t.write(answer_county)


