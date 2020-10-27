import codecademylib3_seaborn
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from term_frequency import bow_matrix, feature_names, df_bag_of_words, corpus_index

# display term-document matrix of term frequencies (bag-of-words)
# conferir no final
print(df_bag_of_words)



# initialize and fit TfidfTransformer, transform bag-of-words matrix
transformer = TfidfTransformer(norm=None)
tfidf_scores = transformer.fit_transform(bow_matrix)

# create pandas DataFrame with tf-idf scores
try:
  df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index = feature_names, columns=corpus_index)
  print(df_tf_idf)
except:
  pass


"""
Poem 1	Poem 2	Poem 3	Poem 4	Poem 5	Poem 6
abash	0	0	0	0	1	0
across	0	0	0	1	0	0
admire	0	0	1	0	0	0
again	0	0	0	1	0	0
agonize	1	0	0	0	0	0
ah	0	1	0	0	0	0
all	1	0	0	2	1	0
an	0	0	1	1	0	0
and	1	0	0	8	5	0
any	0	0	0	0	0	1
aristocracy	0	0	0	0	0	1
ask	0	0	0	0	1	0
at	0	0	0	0	1	0
banish	0	0	1	0	0	0
be	1	2	3	5	3	1
beat	0	0	0	2	0	0
bee	0	0	0	0	0	1
begin	0	0	0	1	0	0
bell	0	0	0	1	0	0
bird	0	0	0	0	1	0
bog	0	0	1	0	0	0
boot	0	0	0	1	0	0
box	0	0	0	1	0	0
brain	0	0	0	1	0	0
break	1	0	0	1	0	0
but	0	1	0	1	0	0
by	1	0	0	0	0	0
can	1	0	0	0	0	0
chart	0	1	0	0	0	0
chillest	0	0	0	0	1	0
clear	2	0	0	0	0	0
clover	0	0	0	0	0	1
compass	0	1	0	0	0	0
comprehend	1	0	0	0	0	0
concern	0	0	0	0	0	1
could	0	0	0	0	1	0
count	1	0	0	0	0	0
creak	0	0	0	1	0	0
crumb	0	0	0	0	1	0
day	1	0	1	0	0	0
defeat	1	0	0	0	0	0
definition	1	0	0	0	0	0
die	1	0	0	0	0	0
distant	1	0	0	0	0	0
do	0	2	0	0	0	1
don	0	0	1	0	0	0
dreary	0	0	1	0	0	0
drum	0	0	0	1	0	0
ear	1	0	0	1	0	0
eden	0	1	0	0	0	0
er	1	0	0	0	0	0
extremity	0	0	0	0	1	0
feather	0	0	0	0	1	0
felt	0	0	0	1	0	0
flag	1	0	0	0	0	0
forbid	1	0	0	0	0	0
fro	0	0	0	1	0	0
frog	0	0	1	0	0	0
funeral	0	0	0	1	0	0
futile	0	1	0	0	0	0
gale	0	0	0	0	1	0
go	0	0	0	1	0	0
he	1	0	0	0	0	0
hear	0	0	0	1	2	0
heart	0	1	0	0	0	0
heaven	0	0	0	1	0	0
here	0	0	0	1	0	0
him	0	0	0	0	0	1
honey	0	0	0	0	0	1
hope	0	0	0	0	1	0
host	1	0	0	0	0	0
how	0	0	2	0	0	0
in	0	3	0	1	4	0
it	0	0	0	1	2	0
keep	0	0	0	2	1	0
know	0	0	1	0	0	0
land	0	0	0	0	1	0
lead	0	0	0	1	0	0
lift	0	0	0	1	0	0
like	0	0	1	1	0	0
little	0	0	0	0	1	0
livelong	0	0	1	0	0	0
luxury	0	1	0	0	0	0
many	0	0	0	0	1	0
me	0	0	0	0	1	0
might	0	1	0	0	0	0
mind	0	0	0	1	0	0
moor	0	1	0	0	0	0
mourner	0	0	0	1	0	0
must	0	0	0	0	1	0
my	0	0	0	3	0	0
name	0	0	1	0	0	0
ne	1	0	0	0	0	0
nectar	1	0	0	0	0	0
need	1	0	0	0	0	0
never	0	0	0	0	2	0
night	0	4	0	0	0	0
nobody	0	0	2	0	0	0
not	1	0	0	0	0	1
numb	0	0	0	1	0	0
of	3	0	1	1	1	1
on	1	0	0	0	1	0
one	1	0	0	0	0	0
our	0	1	0	0	0	0
pair	0	0	1	0	0	0
pedigree	0	0	0	0	0	1
perch	0	0	0	0	1	0
port	0	1	0	0	0	0
public	0	0	1	0	0	0
purple	1	0	0	0	0	0
race	0	0	0	1	0	0
require	1	0	0	0	0	0
rowing	0	1	0	0	0	0
same	0	0	0	1	0	0
sea	0	1	0	0	1	0
seat	0	0	0	1	0	0
seem	0	0	0	1	0	0
sense	0	0	0	1	0	0
service	0	0	0	1	0	0
should	0	1	0	0	0	0
silence	0	0	0	1	0	0
sing	0	0	0	0	1	0
so	1	0	0	0	1	0
solitary	0	0	0	1	0	0
some	0	0	0	1	0	0
somebody	0	0	1	0	0	0
sore	0	0	0	0	1	0
sorest	1	0	0	0	0	0
soul	0	0	0	1	1	0
space	0	0	0	1	0	0
stop	0	0	0	0	1	0
storm	0	0	0	0	1	0
strain	1	0	0	0	0	0
strange	0	0	0	1	1	0
succeed	1	0	0	0	0	0
success	1	0	0	0	0	0
sweet	1	0	0	0	1	0
take	1	0	0	0	0	0
tell	1	0	2	0	0	0
that	0	0	0	1	3	0
the	4	4	1	1	9	2
thee	0	2	0	0	0	0
them	0	0	0	1	0	0
then	0	0	1	2	0	0
there	0	0	1	0	0	0
they	0	0	1	1	0	0
thing	0	0	0	0	1	0
think	0	0	0	1	0	0
those	1	0	0	1	0	0
through	0	0	0	1	0	0
till	0	0	0	2	0	0
time	0	0	0	0	0	1
to	2	2	3	2	0	1
toll	0	0	0	1	0	0
too	0	0	1	0	0	0
tread	0	0	0	2	0	0
triumph	1	0	0	0	0	0
tune	0	0	0	0	1	0
ve	0	0	0	0	1	0
victory	1	0	0	0	0	0
warm	0	0	0	0	1	0
when	0	0	0	1	0	0
who	2	0	1	0	0	0
whose	1	0	0	0	0	0
wild	0	3	0	0	0	0
wind	0	1	0	0	0	0
with	0	3	0	1	1	0
without	0	0	0	0	1	0
word	0	0	0	0	1	0
wreck	0	0	0	1	0	0
yet	0	0	0	0	1	0
you	0	0	3	0	0	0
your	0	0	1	0	0	0
"""