nombre_lista=["nombre",1845,True]
print(nombre_lista)

fbk=['facebook',2449,True]

twt=['twitter',339,False]

ig=['intagram',1000,True]

jyt=['youtube',2000,True]

linke=['linke',663,True]

print("-----------------------------------------------------------------------")

nombre_redes=['facebook','twitter','intagram','youtube','linke']
print(nombre_redes)
print(nombre_redes[0])
print(nombre_redes[2:5])
print(nombre_redes[-3])



print("-----------------------------------------------------------------------")
nombre_redes.append("rojo")
print(nombre_redes)


print("-----------------------------------------------------------------------")
fbk.append(2005)
twt.append(2010)
ig.append(2005)
jyt.append(2009)
linke.append(2008)

print(twt)

print("-----------------------------------------------------------------------")

fbk.remove(2449)
twt.remove(339)
ig.remove(1000)
jyt.remove(2000)
linke.remove(663)

print(fbk)
print(twt)
print(ig)
print(jyt)
print(linke)

print("-----------------------------------------------------------------------")

print(nombre_redes)