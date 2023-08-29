import nltk
import spacy
import numpy as np
import pandas as pd
import copy as cp

sentence = '''As the lines progress, the intensity increases, the passion starts to burn, and when the images
of two birds of prey emerge, devouring time, instead of the other way round, the reader is
surely taken beyond mere pleasures of the flesh. Common sense and the logic of time will no
longer dictate their lives, if they come together. After analysing the poem, it is confirmed to
be a remarkable permutation of the phrase carpe diem.
Robert Herrick’s ‘To the Virgins, to make much of time’: In the same 17th century,
Robert Herrick incorporates in this poem the principle of carpe diem by almost echoing the
phrases used earlier by the ancient Latin poet Virgil: Collige, virgo, rosas (Gather, girl, roses)
and the 16th century French poet Pierre de Ronsard’s (1524 – 1585): ‘Mignonne, allons si la
rose…’ (Sweetheart, Come let us see if the rose which this morning unfolded its crimson
dress to the sun.’4 The French poet addresses to his sweetheart who could be Helen or Mary
or Cassandra and invites her to go with him to see if the rose that bloomed in the morning
with its fresh purple colour has lost its lustre in the evening! But alas! Nature seems to be
cruel that such a beautiful flower loses its colour, droops and sheds its petals in the evening.
It lasts only from dawn to dusk. Just like the rose flower that bloomed in the morning, she too
has flowered and bloomed so sweet and fresh in her youthful charm and beauty. Therefore, as
long as her young age flowers in its greenest freshness, she should gather and enjoy her
youthfulness. Otherwise old age will soon sully, dim and tarnish her charm and beauty.
In the backdrop of these Latin and French poets’ expression of carpe diem, Herrick calls the
young virgin girls to gather the roses and pluck their pleasures of their life to its full potential,
singing of the fleeting nature of life itself.
 Gather ye rosebuds while ye may,
 Old Time is still a-flying;
 And this same flower that smiles today
 Tomorrow will be dying.
The theme of carpe diem became so banal that most of the poets started writing of the brevity
of life and the urgency to enjoy it thoroughly.
Robert Frost’s poem on Carpe Diem: Frost’s speaker of the poem offers a different
approach to the age old theme of Seize the Day or carpe diem initiated by the classical
Roman poet Horace. In the first part of the poem the speaker personifies Age which observes
a pair of young lovers on a journey. He does not know where they are pressing forward. He
speculates that the couple may be going home or moving out of the home village or possibly
proceeding to church, because the ‘chimes are ringing’. Since the lovers are ‘strangers’ to the
speaker, he does not address them personally. But he wishes them all happiness in their life.
He elongates his advice of carpe diem: 5
 Be happy, happy, happy,
 And seize the day of pleasure
In the second part, the speaker exemplifies and evaluates the age-old adage of carpe diem by
alluding to Robert Herrick’s ‘To the Virgins to Make Much of Time’. He alludes to the rose
gathering by the virgins vis-à-vis the fleeting time. The speaker seems to laugh at the couple
basking in their over flooded happiness of the present moment of seizing and plucking the
day. Whatever attracts and stimulates the senses the mind and the heart, the brain becomes
overloaded with all the details of the present. He is of the opinion that their present or here
and now love is ‘too present to imagine’. The very idea of life being lived in the present is
cumbersome and unattainable because the human brain looks for something in future. The
speaker believes that life is lived ‘less in the present than in the future’. And the future in his
opinion is the fertile ground for the imagination. Imagining what one will do tomorrow, what
one will have for lunch, what job one will train for, where one will live, when one will get
married and what one’s children will look like etc. All these indicate the future time. '''
words = sentence.split()
bag_of_words = cp.deepcopy(words)
np.random.shuffle(bag_of_words)
# Bag of words:
# print(bag_of_words)

# Annotated words:
# nltk.download('popular')
# Using natural language toolkit
print("Using natural language toolkit:")
pos_tags = nltk.pos_tag(sentence.split())
print(pos_tags)
pos_tags_df = pd.DataFrame(pos_tags).T
print(pos_tags_df)

print("Using spacy to get parts of speech tags.")
nlp = spacy.load('en_core_web_sm')
pos_tags_2 = [ (word, word.tag_,  word.pos_) for word in nlp(sentence)]
pos_tags_2_df = pd.DataFrame(pos_tags_2).T
print(pos_tags_2)
print(pos_tags_2_df)


