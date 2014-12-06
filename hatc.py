import md5
import re
import json

algorithm = 'MD5'
signature_encoding = 'BASE_64'
signature_length = 8
delimiters = '.'
pre_regex = '[ \t\r\n]'
chars_signed = -1
signatures = []
text_encoding = 'UTF8'

m = md5.new()
pre_reg = re.compile('[ \t\r\n]')
 
 
def encode_section(section, max_length):
    global m
    m.update(section)
    return m.hexdigest()[:max_length]

def pre_process(text, delimiter):
    global pre_re
    return re.sub(pre_reg,'',text).split(delimiter)
        
    
bacon = open('bacon_ipsum.txt', 'r').read()



print bacon

for section in pre_process(bacon,'.'):
    signatures.append(encode_section(section,8))

print json.dumps(
    {
      'algorithm': algorithm,
      'chars_signed': -1,
      'signature_encoding': signature_encoding, 
      'signatures': signatures,
      'delimiters': delimiters,
      'pre_regex': pre_regex,
      'signature_length': signature_length,
      'text_encoding': text_encoding
    },
    sort_keys=True, 
    indent=4, 
    separators=(',', ': '))
