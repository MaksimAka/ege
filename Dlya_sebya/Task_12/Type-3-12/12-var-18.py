def is_prime(num):
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0:
            return False
    return True

for n in range(1, 1000):
    st = '>' + '0'*15 + '1'*n + '2'*15

    while '>0' in st or '>1' in st or '>2' in st:
        st = st.replace('>0', '22>', 1)
        st = st.replace('>1', '2>', 1)
        st = st.replace('>2', '1>', 1)

    st = st[:-1]
    if is_prime(sum(map(int, st))):
        print(n)
        break



