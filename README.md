# Prova tècnica per a 21 buttons

Web crawling basic by Vladimir Remar

## Objectiu:

L'Objectiu d'aquesta prova tècnica consisteix a extreure la informació 
de les pàgines de producte de dues pàgines webs de moda: Naturalylila i 
Goiclothing

## Instruccions

- S'ha de crear un programa en Python que rebi com a entrada un URL i
generi com a sortida una cadena en JSON que contingui almenys les
següents claus:

    - name: nom del producte
    - price: preu del producte
    - image_urls: urls de les diferents imatges del producte
    - description: descripció del producte

- El input puede ser cualquier página de producto tanto de Naturalylila como de
Goiclothing.
- Se puede utilizar Python 2 o Python 3
- Se puede utilizar cualquier librería necesaria
- El tiempo estimado para realizar la prueba técnica es entre 6 - 8 horas
- Una vez finalizada se subir el código a cualquier repositorio público (Github, Gitlab,
Bitbucket,...)
- Se valorará la estructura, claridad y buenas prácticas empleadas en el código.

## Desenvolupament

Prenent com a base el [tutorial](https://doc.scrapy.org/en/latest/intro/tutorial.html) de scrapy,
vaig desenvolupar amb *python 2* un petit [script](https://github.com/vladimir-remar/proba21buttons/blob/master/Vladimir_scripts/vladimir-test.py),
amb el qual poder extreure informació d'un producte.



## Planing 

| Estructuració                           | Temps empreat  
| --------------------------------------  |:-------------:|
| Seguiment Tutorial                      | 2h            |
| Plantejament i test  extens amb scrapy  | 2h            |
| Coding                                  | 2:30h         |
| Debugging                               | 30min         |
| Resultats                               | --            |


## Execució

### Amb un producte d'alguna de les pàgines web

    python vladimir-test.py -l https://naturalbylila.com/producto/bolso-malaga/

### Per obtenir diversos resultats amb un [script](https://github.com/vladimir-remar/proba21buttons/blob/master/Vladimir_scripts/tests.sh) de bash
    
    bash tests.sh
    
### Sortida

La sortida generada és un fitxer .json amb la resposta de totes les consultes
En el meu cas [sortida](https://github.com/vladimir-remar/proba21buttons/blob/master/Vladimir_scripts/result.json)
## Extres

Com a extra he deixat els 2 projectes i els seus respectius resultats

## Conclusions

Expect the Unexpected, ha estat força revelador com poder tractar les 
dades d'una pàgina web més enllà de veure el propi contingut. L'eina 
*scrapy* ha estat com obrir un nou horitzó. La meva curta experiència 
amb ella, més enllà de picar codi ha estat de complet enriquiment.

Puc dir que la meva aventurra amb *scrapy* acaba de començar.

## Referències

[Scrapy Docs](https://doc.scrapy.org/en/latest/index.html)
