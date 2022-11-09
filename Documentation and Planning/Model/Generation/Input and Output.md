# Design comments

The way inputs flow into, and outputs
flow out of, the model should be clearly
defined.

Insight is drawn from deberta in allowing 
for the existence of decoupled lexical
information.

# Input

Let it be the case that an input to a standard transformer is 
defined to be a tensor of shape [..., items, embedding]

The inputs to the generation portion of the model will be a 
canvas collection and an embedding collection.

* Mask. Indicates what elements will not contribute to the loss
* Canvas. Indica

* Mask. 
  * This is a tensor whose last dimension is of length items.
  * True means this element will show up in the output
  * False means it will not.

The inputs used to setup the model is defined as deberta-like
couplings of content, relative-position tensors. It is
the case that two such pairings are expected:

* Canvas
* Embeddings

# Output

The output that shall be provided will be a tensor
of the same length as the canvas. Elements of the canvas