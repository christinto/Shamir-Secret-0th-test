Secret Sharing Tests
=============

[![PyPI](https://img.shields.io/pypi/l/secretsharing.svg)](https://github.com/Tenzorum/Shamir-Secret-0th-test/blob/master/LICENSE)
[![Tenzorum Website]()](https://tenzorum.org/)

A command line PoC for sharding and sharing secrets (e.g. Ethereum, bitcoin or traditional login keys), using Shamir-Secret sharing scheme.

## Installation
Before installing you'd need to make sure you have pip and utility belt installed:
* Open terminal, then install pip and utilitybelt
##  
    >>> sudo easy_install pip
    >>> sudo pip install utilitybelt
##    

## Clone Secret Sharing 0th test repository from Tenzorum GitHub to your machine
    
    >>> git clone https://github.com/Tenzorum/Shamir-Secret-0th-test.git

### Navigate to repository

    >>> cd Shamir-Secret-0th-test/
    >>> cd v2 
## 
## Run Shamir Secret Sharing PoC
  
    >>> python shamir.py
    
 ### Insert your secret text following the prompt 
 
 `Tell me your secret:`
 ### Choose how many fragments will the secret be sliced 
 
 `How many pieces should I slice your secret?`
 
 ### Choose the number of minimum fragments required to reconstruct the secret:
 
 `Which is the minimum amount of pieces to recover you secret?`
 
 ### Insert the fragments numbers with comma separated
 
 `Which pieces should I use to recover [ comma separated: ex: 1, 3, 4]?`
 
 
