import tweepy
import urllib.request
import random
from credentials import consumer_key, consumer_secret, access_token, access_token_secret

# Generate a silly name.
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

uppercase_words = [word for word in words if word[0].isupper()]
name_words  = [word for word in uppercase_words if not word.isupper()]
one_name = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])

# Generate the stats kinda unfairly.
stats = 3
erudite = random.randint(0, 3)

mod_stats = stats - erudite
skulker = random.randint(0, mod_stats)

final_stats = mod_stats - skulker
brute = final_stats

# Array of Items
all_items = ["a Melee Weapon (specify)", "a Ranged Weapon (specify)", "a Piece of Armor (specify)", "a Cloak (specify color)", "some Rations (specify)", "a Torch", "a Net", "a Bear Trap", "a Hammer", "a Mirror", "some Rope", "a pair of Manacles", "a Flask", "some Marbles", "a Piton", "a pair of Scissors", "some Wire", "a Flint Steel"]
subset_items = random.sample(all_items, 3)
items = ", & ".join([", ".join(subset_items[:-1]), subset_items[-1]])
# items = "\n- ".join(["\n- ".join(subset_items[:-1]), subset_items[-1]])

# Array of Portraits
goon_portraits = ["images/goon_a.png", "images/goon_b.png", "images/goon_c.png", "images/goon_d.png"]

class ATunnelGoonBot:
  def __init__(self, names):
    self.random_name(names)

    # initialize Twitter authorization with Tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    self.api = tweepy.API(auth)

  def random_name(self, names):
    self.model = ' '.join([name_words[random.randint(0, len(name_words))] for i in range(2)])

  def tweet(self):
    name = self.model
    portrait_list_item = random.sample(goon_portraits, 1)
    portrait = str(portrait_list_item)
    message = "Greetings " + name + ",\n\nYou have 10HP, & your Inventory Score is 8.\nYour stats are: " + str(brute) + " Brute, " + str(skulker) + " Skulker, & " + str(erudite) + " Erudite.\nYour possesions include " + items + ".\n\nGodspeed."
    # message = name + "\n\n10 Health Points\n8 Inventory Score\n\nStats:\n" + str(brute) + " Brute\n" + str(skulker) + " Skulker\n" + str(erudite) + " Erudite\n\nPossesions:\n- " + items
    try:
      self.api.update_with_media(portrait, message)
      print(message)
    except tweepy.TweepError as error:
      print(message)
      print(error.reason)

  def tweeter(self):
    self.tweet()

if __name__ == "__main__":
  goon = ATunnelGoonBot("names.txt")
  goon.tweeter()