
charcount = 64
alphanumdict = {}

for i in range(1,27):
    alphanumdict[chr(i + charcount)] = i - 1

pub_key_n = int(input("Enter \'n\' of public key: "))
pub_key_e = int(input("Enter \'e\' of public key: "))
decrypt = str(input("Do you want to decrypt message? y/n: "))

if decrypt == "y":
    priv_key_d = int(input("Enter \'d\' of private key: "))
    encrypted_message = str(input("Enter encrypted message with spaces between numbers: "))

    encrypted_list = encrypted_message.split()

    encrypted_list2 = []
    for i in range(len(encrypted_list)):
        encrypted_list2.append(int(encrypted_list[i]))

    decrypt = []
    for i in range(len(encrypted_list2)):
        decrypt.append(((encrypted_list2[i])**priv_key_d) % pub_key_n)

    inv_alphanumdict = {}
    for k, v in alphanumdict.items():
        keys = inv_alphanumdict.setdefault(v, [])
        keys.append(k)

    decrypted_msg = []
    for i in range(len(decrypt)):
        decrypted_msg.append(inv_alphanumdict.get(decrypt[i]))

    decrypted_msg_final = []
    for i in range(len(decrypted_msg)):
        decrypted_msg_final.append(decrypted_msg[i][0])

    print("The decrypted message is: ", end='')
    print(decrypted_msg_final)



else:
    ltr_to_num_list = []
    message = str(input("Enter message in capital letters without spaces: "))
    for i in range(len(message)):
        ltr_to_num_list.append(alphanumdict.get(message[i]))
    encrypt = []
    for i in range(len(ltr_to_num_list)):
        encrypt.append((ltr_to_num_list[i]**pub_key_e) % pub_key_n)
    print("The encrypted message is: ", end='')
    print(encrypt)
