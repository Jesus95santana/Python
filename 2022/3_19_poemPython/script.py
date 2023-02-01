highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_list = highlighted_poems.split(',')
# output(highlighted_poems_list):
# ['Afterimages:Audre Lorde:1997', '  The Shadow:William Carlos Williams:1915', ' Ecstasy:Gabriel a Mistral:1925', '   Georgia Dusk:Jean Toomer:1923', '   Parting Before Daybreak:An Qi:2014', '  The Untold Want:Walt Whitman:1871', " Mr. Grumpledump's Song:Shel Silverstein:2004", ' Angel S ound Mexico City:Carmen Boullosa:2013', ' In Love:Kamala Suraiyya:1965', ' Dream Variations:Lan gston Hughes:1994', ' Dreamwood:Adrienne Rich:1987']

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
    strippingPoem = poem.strip()
    highlighted_poems_stripped.append(strippingPoem)

# output(highlighted_poems_stripped):
# ['Afterimages:Audre Lorde:1997', 'The Shadow:William Carlos Williams:1915', 'Ecstasy:Gabriela M istral:1925', 'Georgia Dusk:Jean Toomer:1923', 'Parting Before Daybreak:An Qi:2014', 'The Untol d Want:Walt Whitman:1871', "Mr. Grumpledump's Song:Shel Silverstein:2004", 'Angel Sound Mexico City:Carmen Boullosa:2013', 'In Love:Kamala Suraiyya:1965', 'Dream Variations:Langston Hughes:1 994', 'Dreamwood:Adrienne Rich:1987']

highlighted_poems_details = []
for details in highlighted_poems_stripped:
    strippedDetails = details.split(':')
    highlighted_poems_details.append(strippedDetails)

# output(highlighted_poems_details):
# [['Afterimages', 'Audre Lorde', '1997'], ['The Shadow', 'William Carlos Williams', '1915'], ['E cstasy', 'Gabriela Mistral', '1925'], ['Georgia Dusk', 'Jean Toomer', '1923'], ['Parting Before  Daybreak', 'An Qi', '2014'], ['The Untold Want', 'Walt Whitman', '1871'], ["Mr. Grumpledump's Song", 'Shel Silverstein', '2004'], ['Angel Sound Mexico City', 'Carmen Boullosa', '2013'], ['I n Love', 'Kamala Suraiyya', '1965'], ['Dream Variations', 'Langston Hughes', '1994'], ['Dreamwo od', 'Adrienne Rich', '1987']]

titles = []
poets = []
dates = []

for sections in highlighted_poems_details:
    titles.append(sections[0])
    poets.append(sections[1])
    dates.append(sections[2])

for i in range(0, len(highlighted_poems_list)):
    statement = 'The poem {title} was published by {poet} in {date}.'
    loopedStatement = statement.format(title=titles[i], poet=poets[i], date=dates[i])
    print(loopedStatement)
