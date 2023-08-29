import nltk
import os
import spacy
import numpy as np
import pandas as pd
import copy as cp
import joblib

sentence = '''O resto fez-me ficar mais algum tempo, no corredor, pensando. Vi entrar o Dr. João da Costa, e preparou-se logo o voltarete do costume. Minha mãe saiu da sala, e, dando comigo, perguntou se acompanhara Capitu.
– Não, senhora, ela foi só.
E quase investindo para ela:
– Mamãe, eu queria dizer-lhe uma coisa.
– Que é?
Toda assustada, quis saber o que é que me doía, se a cabeça, se o peito, se o estômago, e apalpava-me a testa para ver se tinha febre.
– Não tenho nada, não, senhora.
– Mas então que é?
– É uma coisa, mamãe... Mas, escute, olhe, é melhor depois do chá; logo... Não é nada mau; mamãe assusta-se por tudo; não é coisa de cuidado.
– Não é moléstia?
– Não, senhora.
– É, isso é volta de constipação. Disfarças para não tomar suadouro, mas tu estás constipado; conhece-se pela voz.
Tentei rir, para mostrar que não tinha nada. Nem por isso permitiu adiar a confidência; pegou em mim, levou-me ao quarto dela, acendeu vela, e ordenou-me que lhe dissesse tudo. Então eu perguntei-lhe, para principiar, quando é que ia para o seminário.
– Agora só para o ano, depois das férias.
– Vou... para ficar?
– Como ficar?
– Não volto para casa?
– Voltas aos sábados e pelas férias; é melhor. Quando te ordenares padre, vens morar comigo.
Enxuguei os olhos e o nariz. Ela afagou-me, depois quis repreender-me, mas creio que a voz lhe tremia, e pareceu-me que tinha os olhos úmidos. Disse-lhe que também sentia a nossa separação. Negou que fosse separação; era só alguma ausência, por causa dos estudos; só os primeiros dias. Em pouco tempo eu me acostumaria aos companheiros e aos mestres, e acabaria gostando de viver com eles.
– Eu só gosto de mamãe.
Não houve cálculo nesta palavra, mas estimei dizê-la, por fazer crer que ela era a minha única afeição; desviava as suspeitas de cima de Capitu. Quantas intenções viciosas há assim que embarcam, a meio caminho, numa frase inocente e pura! Chega a fazer suspeitar que a mentira é, muita vez, tão involuntária como a transpiração. Por outro lado, leitor amigo, nota que eu queria desviar as suspeitas de cima de Capitu, quando havia chamado minha mãe justamente para confirmá-las; mas as contradições são deste mundo. A verdade é que minha mãe era cândida como a primeira aurora, anterior ao primeiro pecado; nem por simples intuição era capaz de deduzir uma coisa de outra, isto é, não concluiria da minha repentina oposição que eu andasse em segredinhos com Capitu, como lhe dissera José Dias. Calou-se durante alguns instantes; depois replicou-me sem imposição nem autoridade, o que me veio animando à resistência. Daí o falar-lhe na vocação que se discutira naquela tarde, e que eu confessei não sentir em mim.
– Mas tu gostavas tanto de ser padre, disse ela; não te lembras que até pedias para ir ver sair os seminaristas de S. José, com as suas batinas? Em casa, quando José Dias te chamava Reverendíssimo, tu rias com tanto gosto! Como é que agora?... Não creio, não, Bentinho. E depois... Vocação? Mas a vocação vem com o costume, continuou repetindo as reflexões que ouvira ao meu professor de latim.
Como eu buscasse contestá-la, repreendeu-me sem aspereza, mas com alguma força, e eu tornei ao filho submisso que era. Depois, ainda falou gravemente e longamente sobre a promessa que fizera; não me disse as circunstâncias, nem a ocasião, nem os motivos dela, coisas que só vim a saber mais tarde. Afirmou o principal, isto é, que a havia de cumprir, em pagamento a Deus.
– Nosso Senhor me acudiu, salvando a tua existência, não lhe hei de mentir nem faltar, Bentinho; são coisas que não se fazem sem pecado, e Deus que é grande e poderoso, não me deixaria assim, não, Bentinho; eu sei que seria castigada e bem castigada. Ser padre é bom e santo; você conhece muitos, como o Padre Cabral, que vive tão feliz com a irmã; um tio meu também foi padre, e escapou de ser bispo, dizem... Deixa de manha, Bentinho.
Creio que os olhos que lhe deitei foram tão queixosos, que ela emendou logo a palavra, manha, não, não podia ser manha, sabia muito bem que eu era amigo dela, e não seria capaz de fingir um sentimento que não tivesse. Moleza é o que queria dizer, que me deixasse de moleza, que me fizesse homem e obedecesse ao que cumpria, em benefício dela e para bem da minha alma. Todas essas coisas e outras foram ditas um pouco atropeladamente, e a voz não lhe saía clara, mas velada e esganada. Vi que a emoção dela era outra vez grande, mas não recuava dos seus propósitos, e aventurei-me a perguntar-lhe:
– E se mamãe pedisse a Deus que a dispensasse da promessa?
– Não, não peço. Estás tonto, Bentinho? E como havia de saber que Deus me dispensava?
– Talvez em sonho; eu sonho às vezes com anjos e santos.
– Também eu, meu filho; mas é inútil... Vamos, é tarde; vamos para a sala. Está entendido: no primeiro ou no segundo mês do ano que vem, irás para o seminário. O que eu quero é que saibas bem os livros que estás estudando; é bonito, não só para ti, como para o Padre Cabral. No seminário há interesse em conhecer-te, porque o Padre Cabral fala de ti com entusiasmo.
Caminhou para a porta, saímos ambos. Antes de sair, voltou-se para mim, e quase a vi saltar-me ao colo e dizer-me que não seria padre. Este era já o seu desejo íntimo, à proporção que se aproximava o tempo. Quisera um modo de pagar a dívida contraída, outra moeda, que valesse tanto ou mais, e não achava nenhuma. '''
words = sentence.split()
bag_of_words = cp.deepcopy(words)
np.random.shuffle(bag_of_words)
# Bag of words:
# print(bag_of_words)

# Annotated words:
# nltk.download('popular')
# Using natural language toolkit
print("Usando o natural language toolkit:")
# Use lang with ISO 639 code of the language
#pos_tags = nltk.pos_tag(sentence.split(), lang="pt") # not implemented.

# Reference to get the trained model:
# https://github.com/inoueMashuu/POS-tagger-portuguese-nltk
# trained_data_folder = os.path.abspath(__)  'python\introduction\data'

portuguese_tagger = joblib.load('data/POS_tagger_brill.pkl')
pos_tags = portuguese_tagger.tag(nltk.word_tokenize(sentence))
print(pos_tags)
pos_tags_df = pd.DataFrame(pos_tags).T
print(pos_tags_df)

print("Usando o Spacy para se obter as partes do discurso.")
## https://spacy.io/models/pt
model_spacy = spacy.load('pt_core_news_sm')
pos_tags_2 = [ (word, word.pos_) for word in model_spacy(sentence)]
pos_tags_2_df = pd.DataFrame(pos_tags_2).T
print(pos_tags_2)
print(pos_tags_2_df)


