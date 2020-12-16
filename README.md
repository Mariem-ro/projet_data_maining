# <br color="red">Projet data maining</br>
# <br>Objectifs :</br>
<br>• Maitriser l’API de twitter pour l’extraction des tweets</br>
<br>• Maitriser la partie NLP (natural language processing) avec NLTK en Python</br>
<br>• Appliquer les principes de nettoyage des données</br>
<br>• Classer les tweets : regrouper ensemble des tweets qui sont similaires. </br>
# <br> Extraction des tweets par tweepy</br>
<br> Nous avons utulisé la bibliothéque tweepy pour la collecte de 10000 tweets pour cela nous avons faire recours à la méthode api.search.Twitter donne la permission pour l'exploitation de son API a travers l'inscription au "twitter developer" pour avoir des clés a travers lesquelles on peut accées a l'API</br>
<br>![key](https://user-images.githubusercontent.com/66451325/102282770-6677b280-3f31-11eb-98bf-b64b956108a0.jpg)</br>
<br>![Inkedkeyapi](https://user-images.githubusercontent.com/66451325/102282795-71324780-3f31-11eb-8578-87052552b009.jpg)</br>
<br>Reference :http://docs.tweepy.org/en/latest/api.html</br>
<br>Reference :http://docs.tweepy.org/en/latest/</br>
<br>Reference :http://docs.tweepy.org/en/latest/streaming_how_to.html</br>

![tweetscollect](https://user-images.githubusercontent.com/66451325/102276023-881f6c80-3f26-11eb-892e-fbc10c94aed9.gif)

# <br> Tweets cleaning</br>
 <br> Dans cette étape, l’objectif est d’éliminer le texte inutile des tweets tels que les #, les noms des
utilisateurs, les url, …</br>
 <br>pour cette etape nous avons avons definir des fonctions pour prétraitement des tweets  </br>
# <br> NLPK pour cleaning</br>
 <br> On doit procéder à l’analyse du tweet en respectant les différentes étapes du NLP (Natural
LanguageProcessing). La bibliothèque à utiliser est NLTK en Python</br>
# <br> classification des Tweets avec Kmeans</br>
<br>Etant donné un ensemble de tweets, l’objectif est de les résumer sous formes de groupes de sorte à
ce que les Tweets qui sont dans le même groupe soient similaires. Ainsi, l’utilisateur pourra par la
suite lire juste un Tweet de chaque groupe (le Tweet qui est le centroïde de groupes)</br>
<br>Clustering K-Means</br>
<br>Le clustering K-Means est un type d'algorithmes d'apprentissage non supervisé, qui crée des groupes en fonction de la distance entre les points. </br>
<br>Comment? Il existe deux concepts de distance dans le clustering K-Means.</br> 
<br>Dans les sommes des carrés en grappes (WSS) et entre les sommes des carrés en grappes (BSS).</br>
![kmeans](https://user-images.githubusercontent.com/66451325/102290626-b3638500-3f41-11eb-9796-aec4db36d542.PNG)
<br>Somme des carrés du cluster WSS signifie la somme des distances entre les points et les centroïdes correspondants pour chaque cluster et BSS signifie la somme des distances entre les centroïdes et la moyenne totale de l'échantillon multipliée par le nombre de points dans chaque cluster. Vous pouvez donc considérer WSS comme la mesure de la compacité et BSS comme la mesure de la séparation.</br>
![KMean](https://user-images.githubusercontent.com/66451325/102290622-b2325800-3f41-11eb-9aba-c6d54b3b0bb2.PNG)
<br>Pour que le clustering réussisse, nous devons obtenir le WSS inférieur et le BSS supérieur.</br>
<br>Essayez on binder : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mariem-ro/projet_data_maining/main)</br>
