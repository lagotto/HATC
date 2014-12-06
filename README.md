HATC
====

# REFACTOR add (N-Gram) by work example [http://en.wikipedia.org/wiki/N-gram]

## Goals for (H)ash (A)lgorithm for (T)ext (C)omparison
Create a prototype method for specifying a reproducible hash of text content. Goals:

* Allow publishing of an Hash that allows comparison of a text when the actual content isn't available.

* Allow parties who didn't create the hash to reliably reproduce the hash.

* The hash should allow comparison of subsections of the text.

* Finally this is just attempt demonstrate a concept. The assumption if this proves worthwhile other experts are likely to reimplement using more effecent algorithms.


## Output Specification

JSON Document with the following key values

| Key                  | Description                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| algorithm            | Algorithm used  (MD5)                                                                                                |
| chars_signed         | Number of characters, pst pre_regex that are encoded. -1 is the complete document.                                   |
| delimiters           | how the document the is split into different sections                                               |
| pre_regex            | Regex used to clean up text before creating signature. Remove spaces etc.  (better options then regex might be good) |
| signatures           | Array of signatures of each subsection of a document                                                                 |
| signature_encoding   | Type of encoding of used algorithm (I.E. HEX 64)                                                                     |
| signature_length     | For each section signature, how many characters are used. For example MD5_128 is 32 long but we could choose to only use the first 8. |
| text_encoding        | Text encoding (UTF8 please!)                                                                                   |
      
## Example 1

The following bacon article

    Bacon ipsum dolor amet ham shank chuck ball tip. Jowl cow jerky porchetta corned beef, strip steak tenderloin shankle short loin fatback. Spare ribs ham pork belly bacon, t-bone drumstick pancetta kevin rump porchetta hamburger capicola tongue turducken. Bacon capicola sausage tri-tip doner, ground round jowl pork pancetta chicken sirloin shank short ribs. Ham jerky short ribs short loin prosciutto pork belly. Pork belly shoulder ham hock bresaola pork chop doner beef, pancetta filet mignon pork loin.
    
    Prosciutto andouille rump landjaeger meatball. Leberkas meatball sirloin bacon ham hock, boudin strip steak ribeye kielbasa sausage meatloaf pork chop. Alcatra frankfurter spare ribs short loin pastrami swine pork prosciutto cupim jowl ribeye biltong. Porchetta biltong jerky hamburger cow frankfurter rump flank.
    
    Meatloaf sausage cupim alcatra landjaeger, tongue strip steak pastrami beef spare ribs. Meatloaf tail tenderloin pork loin. Tail shankle swine spare ribs picanha. Frankfurter shank flank venison, pork belly cow rump pastrami.
    
    Capicola pancetta shoulder picanha short loin flank ground round bacon sausage. Pig corned beef capicola t-bone, ham hock pancetta pastrami biltong bresaola chicken pork. Pork loin hamburger shankle, alcatra corned beef pork tail boudin spare ribs landjaeger strip steak ham hock. Venison ground round ham filet mignon tenderloin, beef ribs pork belly. Porchetta meatloaf landjaeger biltong.

Could be encoded as

      python hatc.py  -f bacon_ipsum.txt 
      {
          "delimiters": ".",
          "signatures": [
              "9cb87bdb",
              "65d51238",
              "3018f2fa",
              "b213e94c",
              "4e6cdf55",
              "3df4ffd7",
              "87de3f39",
              "a1c5c2d8",
              "7038fd13",
              "65709c7c",
              "e81721c3",
              "443461bb",
              "9e8f7047",
              "29b22339",
              "4ad7cff2",
              "8b0e62fc",
              "899f0b76",
              "008a4665",
              "1ba6c8ed"
          ],
          "pre_regex": "[\\s]",
          "algorithm": "MD5",
          "signature_encoding": "BASE_64",
          "chars_signed": -1,
          "text_encoding": "UTF8",
          "signature_length": 8
      }
          
Suppose a cupcake article might referenced a subsection of the bacon article.

        Carrot cake chocolate bar ice cream powder muffin apple pie pastry soufflé jelly-o. Sugar plum toffee brownie candy dragée donut fruitcake cookie lollipop. Liquorice sesame snaps icing jelly beans chocolate carrot cake. Halvah marshmallow lollipop applicake. Gummies chocolate bar marshmallow cake oat cake. Lemon drops croissant jujubes. Tart jelly beans danish applicake sweet roll liquorice. Unerdwear.com gummies marshmallow bonbon cookie bear claw brownie. Tiramisu cake lemon drops sweet. Macaroon muffin brownie gingerbread gingerbread wafer candy unerdwear.com marshmallow. Jujubes pastry icing bear claw applicake. Oat cake lemon drops lemon drops biscuit tootsie roll.
        
        Meatloaf sausage cupim alcatra landjaeger, tongue strip steak pastrami beef spare ribs. Meatloaf tail tenderloin pork loin. Tail shankle swine spare ribs picanha. Frankfurter shank flank venison, pork belly cow rump pastrami.
        
        Toffee fruitcake cookie muffin liquorice oat cake. Dessert lollipop halvah oat cake. Carrot cake gummi bears tart wafer oat cake bear claw jelly-o unerdwear.com liquorice. Applicake croissant lollipop. Bear claw soufflé macaroon. Danish tiramisu jelly liquorice danish. Sesame snaps sesame snaps marzipan tootsie roll halvah donut sesame snaps candy. Sweet roll fruitcake liquorice bear claw bonbon chocolate cheesecake chocolate bar applicake. Jelly beans chocolate cake macaroon donut. Tiramisu oat cake chocolate cake marzipan danish danish gummi bears bear claw. Soufflé muffin macaroon jelly beans. Candy canes carrot cake lollipop pastry macaroon pie fruitcake oat cake muffin.
      
would be encoded as
      
       {
           "delimiters": ".",
           "signatures": [
               "f79857a1",
               "c0d47091",
               "accdd051",
               "43787f32",
               "e9af37c4",
               "7608abf7",
               "2f68d6e1",
               "c0500edf",
               "323d75c5",
               "c5b0d4b1",
               "f3ff8839",
               "ddddae4f",
               "10704b08",
               "3a54c42c",
               "e81721c3",
               "443461bb",
               "9e8f7047",
               "29b22339",
               "daa61122",
               "cf5ea978",
               "563036d4",
               "241d7830",
               "f1e16b4d",
               "9cd7e9cd",
               "c7710519",
               "0730098a",
               "40366d68",
               "47e6f04d",
               "d3e1d1e6",
               "29bf4360",
               "17d449b5"
           ],
           "pre_regex": "[\\s]",
           "algorithm": "MD5",
           "signature_encoding": "BASE_64",
           "chars_signed": -1,
           "text_encoding": "UTF8",
           "signature_length": 8
       }
                    
By looking at the hashes we see an union of: e81721c3, 443461bb, 9e8f7047 and 29b22339 
and could surmise the cupcake article references the bacon article.   
