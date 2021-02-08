highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

#split information into separate groups of info
highlighted_poems_list=highlighted_poems.split(',')
print(highlighted_poems_list)
highlighted_poems_stripped=[]

#strip the whitespaces
for poem in highlighted_poems_list: 
  highlighted_poems_stripped.append(poem.strip(" "))
print(highlighted_poems_stripped)

highlighted_poems_details=[]

#split the information into separate elements
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
print(highlighted_poems_details)

#creat empty lists
titles=[]
poets=[]
dates=[]

#assign list to appropriate elements
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])

#print out string for each poem
for index in list(range(len(titles))):
  string="The poem {title} was published by {poet} in {date}"
  string_format=string.format(title=titles[index],poet=poets[index],date=dates[index])
  print(string_format)






