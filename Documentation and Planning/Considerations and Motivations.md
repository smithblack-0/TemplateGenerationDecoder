## Decoding

### Autoregressive decoding

The general consensus around text generation in the modern
era is to use autoregressive decoding to predict the 
next word using the previous ones. This has certain
indisputable advantages 

* It inherently orders information allowing easy gramatical learning
* It captures the fact that text is not commutive quite effectively

However, I think there are some very major disadvantages when planning
a large document which will impeed it every being utilized to sanely
generate a cohesive story.

* As a personal writer, it is HARD to generate the introduction before the rest of a paper

### Out of order decoding

Instead, I think it would be better to perform out of
order decoding, in which the model is allowed to 
build its output in any order and to any degree it
wishes. 

So that, for instance, if the model wants to make the 
thesis and the body first, it can do so. This, however,
requires 

To make this trainable, there are multiple possible approaches,
such as providing a canvas to write onto for the entire
document at once with a template, or splitting the document
into subsections.