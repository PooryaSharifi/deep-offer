# deep-offer
Seasonal aware recommendation system

## why Hybrid (collaborative + content based) recommendation failed
### first it is not all about content
suppose we have two use in our platform (A, B), that they share nearly same properties. if A order product c, the probablity which B gonna buy c does not increase sufficiently. on the other hand, if product d which is nearly the same as product c, is also available in our system. the probablity which A and B are gonna buy it. is not sufficiently increases.

### man at the spot dilemma
from the point of heyek [The Use Of Knowledge In Society, 1945](https://www.cato.org/sites/cato.org/files/articles/hayek-use-knowledge-society.pdf) market mechanism (offers and gifts in ecommerce websites), and realtime inputs which users are gonna see. are important to their product selections to order. so history of events which user is expreriensing is important.

also seasonal needs of users is imporant to consider for perfect recommendation system

## Solution
### Timeseries prediction using something like transformers: [attention is all you need](https://arxiv.org/abs/1706.03762) which offers good results in varies of problem categories.
![alt text](https://github.com/PooryaSharifi/deep-offer/blob/main/text_gen.jpg?raw=true)
