def lettercoding(code):
    table = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print('code: ' + code)
    output = ''
    for i in range(len(code)):
        letterindex = code[i]
        cypher = table.index(letterindex)
        encrypt = cypher + 3
        output += table[encrypt]
    print('encrypt: ' + output)
    lettercoding_decrypt(output)
    
def lettercoding_decrypt(code):
    table = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    output = ''
    for i in range(len(code)):
        letterindex = code[i]
        cypher = table.index(letterindex)
        encrypt = cypher - 3
        output += table[encrypt]
    print('decrypt: ' + output)

lettercoding('space wars')
