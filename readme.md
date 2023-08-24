Noisy Channel Model for Spellchecking and Autocorrect


Welcome! This application demonstrates the noisy-channel model that is used for spell-correction and autocorrect. The idea behind it is that a word has been “distorted” by being passed through a noisy communication channel. 
The process of the algorithm is simple: determine if a word is in the dictionary (this application uses a 70,000-word dictionary, some words are unfortunately missing).

If a word is not in the dictionary, create a list of spelling correction candidates that are 1 error away from the typed word.
Lastly, rank each candidate based on its probability of being the intended word, which is determined using the Bayesian Noisy-Channel model. 

There are 4 types of errors: substitution (substituting one letter for another), deletion (deleting one character), insertion (adding an extra character), and transposition(swapping the position of two adjacent letters).  
The letter w represents the correct word. The letter x represents the incorrect word, the one that the user typed. 
P(w) is the probability of word w being typed, and P(x) is the probability of the word x being typed. P(x | w) is the probability of x being typed given that w was the intended word. In other words, the probability that you would type x if you meant to type w. P(w | x) is the probability of w being the intended word given that x was typed. This is the value that matters and is used to rank all candidate corrections. The formula is based on Bayes’ Theorem formula P(w | x) = P(x | w) * P(w) / P(x). P(x) = 100% since we know that x was typed, so the formula can be reduced to P(w | x) = P(x | w) * P(w). 


P(x  | w), which is the probability of typing x when you intended to type w, is determined using a file that compiles thousands of common English spelling errors made online, and determining their frequencies. For example, typing A instead of E happens 100 times more than typing j instead of p. 


P(w), which is the probability of word w being typed, is determined using a list of all words in this programs dictionary, and their corresponding frequencies used on the internet. As you may know, “the” is the most common word, with over 23 billion instances in this dataset while a word like “puzzle” only has 14 million instances in this dataset.  

Options: 

Context Aware Correcting: When this option is on, the probability of a correction being next to the words before and after it is considered. This application comes with a datafile containing 333,000 bigram frequencies. What are bigram frequencies? It’s a list of how many times a word appears before or after another given word based on data from the internet. Although 333,000 seems like a lot, it’s actually misses quite a lot of word-pairs that are commonly used, which is why I have given you option to turn this on or off. 

Real-word errors: It is estimated that between 20%-40% of spelling errors involve a real-word replacing another real-word. For example, someone typing “then” instead of “the.” With this option on, the application will highlight a word in blue if it is spelled correctly but more likely than not a different word. This can only be determined in the context of other words, so Context Aware Correcting must be on  

What this application cannot do: 
This application generally does not support “cognitive” errors. That meaning errors in which you typed the word you intended but the word intended is incorrect. Errors of this kind can include grammatical errors, as well as substituting the correct word (ie. two vs too, their vs there). This program focuses on typographical errors, where you intend to type a word but type the wrong words.  

This application also does not support contractions at the time (eg. don’t, can’t, you’re). If there is any kind of punctuation in a word, it will be treated as two words. 


