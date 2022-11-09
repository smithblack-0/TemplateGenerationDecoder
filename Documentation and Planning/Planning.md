
# Considerations


## Document length

The canvas that will be worked on is not at all limited in
length. In theory, the model might be asked to generate, for
example, 10000 words at once. 

This is not, in and of itself, a problem. However, the standard
mechanisms of generation are. Attention has asymptotic behavior
of O(N^2) with respect to the number of embeddings, meaning this
would quickly get out of control.

All care must be taken to ensure the behavior instead comes
out to be at least O(N log(N)), and preferably O(N)

## Types of task

The generation system must be compatible with many different
types of tasks. Let's enumerate some of them

* Manually define a canvas, then use the encoder to ask for document modification
* Define a canvas with a prior layer, and expect to use it and the encodings
  for language translation
* Define the entire task on a provided canvas as a template, to fill in the blanks.

This means we must be able to query the encodings, query ourselves,
and probability query some other things in some circumstances as well.


# Design

This section is about the design of the model.

The model is a canvas/template generative transformer designed
to fill into a template of sorts with the appropriate 
information whatsoever is going on.

It consists of a decode loop for filling in some sort
of template and additional auxiliary information. It
supports out-of-order (OoO) decoding.


## Design flow 

This outlines how the flow of information through the
model works, along with various parts of the model.


* Decode Loop Start
  * ACT 
    * Bypass Start
      * Content Memory Query
      * Local Connectivity
      * Embedding Decode Layer
      * Feedforward
      * Embeddings Attention
      * Feedforward
      * Central Transfer
        * Self attention
        * Feedforward
        * Control Memory Query
        * FeedForward
        * Control Memory Update
      * Feedback Transfer
      * Feedforward
    * Bypass End
    * Feedforward
    * ACT Update
  * Content Memory Superposition
  * Token Predictions. (Sampled?)
  * Top-p. 
  * Select
  * FORK: Training
    * Correct Token Substitute.
  * FORK: Eval
    * Token Substitute


# Design elements

## 


## Memory

A collection of tensors corrolating with steps in an
ACT process. 

Memory can be configured on construction as an ACT memory 
element, or a standard memory element. ACT memory
elements must be provided with a halting probability at the
moment of storage, and will lock itself then throw when 
finished. 

Standard memory, on the other hand, simply consists
of a collection of tensors. These tensor, however, are again
loadable.

Memory can and should be loaded with some default
parameters when created, but as the name implies can be 
appended to. 

* ACT memory 
  * Fields
    * Key
    * Value
  * Methods
    * Last
    * Query
    * Update


## Local Connectivity Layer

The local connectivity layer is responsible
for ensuring the sane interactions between elements
based on their relative positions. It is what
is responsible for ensuring correct positioning
of letters.

* Local Connectivity
  * Input
    * Content Tensor: Float
    * Flags Tensor: Bool
    * Lexical Tensor: Float
  * Output
    * Content Tensor
  * Action
    * Heading
    * Localization
    * Attention 
      * Deberta interaction on crosstalk between flags, content, lexical
    * Feedforward
    * Convolutional Collapse
    * Head Collapse
    * Feedforward
    * Add plus normalize

## Central Planning

The central planning layer exists to allow
the 

## Embedding Decode Layer

Retrieves information off the 