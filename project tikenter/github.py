


from sympy import *

	
	

def coupcoup(k, long):
	
	""""découpe des blocs de longueur long dans une chaine de caractères k et retourne une liste des blocs"""
	
	d , f = 0 , long
	
	
	l = []
	
	while f <= len(k):
		
		l.append(k[d:f])
		
		d , f = f , f + long
		
	
	m = len(k)%long
	
	if m != 0:
		
		l.append(k[len(k)-m:])
	
	return l



def pgcd(a,b):
	
	"""retourne le plus grand dénominateur commun de a et b"""
	
	while (b>0):
		
		r=a%b
		
		a,b=b,r
		
	return a
	
	
	
def pgcde(a, b):
	
	""" pgcd étendu avec les 2 coefficients de bézout u et v
	Entrée : a, b entiers
	Sorties : r = pgcd(a,b) et u, v entiers tels que a*u + b*v = r
	"""
	r, u, v = a, 1, 0
	rp, up, vp = b, 0, 1
	
	while rp != 0:
		q = r//rp
		rs, us, vs = r, u, v
		r, u, v = rp, up, vp
		rp, up, vp = (rs - q*rp), (us - q*up), (vs - q*vp)
	
	return (r, u, v)


import random



def key():
	
	"""retourne un dictionnaire contenant la clé privée et la clé publique sous forme de tuples: {priv:(clé privée),pub:(clé publique)}"""
	
	#choix au hasard de deux entiers premiers (n et q)
	p = random.randrange(1,1000)
	q = random.randrange(1,1000)
	
	while isprime(p)==false:
		p =random.randrange(1,1000)
		
	while isprime(q) is False:
		q = random.randrange(1,1000)

	return p,q	
	#calcul de n et m
a=key()
p=int(a[0])
q=int(a[1])
phi = (int(p)-1)*(int(q)-1)

def key2():
	
	n = p*q
	m = (p-1)*(q-1)

	#recherche de c premier de m (c'est a dire tel que pgcd(m,c)=1 ) et de d = pgcde(m,c) tel que 2 < d < m
	r = 10
	d = 0
	while r != 1 or d <= 2 or d >= m:
		c = random.randrange(1,1000)
		r, d, v = pgcde(c,m)
		
	n, c, d = int(n), int(c), int(d)


	# return {"priv":(n,c), "pub":(n,d)}
	return n,c,d


	
def chiffre(n, c, msg):
	#conversion du message en codes ascii	
	asc = [str(ord(j)) for j in msg]
	#ajout de 0 pour avoir une longueur fixe (3) de chaque code asccii
	for i, k in enumerate(asc):
		if len(k) < 3:		
			while len(k) < 3:
				k = '0' + k
			asc[i] = k
	#formation de blocs de taille inferieure a n (ici blocs de 4)
	ascg = ''.join(asc)
	d , f = 0 , 4
	while len(ascg)%f != 0: #on rajoute eventuellement des 0 a la fin de ascg de maniere a ce que len(ascg) soit un multiple de f
		ascg = ascg + '0'
	l = []
	while f <= len(ascg):
		l.append(ascg[d:f])
		d , f = f , f + 4
	#chiffrement des groupes
	crypt = [str(((int(i))**c)%n) for i in l]
	return crypt
	

	
	
def dechiffre(n, d, *crypt):

	"""*crypt est une liste des blocks à déchiffrer"""
	
	
	#dechiffrage des blocs
	resultat = [str((int(i)**d)%n) for i in crypt]
		
		
	#on rajoute les 0 en debut de blocs pour refaire des blocs de 4
	for i, s in enumerate(resultat):
		
		if len(s) < 4:
			
			while len(s) < 4:
				
				s = '0' + s
			
			resultat[i] = s
		
		
	#on refait des groupes de 3 et on les convertie directement en ascii
	g = ''.join(resultat)
	
	asci = ''
	
	d , f = 0 , 3
	
	while f < len(g):
		
		asci = asci + chr(int(g[d:f])) #conversion ascii
		
		d , f = f , f + 3
	
	
	
	
	return asci
	



#return n,c,d
#def dechiffre(n, d, *crypt):
#def chiffre(n, c, msg):
f= key2()
k=key()

n=f[0]
c=f[1]
d=f[2]
	

# print(f)
# chifreee=chiffre(f[0], f[1], "hajiba")
# print(chifreee)
# dechiffree=dechiffre(f[0], f[2], *chifreee)
# print(dechiffree)
