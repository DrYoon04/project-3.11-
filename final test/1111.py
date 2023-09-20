with open('hello.txt','r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))

        '''readline으로 파일을 읽을때는 while을 사용해야함'''