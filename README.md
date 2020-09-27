# A Simple Substitution Cipher implementation in Python 

## The Simple Substitution Cipher

This type of cipher was used by Julius Caesar to communicate with his generals. 
It is very simple to generate but it can actually be easily broken and does not provide the security one would hope for.


## ccrack
Feed the encrypted message into `ccrack`.



```
> python ccrack.py "Dtz pjju ts zxnsl ymfy btwi. N it sty ymnsp ny rjfsx bmfy dtz ymnsp ny rjfsx."
5
```

Use the returned substitution cipher to convert the encrypted message back into plain text with `cipher`.

```
> cipher -k 5 -d "Dtz pjju ts zxnsl ymfy btwi. N it sty ymnsp ny rjfsx bmfy dtz ymnsp ny rjfsx."
Your plain text message is: You keep on using that word. I do not think it means what you think it means.

```

**Results:**

```
> ccrack "T lx azdetyr gpcj wlep"
11

> cipher -k  11 -d "T lx azdetyr gpcj wlep"
Your plain text message is: I am posting very late

> ccrack "Dtz pjju ts zxnsl ymfy btwi. N it sty ymnsp ny rjfsx bmfy dtz ymnsp ny rjfsx."
5

> cipher -k 5 -d "Dtz pjju ts zxnsl ymfy btwi. N it sty ymnsp ny rjfsx bmfy dtz ymnsp ny rjfsx."
Your plain text message is: You keep on using that word. I do not think it means what you think it means.

> ccrack "Sdu wi E skngejc kj pdeo necdp jks?"
22

> cipher -k 22 -d "Sdu wi E skngejc kj pdeo necdp jks?"
Your plain text message is: Why am I working on this right now?

> ccrack "K co ugetgvkxg"
2

(aes) C:\dev\homework2>cipher -k 2 -d "K co ugetgvkxg"
Your plain text message is: I am secretive

(aes) C:\dev\homework2>ccrack "M aexglih qsricfepp qszmi ciwxivhec."
4

(aes) C:\dev\homework2>cipher -k 4 -d "M aexglih qsricfepp qszmi ciwxivhec."
Your plain text message is: I watched moneyball movie yesterday.

(aes) C:\dev\homework2>ccrack "Al ak zsadafy!"
22

(aes) C:\dev\homework2>cipher -k 22 -d "Al ak zsadafy!"
Your plain text message is: Ep eo dwehejc!

(aes) C:\dev\homework2>ccrack "Rcvo yj tjp rvio oj ads di ocdn kmjbmvh?"
21

(aes) C:\dev\homework2>cipher -k 21 -d "Rcvo yj tjp rvio oj ads di ocdn kmjbmvh?"
Your plain text message is: What do you want to fix in this program?

(aes) C:\dev\homework2>ccrack "Ocdn dn v ozno ja ocz zhzmbzixt wmjvyxvno ntnozh. Ocdn dn jigt v ozno!"
21

(aes) C:\dev\homework2>cipher -k 21 -d "Ocdn dn v ozno ja ocz zhzmbzixt wmjvyxvno ntnozh. Ocdn dn jigt v ozno!"
Your plain text message is: This is a test of the emergency broadcast system. This is only a test!

(aes) C:\dev\homework2>ccrack "Zgo dgfy vav al lscw qgm?"
18

(aes) C:\dev\homework2>cipher -k 18 -d "Zgo dgfy vav al lscw qgm?"
Your plain text message is: How long did it take you?

(aes) C:\dev\homework2>ccrack "Nby Uxpuhwyx Yhwlsjncih Mnuhxulx (UYM), ufmi ehiqh vs cnm ilcachuf hugy Lcdhxuyf cm u mjywczcwuncih zil nby yhwlsjncih izyfywnlihcw xunu ymnuvfcmbyx vs nby O.M. Huncihuf Chmncnony iz Mnuhxulxm uhx Nywbhifias (HCMN) ch 2001."
20

(aes) C:\dev\homework2>cipher -k 20 -d "Nby Uxpuhwyx Yhwlsjncih Mnuhxulx (UYM), ufmi ehiqh vs cnm ilcachuf hugy Lcdhxuyf cm u mjywczcwuncih zil nby yhwlsjncih iz yfywnlihcw xunu ymnuvfcmbyx vs nby O.M. Huncihuf Chmncnony iz Mnuhxulxm uhx Nywbhifias (HCMN) ch 2001."
Your plain text message is: The Advanced Encryption Standard (AES), also known by its original name Rijndael is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001.

(aes) C:\dev\homework2>ccrack "Efn nv ufe'k jzdgcp yrmv Trvjri jrcru - nv yrmv Trvjri tzgyvi!"17

(aes) C:\dev\homework2>cipher -k 17 -d "Efn nv ufe'k jzdgcp yrmv Trvjri jrcru - nv yrmv Trvjri tzgyvi!"Your plain text message is: Now we don't simply have Caesar salad - we have Caesar cipher!

(aes) C:\dev\homework2>ccrack "Bpm owit wn lqaqvbmzumlqibqvo ivg bpqzl-xizbqma uig jm i owwl wvm nwz i kzgxbwkczzmvkg, xizbqkctiztg qn gwc izm ewzzqml ijwcb idwqlqvo qvbmznmzmvkm nzwu owdmzvumvb iomvkqma, jcb bpib'a vwb vmkmaaizqtg i owwl owit nwz mvbmzxzqam awnbeizm."
8

(aes) C:\dev\homework2>cipher -k 8 -d "Bpm owit wn lqaqvbmzumlqibqvo ivg bpqzl-xizbqma uig jm i owwl wvm nwz i kzgxbwkczzmvkg, xizbqkctiztg qn gwc izm ewzzqml ijwcb idwqlqvo qvbmznmzmvkm nzwu owdmzvumvb iomvkqma, jcb bpib'a vwb vmkmaaizqtg i owwl owit nwz mvbmzxzqam awnbeizm."
Your plain text message is: The goal of disintermediating any third-parties may be a good one for a cryptocurrency, particularly if you are worried about avoiding interference from government agencies, but that's not necessarily a good goal for enterprise software.

(aes) C:\dev\homework2>cipher -k 8 -d "Bpm owit wn lqaqvbmzumlqibqvo ivg bpqzl-xizbqma uig jm i owwl wvm nwz i kzgxbwkczzmvkg, xizbqkctiztg qn gwc izm ewzzqml ijwcb idwqlqvo qvbmznmzmvkm nzwu owdmzvumvb iomvkqma, jcb bpib'a vwb vmkmaaizqtg i owwl owit nwz mvbmzxzqam awnbeizm."
```

