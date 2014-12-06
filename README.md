HATC
====

## Goals for (H)ash (A)lgorithm for (T)ext (C)omparison
Create a prototype method for specifying a reproducible hash of text content. Goals:

* Allow publishing of an Hash that allows comparison of a text when the actual content 
isn't available. 

* Allow parties who didn't create the hash to reliably reproduce the hash.

* The hash should allow comparison of subsections of the text.

* Finally this is just attempt demonstrate a concept. The assumption if this proves 
worthwhile other experts are likely to reimplement using more effecent algorithms. 


##Output Specification

JSON Document with the following key values

| Key                  | Description                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| algorithm            | Algorithm used  (MD5)                                                                                                |
| signature_encoding   | Type of encoding of used algorithm (I.E. HEX 64)                                                                     |
| signature_length     | For each subsectionsignature, how long the resulting key is a 32 character key can be truncated to fist 8 Chars. |
| delimiters           | For the document the is split into different sections, each section                                                  |
| pre_regex            | Regex used to clean up text before creating signature. Remove spaces etc.                                            |
| chars_signed         | Number of characters, pst pre_regex that are encoded. -1 is the complete document.                                   |
| signatures           | Array of signatures of each subsection of a document                                                                 |
| text_encoding        | Text encoding (UTF8 please!)                                                                                   |
      