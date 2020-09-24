import tweepy

from authorization_tokens import *

import random

# #option 1 - pick random phrase from list:
# phrase_list = [ "Hi my name is Tweepy",
#                 "Tweepy is my name, twitter is my game",
#                 "I was born to tweet" ]
# random_number = random.randrange( len(phrase_list) )
# message = phrase_list [random_number]

#option 2 - create sentence template w/ blanks & pick a random word from list to fill in:
# word_list = ["dogs", "cats", "rats", "birds",]
# string_template = "some people prefer {}, but personally I love {}."
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list[random_number]
# random_number = random.randrange( len(word_list) )
# word2 = word_list[random_number]
#
# message = string_template.format(word1,word2)

#option 3 - pick a random template from list; pick words from list; use words to fill in template:
word_list = ["gymnastics", "ballet", "kickboxing", "yoga", "crossfit"]
template_list = [ "If you're good at {}, then you'll probably be great at {}!",
                  "I may look like I'm into {}, but my real passion is {}",
                  "I really hate {}, it's so boring. I would much rather go to a {} class"]
random_number = random.randrange( len(template_list) )
template = template_list[random_number]

random_number = random.randrange( len(word_list) )
word1 = word_list[random_number]

random_number = random.randrange( len(word_list) )
word2 = word_list[random_number]

random_number = random.randrange( len(word_list) )
word3 = word_list[random_number]

random_number = random.randrange( len(word_list) )
word4 = word_list[random_number]

message = template.format(word1,word2,word3,word4)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
