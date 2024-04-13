# Imports
import ollama
import random
import mastodon
from mastodon import Mastodon

# Read curses file
file = open('./haddocks.txt', 'r')
data = file.read()
file.close()

# Format list
datalist = data.split('\n')

# Pick random curse
randomindex = random.randint(0, len(datalist) -1)
randomcurse = datalist[randomindex]

# Remove random curse from the list
del datalist[randomindex]

# Write shortened list back
file=open('./haddocks.txt', 'w')
for item in datalist: 
    file.write(item + '\n')
file.close()

# llama-2 
# Formulate response
response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'What does Captain Haddock mean when he says in less than 300 characters: {}'.format(randomcurse),
  },
])

# Format results
result = randomcurse + ': ' + str(response['message']['content'])

# Post on Mastodon
m = Mastodon(access_token="###Your#Key#here####", api_base_url="https://mastodon.social/")
m.toot(result)
