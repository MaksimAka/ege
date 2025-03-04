st = '22' + '1'*2023 + '22'
while '221' in st or '112' in st:
    st = st.replace('11', '1', 1)
    if '21' in st:
        st = st.replace('21', '12', 1)
    else:
        st = st.replace('12', '1', 1)

print(st)

#Ответ: 121222