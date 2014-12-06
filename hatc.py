import md5
import re
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', default='')
parser.add_argument('-f', '--file', default=None)
args = parser.parse_args()

text = args.text

if args.file is not None:
    text = open(args.file, 'r').read()

algorithm = 'MD5'
signature_encoding = 'BASE_64'
signature_length = 8
delimiters = '.'
pre_regex = '[\s]'
chars_signed = -1
signatures = []
text_encoding = 'UTF8'

m = md5.new()
pre_reg = re.compile(pre_regex)
 
 
def encode_section(section, max_length):
    global m
    m.update(section)
    return m.hexdigest()[:max_length]

def pre_process(text, delimiter):
    global pre_re
    return re.sub(pre_reg,'',text).split(delimiter)        
    

print text

for section in pre_process(text,'.'):
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
