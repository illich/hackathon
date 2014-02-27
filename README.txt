# Data & IoT & Computer Vision & Machine learning hackaton

----------------------------------------------------------------------------------------------------

1. Ekonomická data doplněná o počty tweetů o dané firmě

Jsou tu dva druhy souborů, ten první:

Je to .csv s řádově desítkami tisíc řádek, každá řádka odpovídá jedné minutě.
Sloupce jsou nadepsané, jejich význam je postupně:

datetime - datum a čas
close - cena v dolarech na konci dané minuty
volume - obchodovaný objem v dané minutě
tweet_count - počet tweetů o dané firmě (resp. jejím symbolu), v dané minutě
tweet_weighted_count - totéž, ale váženě, tedy účty s více followery mají větší váhu
tweet_weighted_happy - totéž, ale pouze tweety s pozitivním sentimentem
tweet_weighted_sad - a s negativním
label - label, na který se dá učit (viz níže)

----------------------------------------------------------------------------------------------------

2. Tweety

Samotné texty tweetů.
Formát je datum, label (stejný jako výše), text.

----------------------------------------------------------------------------------------------------

3. Ukázkový problém

label je to co chcete učit.
Jeden label jsme vám do dat už předpočítali a to takto:
- pokud cena akcie v následujících minutách vyroste aspoň o 10 centů, je tam +0.10
- pokud cena akcie v následujících minutách klesne aspoň o 10 centů, je tam -0.10
  (počítá se vždy to první, co nastane)
- pokud cena v následujících 10 minutách ani tolik neporoste ani neklesne, dáváme tam rozdíl cen
  za těchto 10 minut
  
Můžete zkusit nějaký algoritmus naučit na těchto labelech.

Nebo si určete jiný label - chcete-li třeba akcii držet hodinu, tak si obdobným způsobem spočtete label
jako rozdíl ceny za hodinu a současné ceny.

----------------------------------------------------------------------------------------------------

4. Výsledek algoritmu a hodnocení

Pro každý čas se jakýmkoliv způsobem rozhodněte mezi BUY a WAIT.
BUY = koupím jednu akcii a prodám ji podle stejné strategie, jako je vypočtený label
WAIT = nic nedělám

Pro rozhodnutí můžete použít cokoliv kromě labelu samotného.
Respektive "cokoliv" =
- všechna data (kromě labelu) ze současného času a celé minulosti
- jakýkoliv algoritmus, který je zpracuje

Ohodnotit svůj algoritmus můžete jednoduše: sečtěte labely u všech řádek, kde jste se rozhodli pro BUY.
To je váš hrubý zisk.

Pokud chcete být důkladnější:
- tak od hrubého zisku odečtěte 1 cent za každý obchod (nákup, prodej), tím získáte přibližně čistý zisk.
- dejte si pozor, abyste nikdy nedrželi víc než jednu akcii najednou - tedy např. dávejte BUY jen jednou za 10 minut

Pokud je váš algoritmus dobrý, měl by vydělat víc, než "buy-and-hold", tedy postup, kdy akcii koupíte
na úplném začátku období a prodáte na úplném konci.

----------------------------------------------------------------------------------------------------

5. Trénovací a testovací data

Soubory jsme vám rozdělili na dvě části:
- prvních 80 % je trénovací část
- posledních 20 % je testovací část

Na trénovací části provádíte veškerý vývoj - zkoumáte data, volíte algoritmus, ladíte jeho parametry.
V ideálním světe byste měli pustit váš algoritmus NA TESTOVACÍCH DATECH JEN JEDINKRÁT ZA HACKATHON.

Asi vám to nedá a když budete mít víc algoritmů, tak si je nejspíš na testovacích datech zkusíte pustit
každý. Jen vězte že je to lehké švindlování a že pak nemůžete dělat žádné závěry o tom, jak se bude
algoritmus chovat v reálu. (je to jako kdybyste 10x hodili kostkou, vzali maximum a pak tvrdili, že umíte
házet šestky).

					    Hodně štěstí!

