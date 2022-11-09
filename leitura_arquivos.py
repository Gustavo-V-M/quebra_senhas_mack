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

def permute_3(permutations, words):
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
    
    permutations_2 = permute_2(words)
    for i in permutations_2:
        print(i)
    
    permutation_3 = permute_3(permutations_2, words)
    for i in permutation_3:
        print(i)

if __name__ == '__main__':
    main()