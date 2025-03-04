ans = []
for n in range(3, 10000):
    st = '5' + '2'*n

    while '72' in st or '522' in st or '2222' in st:
        st = st.replace('72', '2', 1)
        st = st.replace('522', '27', 1)
        st = st.replace('2222', '5', 1)

    summ = sum(map(int, st))
    if summ == 63:
        ans.append(n)

print(min(ans))

#Ответ: 186