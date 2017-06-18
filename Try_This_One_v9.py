from subprocess import *
import socket
import time
import sys
import re
import collections
import math

tokens_patterns = [
 ('NUMBER',    r'\d+(\.\d+([Ee]\d+)?)?'),
 ('OP_PLUS',   r'\+'),
 ('OP_MINUS',  r'\-'),
 ('OP_EXP',    r'\*\*'), 
 ('OP_MOD',    r'\%'),
 ('OP_TIMES',  r'\*'),
 ('OP_DIVIDE', r'/'),
 ('SQRT',      r'sqrt'),
 ('SKIP',      r'[ \t\n]+'),
]

Token = collections.namedtuple('Token', 'type value')

def tokenizer(expression):
    get_token = re.compile('|'.join('(?P<%s>%s)' % pair for pair in tokens_patterns)).search
    position = 0
    token = get_token(expression)
    while token:        
      token_type = token.lastgroup
      if token_type != 'SKIP':
          token_value = token.group(token_type)
          yield Token(token_type, token_value)
      token = get_token(expression, token.end())

def evaluate(expression):
    stack = []
    for token in tokenizer(expression):
        if token.type == 'NUMBER':
            stack.append(float(token.value))
        else:
            if token.type == 'SQRT':
                stack.append(float(stack.pop() ** (1 / 2)))
            else:
                value2 = stack.pop()
                value1 = stack.pop()
                if token.type == 'OP_PLUS':
                    stack.append(float(value1 + value2))
                elif token.type == 'OP_MINUS':
                    stack.append(float(value1 - value2))
                elif token.type == 'OP_TIMES':
                    stack.append(float(value1 * value2))
                elif token.type == 'OP_EXP':
                    stack.append(float(value1 ** value2))
                elif token.type == 'OP_MOD':
                    stack.append(float(value1 % value2))
                elif token.type == 'OP_DIVIDE':                
                    if value2 == 0:
                        raise ValueError('Division by zero')
                    else:
                        stack.append(float(value1 / value2))
    return stack.pop()

    
hostname="35.158.25.165"
port=10237

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, port))
q=s.recv(2048)
time.sleep(2)
content=s.recv(2048)
print "Content: "
print content

ans=evaluate(content)
print ans
ans=str(ans).split('.')[0]
time.sleep(1)
ans=ans+"\n"
print ans
s.sendall(ans.encode())

while True:
    content=s.recv(4096)
    if(len(content)>0):
        print content
        s.shutdown(socket.SHUT_WR)
        sys.exit(0)
