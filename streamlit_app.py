import streamlit as st
import pandas as pd
import io
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Data Loading and Cleaning (same as before)
data = """piadina
poadina
giovanni_rossi
gzkzof
pancake
pasta
melanzane
melanzana
piselli
legumi
colazione
cola
colazione
porrige
curry
farro
orzo
asparagi
dolci
vellutata
riso
funghi
peperoni
pepe
pomodori secchi
crostini
pankake
lwalca
mchjco
mrfgbj
akqdlr
hnujcw
Pasta
ezpqth
gzposn
ygugkw
dycnxx
pasta con ricotta
uovo
quinoa
zucchine
yogurt
pommodorini
pasta zucchine
cefi
 zucchine
gbetetti
gorgonzola
gamberettu
tofu
pasta con zucchine
seitan
risotto
feta
ricette veloci
robiola
fagiolini
zucca
ricette con zucchine
pesce
rucola
salmone
pane melanzane
manzo
verza
gnochi
gnocchi
ceci
sgombro
spada
piadina l
piadina
bvhnuj
ongzpo
sfjjqs
vxjwzt
sxgtow
fflqxn
hyqflu
pasta e tonno
cous cous melanzane tonno
panino prosciutto crudo
cous cous melanzane
spaghetti
cavolfiore
paccheri
formaggio
ricotta
polpette di ceci
petto di pollo
frittata
gam
za
zafferano
pollo
mozzarella
lenticchie
tonno
pollo
zuppa di broccoli
 lenticchie
zucchine lenticchie
orata
eomsdv
secondi piatti
primosale
uova
pollo allo zafferano
carne
polpette
falafel
vellutata zucca
bresaola
pquvwt
panino
pane
panino di pollo
pa
tonno
ricette con tonno
broccoli
tacchino
petto di tacchino
pere cacao
pere cacak
cavolo nero
", ricotta, pasta "
"zucchine, ricotta, pancetta "
 zucchine pancetta
finocchi
merluzzo
zucca cavolo nero
cavolo
radicchio
bkfvvp
gqyodh
ztsymr
orzo
orzo insalata
wfsdts
vitello
branzino
gamberetti
hamburger
cous cous
zuppa di cavolo nero e lenticchie
frullato
smoothie
hummus
piada
ci
schiscette
gamberetti pane
gnocchi
grano saraceno
grano saracen
pollo alla piastra
uova in purgatorio
fetA
uov
po
carne ross
burger vegetali
merenda
muffin
io
tofy
cous coua
gamber
carciofi
insalata
uova e zucchine
polpette vitello
spinaci
avocado
spigola
burger
porridge
fodmap
pasta alla boscaiola
colazioni
skyr
pudding
coniglio
patate
risotto
ravioli
ricotta e spinaci
i totani
calamari totani
calamari
fagioli
sedano
bresaola
philadephia
philadelphia
gdxsol
bsmoyj
pollo al curry
gamberetti
tonno fresco
maiale
arista
fri
pesce spada
piadina integrale
lonza
ricette salutari
pancke
avena
gamberi
uova purgatorio
cannellini
primi
pollo con verdure
banana
dolce
polenta
pasa
riso gamberetti e zucchine
fiocchi
pancake
vellutata zucchine
polpette limone
pollo curry
fiocchi D'Avena
chetogenica
salmonr
e
farro e lenticchie
cavolo nero
lenticchie farro
cavolo nero spinaci
cous
crackers
cracker
orso
pasta con pesce
pasta
pollo fungji
pollo funghi
pollo all'arancia
cous cous
cci
salmone affumicato
salmone
pollo spinaci
uova pomodoro
pizza
tofu quinoa
vongole
patate cetrioli
sogliola
orat
broccoli lessi
riso con verdure
bistecca vitello
cous cous verdire
piselli e funghi
couscous
pasta pomodoro e parmigiano
pollo al radicchio
patate
parmigiana
tempeh
fiocchi di latte
crepes
fusilli
rombo
tortellini
piafina
sesamo
spuntini dolci
calamaro
seppie
pesto
carne rossa
fiocchi
uova zucchine
porrige con fragole
pasta con funghi
pasta con fumghi
melanzane
succa
vellutata con piselli
porridje
porri
pasta e piselli
pasta con i piselli
cavolfiore
gallette
zuppa
pollo al limone
filetto di manzo
melanzana
macinato
passato di verdure
pesce spada
funghi zucca
pane
frittata
frittata porro
frittata porri
uova
polo
albume
pesche
mel
zucchine uova
quinoa e ceci
merluzzo
albumi
lenticchie
piadina ricotta
fubghi
fagio
minestrone
Orzo
miglio
finocchio
pollo con verdure
pollo con verdire
poke
coscia
petto di pollo all'arancia
vellutata di zucca
insalata
cotto
tonno e zucchine
speck
salmone e spinaci
pruscito cotto
sushi
cubetti di cotto
riso e legumi
carne
polpo
uova e peperoni
uova e peperoni ricette
zucca
torta cannolo
cous cou
cannolo
cous cois
curcuma
Uova all'occhio con patate croccanti
pasta e zucchine
pesce al forno
pasta veloce
ahjsdadsgjghasd
trota
asadsasd
adshdjs
\"am,sdhjasd\"
Vitello
Pollo
adshdjsòalsjdjakdsjklasdjksla
petto si pollo
riso venere
melenzane
melenzana
riso e formaggio fresco
hummus
caprese
uova con patate
platess
pizza
pizza di uova
pizza frittata
mela
vitellone
metluzzo
tem
merluzo
seita
frutti di bosco
tocchetti di pollo
pasta con salmone
pasta e robiola
riso e pollo
riso zucchine
pasta e merluzzo
formaggio
pasta philadelphia
pasta ricotta
secondi
pasta con verdure
tacchino funghi
tacchino
tacchino verdure
tacchino finghi
uova pasta
frutta
cat
Uova in camicia con pomodori arrosto e basilico e pane croccante
riso con fagioli
yogurt greco e fritti di bosco
tiramisu
yogurt greco e frutti di bosco
pollo al curry
merluzzo impanato
pesce bianco
calamari
lenticchie e zucchine
piadine
mozzarelline
mozzarella di mucca
mozzarellla
gnocchi di patate
mozzarella di vacca
riso con zucca
polli
petto di pollo e verdure
ricetta uova
ricetta piadina
piadina
ricetta piadina integrale
pollo e patate
parate
gamberi
risotto zucchine e salmone
risotto con zucchine e salmone
pollo al radicchio
uova in purgtorio
cus cus
tofu e avocado
pankace
verdure
zucchine e ricotta
calamarata
bacca
chia
vellitata finocchio
vellutata finocchi
vellutata finocchio
vellitata
vellutata piselli
pollo con zucchine
pollo zucchine
pollo e zucchine
carote e piselli
carbonara
upva
riso gamberetti
farro con rucola tofu
fagioli
spatz
branzino
ta
patate americane
patata
spuntini
soia
pollo soia
zuppa zucchine e ceci
pollo con soai
pollo con so
prim
pasta di legumi
pepe rosa
lentcchiei
lenticchie
riso integrale
pasta con pesce spada
patate e piselli
zuppa
reminder
finocchi
spaghetti
panna
banane
kiwi
pasta e pollo
farto
vitella
pasta e verdure
gambe
cous
polo al curry
Gamberetti
soesa
stracchino
risoni con piselli
risoni
pollo arancia
banana bread
spezzatino carne e patate
spezzatino di manzo e patate
pak
pak choi
carote
frittata di piselli
spezzatino di maiale e patate
spezzatino di maiale con patate
ricette con petto di pollo
brownis
bocconcini di pollo
pasta con legumi
pesce e pane e verdure
pesce pane  verdure
pesce e pane
polipo
pasra
bphzzn
straccetti
straccetti di pollo
bocconcini di pollo
cous cous mozzarella e pomodorini
nasello
primo sale
straccetti di pollo
peperoni
fiori di zucca
verzw
lenticchie
cokaziini
scamorza
spigolq
salsa di soua
riso alla cantonese
salsa di soia
pollo e cavolfiore
pollo e xavolfiore
torta salata
acqua
pasta con macinato
broccoletti
pasta e zucca
ragu di pesce
Riso
piastra
pizza fri
lasagna
pasta con robiola
cuscus
omelette
uovo strapazzato
bowl
carlotta italiano
gnocchi patate
pollo alla pizza
lentichie
cavolo rosso
ragù
overnight porridge
spigola broccolo
spigola
orata
cavolfiore polpette
melanzane e pomodorini
spaghetti con crema di melanzane e pomodorini
spaghetti melanzane e pomodorini
spiedini di po
farinata
albume
lenticchir
lenticchie umido
passata
porro
linguine
fave
pollo fungh
pollo funghi zafferano
pollo con i funghi
zuppe
riso e lenticchie
zuppa zucchine
trippa
insalatone
peperonata
insalate
polpette
prosciutto
vellutata di fio
vellutata di
vellutata difi
vellutata di finocchi
minestra di zucchine
vellutata di fi
zucchina
minestra
vellutata di finocchio
salmonns
di
salmonne
riso con gamberetti
vellutata di zucchine
pasta di ceci
grana
grqna
polpette ricotta
zucchine grigliate
bocconcini
vellutat
bocconcinni
bocconcinii
scaloppine
Riso
agombro
farina di ceci
sfoglia
forno
pasta sfoglia
riso ceci
finocchi arancio
piadine di legumi
cipolla
carne di vitello
fettine di pollo
polpette finocchi
fettine di vitella
ragù
pomodoro
straccetti di vitelo
straccetti di vitello
orzo con tonno
farro e gamberetti
riso con pollo e funghi
cocco
\"uova, salmone verdura\"
sarde
alici pasta
alici
pasta funghi
crema funghi
funghi pasta
uova menta
fusilloni
lin
farro con rucola
soiola
fiocchi d'avena
yogurt
fette biscottate
cuscus ceci
risogamberetti
platessa
uova con patate croccanti
topinanbur
torta di mele
mais
waffle
croccole
\"pasta, uova, verdure\"
carbonara vegetariana
polpette branzino
polpette pesce
polpette merluzzo
pasta ceci
quinoa prosciutto
quinoa cotto
piadina avocado
avocado
ragù di tofu
zucchin
legu
legumi
ceci tostati
cavolo romanesco
cavolo
cavolo ro
cavolo romano
broccolo
cinnamon rolls
cous cous con mozzarella
cous cous con pomodori
bulgur
"""

df = pd.read_csv(io.StringIO(data), header=None, names=['query'])

# Lowercase and strip whitespace
df['cleaned_query'] = df['query'].str.lower().str.strip()

# Correct typos
df['cleaned_query'] = df['cleaned_query'].replace({'poadina': 'piadina', 'pankake': 'pancake', 'pommodorini': 'pomodorini', 'gamberettu': 'gamberetto', 'gnochi': 'gnocchi'})
df['cleaned_query'] = df['cleaned_query'].replace({'cavolfiore':'cavolo fiore', 'fubghi':'funghi', 'melenzane':'melanzane', 'metluzzo':'merluzzo','merluzo':'merluzzo', 'spigolq':'spigola', 'lentcchie':'lenticchie', 'lentcchiei':'lenticchie', 'pruscito cotto':'prosciutto cotto'})
df['cleaned_query'] = df['cleaned_query'].replace({'legu':'legumi'})

# Remove nonsense queries (very aggressive)
df = df[~df['cleaned_query'].str.contains(r'^[a-z0-9]{5,}$', regex=True)]  # Remove 5+ char alphanumeric strings

#Remove queries that look like memory addresses
df = df[~df['cleaned_query'].str.contains(r'0x[a-f0-9]+', regex=True)]

def categorize_query(query):
    if 'pasta' in query or 'spaghetti' in query or 'paccheri' in query or 'fusilli' in query or 'tortellini' in query or 'linguine' in query or 'calamarata' in query or 'risoni' in query:
        return 'Pasta Dishes'
    elif 'riso' in query or 'risotto' in query:
        return 'Rice Dishes'
    elif 'piadina' in query or 'pizza' in query or 'focaccia' in query:
        return 'Bread/Baked Goods'
    elif 'pollo' in query or 'tacchino' in query or 'carne' in query or 'pesce' in query or 'salmone' in query or 'tonno' in query or 'sgombro' in query or 'merluzzo' in query or 'vitello' in query or 'maiale' in query or 'manzo' in query or 'polpo' in query or 'prosciutto' in query or 'bresaola' in query:
        return 'Protein Sources'
    elif 'zucchine' in query or 'melanzane' in query or 'zucca' in query or 'cavolo' in query or 'broccoli' in query or 'piselli' in query or 'peperoni' in query or 'carote' in query or 'finocchi' in query or 'spinaci' in query or 'funghi' in query or 'patate' in query or 'lenticchie' in query or 'ceci' in query or 'fagioli' in query or 'asparagi' in query or 'sedano' in query or 'porri' in query or 'radicchio' in query or 'avocado' in query or 'pepe' in query:
        return 'Vegetables/Legumes'
    elif 'uovo' in query or 'uova' in query:
        return 'Eggs'
    elif 'formaggio' in query or 'ricotta' in query or 'yogurt' in query or 'latte' in query or 'panna' in query or 'mozzarella' in query or 'grana' in query or 'stracchino' in query or 'philadelphia' in query or 'scamorza' in query or 'feta' in query or 'robiola' in query or 'primo sale' in query:
        return 'Dairy Products'
    elif 'vellutata' in query or 'zuppa' in query or 'minestra' in query:
        return 'Soups/Creams'
    elif 'dolci' in query or 'pancake' in query or 'torta' in query or 'muffin' in query or 'pudding' in query or 'tiramisu' in query or 'cinnamon rolls' in query or 'waffle' in query or 'brownis' in query or 'banana bread' in query or 'crepes' in query:
        return 'Desserts'
    elif 'colazione' in query or 'porridge' in query or 'fiocchi' in query or 'skyr' in query or 'merenda' in query or 'fette biscottate' in query:
        return 'Breakfast/Snacks'
    elif 'insalata' in query or 'cous cous' in query or 'quinoa' in query or 'farro' in query or 'bulgur' in query or 'orzo' in query:
        return 'Salads/Grains'
    elif 'hamburger' in query or 'polpette' in query or 'frittata' in query or 'omelette' in query or 'spezzatino' in query or 'straccetti' in query or 'bocconcini' in query:
        return 'Meat Dishes'
    elif 'curry' in query:
        return 'Curry Dishes'
    elif 'salsa' in query or 'pesto' in query or 'ragù' in query:
        return 'Sauces'
    elif 'pane' in query or 'crostini' in query or 'gallette' in query or 'crackers' in query:
        return 'Bread/Crackers'
    elif 'frullato' in query or 'smoothie' in query:
        return 'Beverages'
    elif 'ricette' in query:
        return 'Recipes'
    elif 'spuntini' in query:
        return 'Snacks'
    elif 'pomodori secchi' in query or 'rucola' in query or 'verza' in query or 'zafferano' in query or 'tofu' in query or 'seitan' in query or 'falafel' in query:
        return 'Specific Ingredients'
    elif 'secondi piatti' in query:
        return 'Italian Cuisine'
    elif 'cola' in query:
      return 'Beverages'
    elif 'platessa' in query or 'sogliola' in query or 'trota' in query or 'nasello' in query or 'calamaro' in query or  'vongole' in query or 'seppie' in query or 'bacca' in query or 'spigola' in query or 'orata' in query:
        return 'Fish/Seafood'
    elif 'passato di verdure' in query or 'albume' in query or 'soia' in query:
        return 'Ingredients'
    elif 'pere cacao' in query or 'pere cacak' in query or 'mela' in query or 'kiwi' in query or 'frutti di bosco' in query:
        return "Fruits"
    elif 'uovo strapazzato' in query or 'carbonara vegetariana' in query or 'poke' in query or 'bowl' in query:
        return "Dishes"
    elif 'grano saraceno' in query or 'grano saracen' in query or 'mais' in query:
        return 'Grains'
    elif 'cubetti di cotto' in query or 'fettine di vitella' in query or 'spiedini di po' in query or 'piadine di legumi' in query or 'fave' in query:
        return 'Prepared Ingredients'
    elif 'pak choi' in query:
        return 'Vegetables/Legumes'

    else:
        return 'Uncategorized'

df['category'] = df['cleaned_query'].apply(categorize_query)

#Remove queries with length less than 3 that are uncategorized
df = df[~((df['category'] == 'Uncategorized') & (df['cleaned_query'].str.len() < 3))]

query_counts = df['cleaned_query'].value_counts().sort_values(ascending=False)

#Filter out general queries for the word cloud
query_counts_filtered = query_counts[query_counts.index.str.split().str.len() > 1]

# Streamlit App
st.title("Analisi Query di Ricerca Utenti")

st.subheader("Distribuzione Categorie")
category_counts = df['category'].value_counts().sort_values(ascending=False)
fig_categories = px.bar(x=list(category_counts.index), y=list(category_counts.values), labels={'x': 'Categoria', 'y': 'Frequenza'})
st.plotly_chart(fig_categories)

# Most Searched Queries (Improved)
st.subheader("Query di Ricerca Più Frequenti")
num_queries = st.slider("Numero di Query da Visualizzare", min_value=5, max_value=30, value=15)

fig_queries = px.bar(x=query_counts.index[:num_queries], y=query_counts.values[:num_queries], labels={'x': 'Query', 'y': 'Frequenza'})
st.plotly_chart(fig_queries)

# Word Cloud
st.subheader("Word Cloud delle Query di Ricerca (Escluse Query Generiche)")
text = " ".join(query_counts_filtered.index)
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)

st.subheader("Tabella Dati Grezzi")
st.dataframe(df)

st.subheader("Key findings 🔍")
st.write("""
*   Gli utenti cercano spesso piatti italiani (pasta, piadina, risotto) e ingredienti salutari (lenticchie, verdura)
*   **Pollo e gamberi** sono tra le fonti di proteine più cercate
*   Le query sono generalmente concentrate su ingredienti singoli e semplici, il che ci fa pensare che cerchino idee di ricette per pasti veloci e facili
""")

st.subheader("Proposte miglioramenti 💪")
st.write("""
*   Suggerimenti di ricerca
*   Aggiunta analytics su risultati della ricerca e effettiva rilevanza dei risultati (per ora non abbiamo alcuna informazione a riguardo)
*   Sviluppare Contenuti: Creare nuovi contenuti focalizzati su:
    *   Ricette vegetariane/vegane
    *   Piatti a base di pollo e gamberetti
    *   Utilizzo creativo di verdure e legumi
*   Ottimizzare Suggerimenti: Utilizzare la cronologia di ricerca degli utenti per offrire suggerimenti di ricette e ingredienti pertinenti.
*   Implementare Filtri: Aggiungere filtri di ricerca per consentire agli utenti di specificare preferenze dietetiche (es. senza glutine, vegetariano, a basso contenuto di carboidrati).
""")

st.subheader("Ongoing 👷🏻🚧🏗️")
st.write("""
1.  Query analysis - Data pipeline setup (Raccolta query separate per ambiente)
2.  Query suggestions
3.  Add data ingestion for clicks on search results - (analisi performance search)
4.  Search results ordering and ranking
""")
