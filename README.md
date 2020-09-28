# A Simple Substitution Cipher implementation in Python 

## The Substitution Cipher

This type of cipher was used by Julius Caesar to communicate with his generals, and thus it is sometimes referred to as a Caesar cipher 
It is very simple to generate but it can actually be easily broken and does not provide the security one would hope for.

## Encrypt Example 

Encrypt a Caesar cipher encrypted message with a 21 character shift

    > python ccipher.py -k 21 "This is a test of the emergency broadcast system. This is only a test!"
    Your encrypted message is: 
    Ocdn dn v ozno ja ocz zhzmbzixt wmjvyxvno ntnozh. Ocdn dn jigt v ozno!



## Decrypt Example 

Decrypt a Caesar cipher encrypted message

    > python ccrack.py "Dtz pjju ts zxnsl ymfy btwi. N it sty ymnsp ny rjfsx bmfy dtz ymnsp ny rjfsx."
    5


Use the returned substitution cipher shift to convert the encrypted message back into plain text with `ccipher`.

    > python ccipher.py -k 5 -d "Dtz pjju ts zxnsl ymfy btwi. N it sty ymnsp ny rjfsx bmfy dtz ymnsp ny rjfsx."
    Your plain text message is:
    You keep on using that word. I do not think it means what you think it means.



