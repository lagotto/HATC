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
      
## Example

The following text

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