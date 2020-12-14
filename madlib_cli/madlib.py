import re

def user_welcome():
    print("""
    ** Welcome to MadLib Cli, ready to play? **
    ** Instructions: You will be given a     **
    ** prompt with certain words missing     **
    ** denoted by their type of word you will**
    ** chose how they are filled and we will **
    ** provide you with humor                **
     """)
def read_template(txt_file):
    with open(txt_file) as text:
        madlib = text.read()
        return madlib
"""[summary] 
    Takes in a text file path
    returns read text file
    """

def parse_template(txt):
    new = tuple(re.findall(r"\{([A-Za-z0-9_'\s1-]+)\}", txt, re.IGNORECASE))
    length = len(new)
    for i in range(0,length):
        if( i == 0 ):
            print(i)
            new_txt = txt.replace(new[i],"")
        else:
            new_txt = new_txt.replace(new[i],'')
    return  new_txt,new
"""[summary]
    Takes in read text file
    Parses all text out of 
    file returns the split text
    and what was parsed from it
    """

def user_prompt(words):
    print('Please enter in appropirate resopnses for the prompts')
    responses = []
    for word in words:
        responses.append(input(f'Please enter {word}'))
    return(responses)
"""[summary]
    Takes in parsed words
    prompts user for a response according
    to parsed words returns the responses
    """

def merge(strip,res):
    length = len(res)
    for i in range(0, length):
        if( i == 0):
            story = strip.replace('{}',res[i],1)
        else:
            story = story.replace('{}',res[i],1)
    return story
"""[summary]
    takes in the stripped text and the
    user responses and replaces all {} with 
    the words of matching index returns the
    finished story
    """


def game():
    stripped, promtps = parse_template(read_template('../assets/madlib.txt'))

    res = user_prompt(promtps)
    fout = open("../assets/libstory.txt", 'w')
    fout.write(merge(stripped,res))

    fout.close()
    print(merge(stripped,res))

# comment live 77 for testing functions uncomment to play game
# game()



# I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

# What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.