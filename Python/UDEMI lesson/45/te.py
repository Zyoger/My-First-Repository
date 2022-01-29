f = b'test.bin'

# unicode string
string = 'pythön!'
# print string
print('The string is:', string)
# default encoding to utf-8
string_utf = string.encode('cp037')
# print result
print('The encoded version is:', string_utf)

with open(f, 'wb') as f:
    f.write(string_utf)
