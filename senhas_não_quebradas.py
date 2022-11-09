
def getUsers(arq):
    lines = arq.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split(":")

    l = len(lines)
    X = [""]*l

    for i in range(l):
        X[i] = lines[i][0]

    return X

def checkEquals(users_1, users_all):
    uncracked = []
    indexes = []
    for i in range(len(users_all)):
        add = True
        cur = users_all[i]
        for j in range(len(users_1)):
            if cur == users_1[j]:
                add = False
                break
        
        if add:
            uncracked.append(cur)
            indexes.append(i)


    return indexes

def main(): 
    cracked_passwords = open("senhas_quebradas.txt", "r")
    all_passwords = open("usuarios_senhascodificadas.txt", "r")
    all_passwords_lines = all_passwords.readlines()
    all_passwords.seek(0,0)

    uncracked_passwords = open("senhas_não_quebradas.txt", "w")

    cracked_users = getUsers(cracked_passwords)
    all_users = getUsers(all_passwords)

    indexes = checkEquals(cracked_users, all_users)


    if len(indexes) > 0:
        for i in range(len(indexes)):
            uncracked_passwords.write(all_passwords_lines[indexes[i]]+"\n")
        print("ok!")
    
    else:
        print("Não existem senhas a serem quebradas!")

    cracked_passwords.close()
    all_passwords.close()
    uncracked_passwords.close()


if __name__ == "__main__":
    main()