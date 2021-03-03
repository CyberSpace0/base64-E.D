print('                                                 '
      '\n'
      ' _______         /\            //   ) ) |------   '
      '\n |      )       /  \          ((        |      ||     '
      '\n |______|      /    \           \\       |       || '
      '\n |      |     /======\           ) )    |      ||'
      '\n |______)    /        \   ((___ / /     |_______||     '
      '\n\n    ')

def base64():
    import base64
    print('\n'
         '[1] encode\n'
        '[2] decode')
    user = input('enter value []:')
    if user == '1':
        encode = input('enter value be encode')
        print(base64.b64encode(encode.encode('UTF-8')))
    elif user == '2':
        decode = input('enter value be decode')
        print(base64.b64decode(decode))
base64()





