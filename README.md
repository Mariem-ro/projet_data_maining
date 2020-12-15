# <br color="red">Projet data maining</br>
# <br>Objectifs :</br>
<br>• Maitriser l’API de twitter pour l’extraction des tweets</br>
<br>• Maitriser la partie NLP (natural language processing) avec NLTK en Python</br>
<br>• Appliquer les principes de nettoyage des données</br>
<br>• Classer les tweets : regrouper ensemble les tweets qui sont similaires. C’est une étape qui peut
être considérée comme une étape </br>
# <br> Extraction des tweets par tweepy</br>
<br>Reference :http://docs.tweepy.org/en/latest/api.html</br>
<br>Reference :http://docs.tweepy.org/en/latest/</br>
<br>Reference :http://docs.tweepy.org/en/latest/streaming_how_to.html</br>

![tweetscollect](https://user-images.githubusercontent.com/66451325/102276023-881f6c80-3f26-11eb-892e-fbc10c94aed9.gif|width=100)

# <br> Tweets cleaning</br>
 <br> Dans cette étape, l’objectif est d’éliminer le texte inutile des tweets tels que les #, les noms des
utilisateurs, les url, …</br>
# <br> NLPK pour cleaning</br>
 <br> On doit procéder à l’analyse du tweet en respectant les différentes étapes du NLP (Natural
LanguageProcessing). La bibliothèque à utiliser est NLTK en Python</br>
# <br> classification des Tweets avec Kmeans</br>
<br>Etant donné un ensemble de tweets, l’objectif est de les résumer sous formes de groupes de sorte à
ce que les Tweets qui sont dans le même groupe soient similaires. Ainsi, l’utilisateur pourra par la
suite lire juste un Tweet de chaque groupe (le Tweet qui est le centroïde de groupes)</br>
essayez on binder : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mariem-ro/projet_data_maining/main)
