import quebra_senhas

#TODO
#arrumar codigo de checar senhas
#escrever os nos arquivos

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
            print(word)
            return word
    

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

def write_decoded_pass(user, password):
    pass

def main():
    words = get_words("palavras.txt")
    passwords_users = get_encoded_pass("usuarios_senhascodificadas.txt")

    for i in range(len(passwords_users)):
        passwords_users[i] = passwords_users[i].strip("\n").split(":")
    
    for i in range(len(words)):
        words[i] = words[i].strip("\n")
    
    users = passwords_users[0]
    passwords = passwords_users[1]

    for i in range(len(words)):
        print(words[i])
            
    permutations_2 = permute_2(words)
    for i in range(len(permutations_2)):
        print(permutations_2[i])
    
    permutation_3 = permute_rest(permutations_2, words)
    for i in range(len(permutation_3)):
        print(permutation_3[i])
    
    permutation_4 = permute_rest(permutation_3, words)
    for i in range(len(permutation_4)):
        print(permutation_4[i])
            
    
    permutation_5 = permute_rest(permutation_4, words)
    for i in range(len(permutation_5)):
        print(permutation_5[i])

    

if __name__ == '__main__':
    main()