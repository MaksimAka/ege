ans = []
for n in range(3, 1000):
    st = '3' + '5'*n

    while '25' in st or '355' in st or '555' in st:
        st = st.replace('25', '32', 1)
        st = st.replace('355', '25', 1)
        st = st.replace('555', '3', 1)

    if st.count('2') == 5:
        ans.append(n)
print(max(ans))