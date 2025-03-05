print('H W L N')
for H in 0,1:
  for W in 0,1:
       for L in 0,1:
           for N in 0,1:
               f = (not(H <= L)) <= ((not(W <= N)) and H)
               if not f:
                   print(H,W,L,N)
