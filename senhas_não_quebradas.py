
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


    return uncracked,indexes

def main(): 
    cracked_passwords = open("senhas_quebradas.txt", "r")
    all_passwords = open("usuarios_senhascodificadas.txt", "r")
    all_passwords_lines = all_passwords.readlines()

    uncracked_passwords = open("senhas_não_quabradas.txt", "w")

    cracked_users = getUsers(cracked_passwords)
    all_users = getUsers(all_passwords)

    uncracked_users, indexes = checkEquals(cracked_users, all_users)

    for i in range(len(uncracked_users)):
        uncracked_passwords.write(uncracked_users[i]+":"+all_passwords_lines[indexes[i]]+"\n")

    cracked_passwords.close()
    all_passwords.close()
    uncracked_passwords.close()

    print("ok!")

if __name__ == "__main__":
    main()