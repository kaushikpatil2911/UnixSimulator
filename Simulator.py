def get_new_path (path, where):
    if not where:
        return path 
        
    if where[0] == '.':
        where = where[1:]
        if not where:
            return path 
        where = where[1:]
        return get_new_path (path, where)
    
    if where[0] == '..':
        where = where [1:]
        if not path:
            return path
        path.pop()
        path.pop()
        if not where:
            return path 
        where = where[1:]
        return get_new_path (path, where)

    if not where[0].isalnum():
        return where[0] + ": No such file or directory"
        
    if path [-1] != '/':
        path.append ('/')
    
    path.append (where[0])
    where = where[1:]
    if not where:
        return path 
    where = where[1:]
    return get_new_path (path, where)
    

while True:
    print ("# ", end = "")
    command = input().split()
    if len(command) != 3:
        print ("Bad input")
        continue
    if command[0] != 'mycd':
        print ("Bad input")
        continue
    
    path = command[1]
    where = command[2]
    while path.find("//") != -1:
        path = path.replace ("//", "/")
        print (path)
    while where.find("//") != -1:
        where = where.replace ("//", "/")

    path = path.replace ("/", "@/@").split("@")
    path = [item for item in path if item != '']
    where = where.replace ("/", "@/@").split("@")
    where = [item for item in where if item != '']

    if where[0] == '/':
        path = ''.join(where)
        print (path)
        continue
    
    path = get_new_path (path, where)
    if not path:
        path = ['/']
    path = ''.join(path)
    print (path)
