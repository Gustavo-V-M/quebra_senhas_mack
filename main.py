import quebra_senhas

def get_words(arq_path):
    arq = open(arq_path, "r")
    lines = arq.readlines()
    arq.close()
    return lines
    
def get_encoded_pass(arq_path):
    arq = open(arq_path, "r")
    lines = arq.readlines()
    arq.close()
    return lines


def test_word(word, passwords):

    for w in range(len(passwords)):
        coded_word = quebra_senhas.codificar_senha(word)
        if coded_word == passwords[w]:
            return w
    
def check_permutation(permutation, passwords, arq, users):
    for i in range(len(permutation)):
        if test_word(permutation[i], passwords) != None:
            index = test_word(permutation[i], passwords) 
            arq.write(users[index]+":"+permutation[i]+"\n")


def permute_2(words):
    X = []
    for a in range(len(words)):
        cur_word = words[a]

        for b in range(0, len(words)):
            cur_word = cur_word + " " + words[b]

            X.append(cur_word)
            aux = cur_word.split(" ")
            if len(aux) == 2:
                cur_word = words[a]

    return X

def permute_rest(permutations, words):
    X = []
    for i in range(len(permutations)):
        for j in range(len(words)):
            X.append(permutations[i] + " " + words[j])
    
    return X

def main():
    words = get_words("palavras.txt")
    passwords_users = get_encoded_pass("usuarios_senhascodificadas.txt")

    cracked_passwords = open("senhas_quebradas.txt", "w")


    for i in range(len(passwords_users)):
        passwords_users[i] = passwords_users[i].strip("\n").split(":")
    
    for i in range(len(words)):
        words[i] = words[i].strip("\n")
    
    users = [""]*len(passwords_users)
    passwords = [""]*len(passwords_users)

    for i in range(len(passwords_users)):
        users[i] = passwords_users[i][0]
        passwords[i] = passwords_users[i][1]

    
    check_permutation(words, passwords, cracked_passwords, users)
            
    permutation_2 = permute_2(words)
    check_permutation(permutation_2, passwords, cracked_passwords, users)

    permutation_3 = permute_rest(permutation_2, words)
    check_permutation(permutation_3, passwords, cracked_passwords, users)
    
    permutation_4 = permute_rest(permutation_3, words)
    check_permutation(permutation_4, passwords, cracked_passwords, users)
            
    
    permutation_5 = permute_rest(permutation_4, words)
    check_permutation(permutation_5, passwords, cracked_passwords, users)
    
    print("ok!")
    cracked_passwords.close()
if __name__ == '__main__':
    main()