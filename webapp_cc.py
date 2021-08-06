import streamlit as st
st.title('Welcome to useful app websites')
html_temp = """
	<div style="background-color:tomato;padding:3px">
	<h2 style="color:white;text-align:center;"> Gates Dashboard </h2>
	</div>
	"""
st.markdown(html_temp, unsafe_allow_html=True)
prg = st.radio("Select your program", ("CCode", "Aud2txt", "Test"))

if prg == "CCode":
    lalb = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    salb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    spl_let = ['!', '@', '#', '$', '%', '^', '&',
               '*', '(', ')', '_', '+', '{', '}', '|']

    def encrypter(endata, enkey):
        message = []
        final = []
        for k in endata:  # HELLO
            message.append(k)  # storing the entered data as by user as LIST
        for l in message:
            try:
                if l in salb:
                    a = salb.index(l)
                    b = (a+enkey) % 26
                    c = salb[b]
                    final.append(c)
                elif l in lalb:
                    a = lalb.index(l)
                    b = (a+enkey) % 26
                    c = lalb[b]
                    final.append(c)
                else:
                    a = spl_let.index(l)
                    b = (a+enkey) % 26
                    c = lalb[b]
                    final.append(c)
            except ValueError:
                final.append(l)
        return final

    def decrypter(dedata, dekey):
        message = []
        final = []
        for k in dedata:
            message.append(k)  # storing the entered data as by user as LIST
        for l in message:
            try:
                if l in salb:
                    a = salb.index(l)
                    b = (a-dekey) % 26
                    c = salb[b]
                    final.append(c)
                elif l in lalb:
                    a = lalb.index(l)
                    b = (a-dekey) % 26
                    c = lalb[b]
                    final.append(c)
                else:
                    a = spl_let.index(l)
                    b = (a+enkey) % 26
                    c = lalb[b]
                    final.append(c)
            except ValueError:
                final.append(l)
        return final

    st.write("Select a Choice from below to process your data")
    c = st.radio("", ("1. Encrypter", "2. Decrypter"))
    if c == "1. Encrypter":
        userdata1 = st.text_input("Enter the text you want to Encrypt: ")
        key1 = st.number_input(
            "Select the key code to encrypt the above text", step=1, max_value=10, min_value=1)
        coded = encrypter(userdata1, key1)
        st.success("".join(coded))
    elif c == "2. Decrypter":
        userdata2 = st.text_input("Enter the text you want to Decrypt: ")
        key2 = st.number_input(
            "Select the key code to decrypt the above text", step=1, max_value=10, min_value=1)
        coded = decrypter(userdata2, key2)
        st.write("Decrypted Text is")
        st.success("".join(coded))
    else:
        st.warning("Enter a valid Choice")


elif prg == "Aud2txt":
    st.write("Aud2Txt")
else:
    st.write("Test")
