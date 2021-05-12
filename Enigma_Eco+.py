##### César #####
texte1 ="kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
def cesar(texte,cle):
    """Cette fonction a pour but de crypter/décrypter un texte via l'alogrithme de césar"""
    resul= "" # sortie du texte
    for lettre in texte:
        tpxt =ord(lettre) # variable temporaire de stockage de lettre
        if tpxt == 32 or tpxt == 46 or tpxt == 58: #Pour garder la ponctuation
            pass
        else:
            tpxt -= 97
            tpxt = (tpxt + cle)%26
            tpxt += 97
        resul += (chr(tpxt))
    return resul

print(cesar(texte1,1))


##### Fréquence #1 #####
texte2 ="gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."

def anlyfr(texte):
    """Cette fonction a pour but de calculer le nombre de répétition d'une lettre dans un texte"""
    sr ="" # sortie du résultat
    vltr = 97 # 1er lettre a analyser cette variable augmentera au fil de l'éxécution pour changer de lettre et analyser toutes les lettres
    while vltr < 123:
        cmp = texte.count(chr(vltr))
        if cmp ==0:
            vltr +=1
        else:
            sr += (chr(vltr)+" "+str(cmp)+"\n")
            vltr +=1
    return sr
    

print(anlyfr(texte2))
##### Definition de liste de réf #####
hz = [['a','9'],['c','1'],['d','5'],['f','3'],['g','4'],['i','7'],['k','i'],['l','h'],['m','g'],['n','a'],['o','r'],['q','p'],['s','o'],['u','t'],['v','c'],['w','f'],["x","e"],['y','u'],['4','l'],['5','n'],['7','s'],['1','d'],['3','m'],['9','z']]
# Liste crée a partir de la sortie de la fonction précédente.
# la lettre de référence de 'a' été remplacé par 'z' car si on suivait l'article wikipédia de référence on obtiendra b
# Certaines lettres deviennent des chiffres pour éviter qu’elles soient redécrypté leur décryptions se fait à la fin.


##### Fréquence 2 : electric boogaloo #####
def chngr(texte):
    varcl = 0 # variable de compte
    while varcl < 24:
        texte=texte.replace(hz[varcl][0],hz[varcl][1])
        varcl +=1
    return texte

print(chngr(texte2))


##### Vigenère #Mdp =xova #####
motpasse = ['x','o','v','a']
texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
def viggen(texte,mdp):
    crflm = 0 # compteur qui a pour but de se balader dans le mot de passe pour sélectionner le bon caractére
    resul= "" # résultat final
    for lettre in texte:
        tpxt =ord(lettre)
        if tpxt == 32 or tpxt == 44 or tpxt == 63 or tpxt == 46 or tpxt == 39 :
            crflm +=1
        else:
            tpxt -= 96
            vac = mdp[crflm%4] # VAC est une variable qui a pour but de stocker temporairement la lettre du mot de passe
            vac = ord(vac)-96
            tpxt += vac
            tpxt = tpxt % 26 
            tpxt += 96
            if tpxt == 96:
                tpxt +=26
            crflm +=1
        resul += (chr(tpxt))
    return resul

print(viggen(texte3,motpasse))


##### Vigenère + Mirroir #####
# Pas fini

motpasse2 = ['','','','']
textefin = "jeqeqecvnf suozvb jfk muj dfjr fmy rvuqsk ve itajtd mifwz nnrt imtrvp zuh srzmzbqz tepr zn tmsnirt imtrvp nec hw dzpqj tjf pdecpr zl jr ptejnt ekpb iu b iiuyu iy ijz surg rjs ttsn votp ac hw rzpuen jozw rvwdvx jbo nirscyjv fi svmkyw ve iaflss yie te teffvv'u riznxjzvv jfk nelrhtjrk dh sivdvjvve yi cvb à jffrds tdp rvwdv sebr onvnqsy zvp zuhjwiM le wmifo wiezib nec triot qmjvr'c onrwz memfqg srq wdaietsq vk"
#print(viggen(textefin,motpasse2)) 
def reflec(texte):
    """focntion qui retourne un texte"""
    texte = texte[::-1]
    return texte
#print(reflec(textefin))

#textert = (reflec(textefin)) 
#print(viggen(textert,motpasse2)) 

