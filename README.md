# deep-offer
Seasonal aware recommendation system \
each offer that shows to a user of a system e.g e-commerces is costly for him, it makes bias in his mind and takes .2 seconds of his time on average so a couple of percents in increase of recommendation precision is worthy.

## why Hybrid (collaborative + content based) recommendation failed
### first it is not all about content
suppose we have two use in our platform (A, B), that they share nearly same properties. if A order product c, the probablity which B gonna buy c does not increase sufficiently. on the other hand, if product d which is nearly the same as product c, is also available in our system. the probablity which A and B are gonna buy it. is not sufficiently increases.

### man at the spot dilemma
from the point of heyek [The Use Of Knowledge In Society, 1945](https://www.cato.org/sites/cato.org/files/articles/hayek-use-knowledge-society.pdf) market mechanism (offers and gifts in e-commerce websites), and realtime inputs which users are gonna see. are important to their product selections to order. so history of events which user is expreriensing is important. \
also seasonal needs of users is imporant to consider for perfect recommendation system. ready for a good solution for a welly defined problem!

## Solution
### why not using deep learning models to predict next order of each user
the use of recurrent neural nets in text generation is a well known practice. but we can suppose each word as a product related to a user \
![alt text](https://github.com/PooryaSharifi/deep-offer/blob/main/text_gen.png?raw=true)
then timeseries prediction using something like transformers: [attention is all you need](https://arxiv.org/abs/1706.03762) which offers good results in varies of problem categories. \
here we know that:
  - oona ke check karde. oona ke kharide.
  - each product has a brand.
  - each product has a category
  - each product has a (Repetitive | Popular) name
  - each product has a time which seen or bought by a casual user
  - dar oon lahze cheghad offer dashte
  - use a text generation to predict next things that probably got bought

![alt text](https://github.com/PooryaSharifi/deep-offer/blob/main/offer_gen.png?raw=true)
