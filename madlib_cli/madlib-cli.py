import re
"""
Welcoming message
"""
print("***********************")
print("**THIS IS MADLIB Game**")
print("***********************")
"""
read_template function that takes in a path to text file and returns a stripped string of the file’s contents.
"""
def read_template(file_path:str)->str:
    try:
     with open (file_path) as file:
        content=file.read()
        return content.strip()
    except:
        print(file_path)
        raise FileNotFoundError

"""
parse function that takes in a template string and returns a string with language parts removed,
and a separate list of those language parts.
"""
def parse_template(word:str)->str:
 actual=tuple(re.findall(r'{(.*?)}',word))
 stripped=re.sub('{.*?}','{}',word)
 return stripped,actual

"""
merge function that takes in a “bare” template and a list of user entered language parts, 
and returns a string with the language parts inserted into the template.
"""
def merge(str_text:str,add_word:tuple):
    merged_text=str_text.format(*add_word)
    with open('assets/result.txt','w') as output:
        output.write(merged_text)
    return merged_text


"""
This is where the game starts and all other functions work
"""

def start_madlib():
    read_file=read_template("assets/text.txt")
    text,val=parse_template(read_file)
    result=[]
    for i in val:
        user_input=input(f"enter {i}")
        result.append(user_input)
    game_result=merge(text,result)
    return game_result

if __name__== "__main__":
    start_madlib()