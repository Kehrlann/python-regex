# python-regex

## Consignes générales

Les expressions régulières... en Python!

Vous allez faire 4 exercices. Pour le rendu, remplissez **uniquement les fonctions** dans les fichiers désignés, veillez bien à n'ajouter aucun autre code dans ces fichiers. Évaluez votre note en local de temps en temps (cf ci-dessous).

Pendant que vous préparez vos exercices, pouvez tester vos fonctions en utilisant la construction
`if __name__ == "__main__":`


```python
def toto(un, deux, trois):
  # votre code
  # ...

if __name__ == "__main__":
  resultat = toto("un", 2, three)
  print(resultat)
```

Nota bene:

- nous nous concentrons sur l'écriture de l'expression régulière en elle-même, et pas sur l'utilisation de la bibliothèque;
- en particulier, tous les exercices font appel à re.match entre votre regexp et une liste de chaînes d'entrée qui servent de jeux de test.


## Rendre votre travail

Quand le résultat pour un des exercices est satisfaisant, git add, git commit, git push:

```shell
$ git add phythonid.py
$ # ajoutez aussi tout autre fichier que vous voulez committer
$ git commit --message "Python ID"
$ git push
```

Rendus **obligatoires**:

- `pythonid`
- `agenda`
- `phone`

Rendus facultatifs:

- `url`

## Évaluer votre note en local

Vous pouvez évaluer votre note en local, avec:

```shell
$ python grader.py
```

Si les tests ne finissent jamais, appuyez sur `Ctrl + C` pour interrompre.


## Exercice - `pythonid`

On vous demande d'écrire une expression régulière qui décrit les noms de variable en Python. Pour cet exercice on se concentre sur les caractères ASCII. On exclut donc les noms de variables qui pourraient contenir des caractères exotiques comme les caractères accentués ou autres lettres grecques.

Il s'agit donc de reconnaître toutes les chaînes qui commencent par une lettre ou un `_`, suivi de lettres, chiffres ou `_`.

Quelques exemples:
- 'a'
- '_'
- '__'
- 'aa1'
- 'A1a'

Quelques exemples qui ne sont pas des identifiants python:
- '-'
- '1Aa'
- '-aa1'


## Exercice - `agenda`

On veut reconnaître dans un fichier toutes les lignes qui contiennent un nom et un prénom.

Plus précisément, on cherche les chaînes qui :

* commencent par une suite - possiblement vide - de caractères alphanumériques (vous pouvez utiliser `\w`) ou tiret haut (`-`) qui constitue le prénom ;
* contiennent ensuite comme séparateur le caractère 'deux-points' `:` ;
* contiennent ensuite une suite - cette fois jamais vide - de caractères alphanumériques ou tiret haut, qui constitue le nom ;
* et enfin contiennent un deuxième caractère `:` mais optionnellement seulement.

On vous demande de construire une expression régulière qui définit les deux groupes `nom` et `prenom`, et qui rejette les lignes qui ne satisfont pas ces critères.

Dans la correction - et ce sera pareil pour tous les exercices de regexp où on demande des groupes - la correction affiche **uniquement les groupes demandés**; ici on va vous montrer les groupes `nom` et `prenom`; vous avez parfaitement le droit d'utiliser des groupes supplémentaires, nommés ou pas d'ailleurs, dans votre propre regexp.


| chaîne                      | groupes                                               |
|-----------------------------|-------------------------------------------------------|
| 'Daniel:Durand'             | [('nom', 'Durand'), ('prenom', 'Daniel')]             |
| 'Jean:Dupont:'              | [('nom', 'Dupont'), ('prenom', 'Jean')]               |
| 'Jean:Dupont::'             | None                                                  |
| ':Dupontel:'                | [('nom', 'Dupontel'), ('prenom', '')]                 |
| 'Jean-Noël:Dupont-Nemours'  | [('nom', 'Dupont-Nemours'), ('prenom', 'Jean-Noël')]  |
| 'Charles-Henri:Du Pré'      | None                                                  |
| 'Charles Henri:DuPré'       | None                                                  |


En guise d'indice, je vous invite à regarder les fonctions *built-in* [`sum`](https://docs.python.org/3/library/functions.html#sum), [`min`](https://docs.python.org/3/library/functions.html#min) et [`max`](https://docs.python.org/3/library/functions.html#max).


## Exercice - `phone`

Cette fois on veut reconnaître des numéros de téléphone français, qui peuvent être :

* soit au format contenant 10 chiffres dont le premier est un `0` ;
* soit un format international commençant par `+33` suivie de 9 chiffres.

Dans tous les cas on veut trouver dans le groupe `number` les 9 chiffres vraiment significatifs, comme ceci :

| chaîne          | groupes                   |
|-----------------|---------------------------|
| '0123456789'    | [('number', '123456789')] |
| '01234567890'   | None                      |
| '012345678'     | None                      |
| '1234567890'    | None                      |
| '+33123456789'  | [('number', '123456789')] |
| '+3312345678'   | None                      |
| '+330123456789' | None                      |


## Exercice - `url`

Vu comment sont conçus les exercices, vous ne pouvez pas passer à `re.compile` un drapeau comme `re.IGNORECASE` ou autre ; sachez cependant que vous pouvez ***embarquer* ces drapeaux dans la *regexp*** elle-même ; par exemple pour rendre la regexp insensible à la casse de caractères, au lieu d'appeler `re.compile` avec le flag `re.I`, vous pouvez utiliser `(?i)` comme ceci :

```python
>>> import re
>>> # on peut embarquer les flags comme IGNORECASE
>>> # directement dans la regexp
>>> # c'est équivalent de faire ceci
>>> re_obj = re.compile("abc", flags=re.IGNORECASE)
>>> re_obj.match("ABC").group(0)
'ABC'
>>> # ou cela
>>> re.match("(?i)abc","ABC").group(0)
'ABC'
>>> # les flags comme (?i) doivent apparaître
>>> # en premier dans la regexp
>>> re.match("abc(?i)","ABC").group(0)
<stdin>:1: DeprecationWarning: Flags not at the start of the expression 'abc(?i)' but at position 3
'ABC'
```

Pour plus de précisions sur ce trait, que nous avons laissé de côté dans le complément pour ne pas trop l'alourdir, voyez [la documentation sur les expressions régulières](https://docs.python.org/3/library/re.html#regular-expression-syntax) et cherchez la première occurrence de `iLmsux`.


### Décortiquer une URL

On vous demande d'écrire une expression régulière qui permette d'analyser des URLs.

Voici les conventions que nous avons adoptées pour l'exercice :

* la chaîne contient les parties suivantes :
  * `<protocol>://<location>/<path>` ;
* l'URL commence par le nom d'un protocole qui doit être parmi `http`, `https`, `ftp`, `ssh` ;
* le nom du protocole peut contenir de manière indifférente des minuscules ou des majuscules ;
* ensuite doit venir la séquence `://` ;
* ensuite on va trouver une chaîne `<location>` qui contient :
  * potentiellement un nom d'utilisateur, et s'il est présent, potentiellement un mot de passe ;
  * obligatoirement un nom de `hostname` ;
  * potentiellement un numéro de port ;
* lorsque les 4 parties sont présentes dans `<location>`, cela se présente comme ceci :
  * `<location> = <user>:<password>@<hostname>:<port>` ;
* si l'on note entre crochets les parties optionnelles, cela donne :
  * `<location> = [<user>[:<password>]@]<hostname>[:<port>]` ;
* le champ `<user>` ne peut contenir que des caractères alphanumériques ; si le `@` est présent le champ `<user>` ne peut pas être vide ;
* le champ `<password>` peut contenir tout sauf un `:` et de même, si le `:` est présent le champ `<password>` ne peut pas être vide ;
* le champ `<hostname>` peut contenir une suite non-vide de caractères alphanumériques, underscores, ou `.` ;
* le champ `<port>` ne contient que des chiffres, et il est non vide si le `:` est spécifié ;
* le champ `<path>` peut être vide.

Enfin, vous devez définir les groupes `proto`, `user`, `password`, `hostname`, `port` et `path` qui sont utilisés pour vérifier votre résultat. Dans la case `Résultat attendu`, vous trouverez soit `None` si la regexp ne filtre pas l'intégralité de l'entrée, ou bien une liste ordonnée de tuples qui donnent la valeur de ces groupes ; vous n'avez rien à faire pour construire ces tuples, c'est l'exercice qui s'en occupe.


| chaîne                                    | groupe |
|-------------------------------------------|--------|
| 'http://www.google.com/a/b'               | [ ('proto', 'http'), ('user', None), ('password', None), ( 'hostname', 'www.google.com'), ('port', None), ('path', 'a/b')] |
| 'HttPS://www.google.com:8080/a/b'         | [ ('proto', 'HttPS'), ('user', None), ('password', None), ( 'hostname', 'www.google.com'), ('port', '8080'), ('path', 'a/b')] |
| 'http://user@www.google.com/a/b'          | [ ('proto', 'http'), ('user', 'user'), ('password', None), ( 'hostname', 'www.google.com'), ('port', None), ('path', 'a/b')] |
| 'FTP://username:hispass@www.google.com/'  | [ ('proto', 'FTP'), ('user', 'username'), ('password', 'hispass'), ( 'hostname', 'www.google.com'), ('port', None), ('path', '')] |
| 'ssh://missing.ending.slash'              | None |
| 'gopher://unsupported.proto.col/'         | None |
| 'http:///missing/hostname/'               | None |
| 'http://:toto@www'                        | None |
| 'ftp://www:1:2/a/'                        | None |
