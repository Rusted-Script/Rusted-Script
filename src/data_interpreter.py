import fileinput
from os import replace

file_name = input("what is the rusted script file name?: ")
sql_name = input("what do you want to sql file name to be?: ")

print(file_name)
print(sql_name)

with open(file_name + ".rusted", "r") as f:
    contents = f.read()

with open(sql_name + ".sql", 'w') as file:
    file.write(contents)

replace_texts = {"get" : "SELECT"}

for line in fileinput.input(sql_name + '.sql', inplace=True):
    for search_text in replace_texts:
        replace_text = replace_texts[search_text]
        line = line.replace(search_text,replace_text)
    print(line, end='')
