HATC
====

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

The following meat article

    Bacon ipsum dolor amet ham shank chuck ball tip. Jowl cow jerky porchetta corned beef, strip steak tenderloin shankle short loin fatback. Spare ribs ham pork belly bacon, t-bone drumstick pancetta kevin rump porchetta hamburger capicola tongue turducken. Bacon capicola sausage tri-tip doner, ground round jowl pork pancetta chicken sirloin shank short ribs. Ham jerky short ribs short loin prosciutto pork belly. Pork belly shoulder ham hock bresaola pork chop doner beef, pancetta filet mignon pork loin.
    
    Prosciutto andouille rump landjaeger meatball. Leberkas meatball sirloin bacon ham hock, boudin strip steak ribeye kielbasa sausage meatloaf pork chop. Alcatra frankfurter spare ribs short loin pastrami swine pork prosciutto cupim jowl ribeye biltong. Porchetta biltong jerky hamburger cow frankfurter rump flank.
    
    Meatloaf sausage cupim alcatra landjaeger, tongue strip steak pastrami beef spare ribs. Meatloaf tail tenderloin pork loin. Tail shankle swine spare ribs picanha. Frankfurter shank flank venison, pork belly cow rump pastrami.
    
    Capicola pancetta shoulder picanha short loin flank ground round bacon sausage. Pig corned beef capicola t-bone, ham hock pancetta pastrami biltong bresaola chicken pork. Pork loin hamburger shankle, alcatra corned beef pork tail boudin spare ribs landjaeger strip steak ham hock. Venison ground round ham filet mignon tenderloin, beef ribs pork belly. Porchetta meatloaf landjaeger biltong.

Could be encoded as

    {
        "algorithm": "MD5_128",
        "chars_signed": -1,
        "delimiters": ".",
        "pre_regex": "[\s]",
        "signature_encoding": "BASE_64",
        "signature_length": 8,
        "signatures": [
            "9cb87bdb",
            "a6d4598f",
            "fc41fa2b",
            "0feb2a2b",
            "7bc54e52",
            "faba705d",
            "6840b0d8",
            "89096eb4",
            "d21e498f",
            "fa3befc7",
            "67b9e179",
            "d90ef02a",
            "8590c917",
            "8cf11d6a",
            "cecd1900",
            "df07f642",
            "7fb1fe75",
            "7bb2eff4",
            "21b708ba",
            "21b708ba"
        ],
        "text_encoding": "UTF8"
    }
    
Suppose a cupcake article referenced a subsection of the meat article.

        Carrot cake chocolate bar ice cream powder muffin apple pie pastry soufflé jelly-o. Sugar plum toffee brownie candy dragée donut fruitcake cookie lollipop. Liquorice sesame snaps icing jelly beans chocolate carrot cake. Halvah marshmallow lollipop applicake. Gummies chocolate bar marshmallow cake oat cake. Lemon drops croissant jujubes. Tart jelly beans danish applicake sweet roll liquorice. Unerdwear.com gummies marshmallow bonbon cookie bear claw brownie. Tiramisu cake lemon drops sweet. Macaroon muffin brownie gingerbread gingerbread wafer candy unerdwear.com marshmallow. Jujubes pastry icing bear claw applicake. Oat cake lemon drops lemon drops biscuit tootsie roll.
        
        Meatloaf sausage cupim alcatra landjaeger, tongue strip steak pastrami beef spare ribs. Meatloaf tail tenderloin pork loin. Tail shankle swine spare ribs picanha. Frankfurter shank flank venison, pork belly cow rump pastrami.
        
        Toffee fruitcake cookie muffin liquorice oat cake. Dessert lollipop halvah oat cake. Carrot cake gummi bears tart wafer oat cake bear claw jelly-o unerdwear.com liquorice. Applicake croissant lollipop. Bear claw soufflé macaroon. Danish tiramisu jelly liquorice danish. Sesame snaps sesame snaps marzipan tootsie roll halvah donut sesame snaps candy. Sweet roll fruitcake liquorice bear claw bonbon chocolate cheesecake chocolate bar applicake. Jelly beans chocolate cake macaroon donut. Tiramisu oat cake chocolate cake marzipan danish danish gummi bears bear claw. Soufflé muffin macaroon jelly beans. Candy canes carrot cake lollipop pastry macaroon pie fruitcake oat cake muffin.
      
would be encoded as
  
      
      {
          "algorithm": "MD5",
          "chars_signed": -1,
          "delimiters": ".",
          "pre_regex": "[\\s]",
          "signature_encoding": "BASE_64",
          "signature_length": 8,
          "signatures": [
              "f79857a1",
              "82f867e7",
              "79d53163",
              "e332ed2a",
              "8ff34306",
              "a6c1884e",
              "7b5a94b9",
              "23145dd5",
              "f53bd129",
              "c0043f88",
              "11b37eab",
              "f4c32e99",
              "fd36d520",
              "c826212b",
              "94fe88d0",
              "9a42af2c",
              "6af3afc4",
              "88b58a00",
              "1ba18f42",
              "6c0bf019",
              "73a6670c",
              "6adbac6c",
              "26fb8feb",
              "1d8f44bf",
              "3c39f784",
              "ce425fc7",
              "a6f8fa5b",
              "8842e658",
              "4415b832",
              "22971773",
              "d84faf4c",
              "d84faf4c"
          ],
          "text_encoding": "UTF8"
      }      
