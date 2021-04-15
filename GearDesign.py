#code for gear design (Works for Spur and Helical gears)

import math
from math import *
#Take Inputs
print("Shaiman \n\nProgram for gear design (Works for Spur and Helical gears)")
sutp = float(input(" Sut_Pinion : "))
sutg = float(input(" Sut_Gear : "))
p= float(input(" Z_pinion : "))
g= float(input(" Z_gear: "))
hel= float(input(" Is gear Helical? (1 for Yes / 0 for No ) : "))
bhn= float(input(" Hardness in BHN : "))
psy=int(input(" Friction Angle is : "))
alpha=int(input(" Helix angle is : "))
ca=cos(alpha*0.017453)                                                     #cos(25)
ca2=pow(ca,2)                                                       #cos^2(25)
ca3=pow(ca,3)                                                       #cos^3(25)



if hel==1:                                                          #code for helical
    zp=p/ca3
    zg=g/ca3

    # calculations

    # Which one is weak?
    print(zp)
    print(zg)
    sbp = sutp/3
    print( 'Bending Strength Pinion ',sbp)

    sbg = sutg/3
    print( 'Bending Stre5ngth Gear ',sbg)

    yp = 0.484-(2.87/zp)
    print( 'Y_p ', yp)

    yg = 0.484-(2.87/zg)
    print( 'Y_g ',yg)

    b = sbp * yp
    print( 'Sigma_p * Y_p',b)
    a = sbg * yg
    print( 'Sigma_g * Y_g', a)

    print(zp)
    print(zg)
    print(ca3)

    if  a>b:
        print("pinion is weak")
        sigma_b_Y=b
        nopin=p
    else:
        print("gear is weak")
        sigma_b_Y=a
        nopin=g

    #Failure criteria

    #Bending
    sb = sigma_b_Y*10 # *Mn * 10Mn
    print("Sb :",sb," Mn_pow_2")

    #Wear
    dp=nopin/ca                        #Mn excluded
    print("dp: ",dp)
    q=(2*g)/(p+g)
    print("q:",q)
    bhn_by_100=(bhn/100)
    sq_bhn_by_100=pow(bhn_by_100,2)
    k=0.16*sq_bhn_by_100
    print("K",k)
    sw=(dp*10*q*k)/ca                  #Mn excluded
    print("Sw: ",sw," Mn_pow_2")

    #result
    if sb>sw:
        print("\n\nWear failure\n")
        fc=sw
    else:
        print("\n\nBending failure\n")
        fc=sb

    #By velocity Factor Approach
    power=float(input("Power (watt) : "))
    rpm=float(input("Speed in RPM : "))
    pi=22/7
    v=(pi*dp*rpm)/60000
    print("v :",v ," * Mn m/s")
    pt=power/v
    print("Pt : ",pt,("/Mn"))
    vel=float(input("Assume velocity in m/s : "))
    cs=float(input("Input C_s : "))
    cv=5.6/(5.6+math.sqrt(vel))
    print("C_v is : ",cv)
    peff=(cs*pt)/cv
    print("Peff : ",peff," / Mn")

    fos=float(input("Input FOS : "))
    fract=(peff*fos)/fc
    mn=pow(fract,0.3333)

    print("Mn : ", mn)
    m=float(input("Enter M_n :"))
    fc=fc*m*m
    print("Failure Stress is : ",fc)
    pt=pt/m
    print("Pt is : ",pt)
    v=v*m
    print("v is : ",v)
    peff=peff/m
    print("peff is : ",peff)
    dp=p*m
    print("dp is : ",dp)
    dg=g*m
    print("dg is : ",dg)

    c=float(input("Input C : "))
    print("C : ",c)


    grade=int(input("Enter Grade of m/c (4 or 8) : "))
    print("For grade ",grade, ", \n")



    if grade==4:
        eg=(3.2+0.25*(m+0.25*pow(m*g,0.5)))*0.001   #grade4
        print("eg : ",eg)
        ep=(3.2+0.25*(m+0.25*pow(m*p,0.5)))*0.001   #grade4
        print("ep : ",ep)
    else:
            
        eg=(16+1.25*(m+0.25*pow(m*g,0.5)))*0.001   #grade8
        print("eg : ",eg)
        ep=(16+1.25*(m+0.25*pow(m*p,0.5)))*0.001   #grade8
        print("ep : ",ep)

    
    if a<b:
        e=eg
    else:
        e=ep
    print("e : ",e)


    num=21*v*(c*e*10*m*ca2+pt)*ca
    print("num is : ",num)
    den=21*v+pow((c*e*10*m*ca2+pt),0.5)
    print("den is : ",den)
    pdyn=num/den
    print("pdyn is : ",pdyn)
    peff=pt*cs+pdyn
    print("peff is : ",peff)

    newfos=fc/peff
    print("Final Fos is : ",newfos)

    


    
elif hel==0:                                           #for spur gear
    zp=p
    zg=g
     # calculations

    # Which one is weak?



    print("zp is :",zp)
    print("zp is :",zg)
    sbp = sutp/3
    print( 'Bending Strength Pinion ',sbp)

    sbg = sutg/3
    print( 'Bending Strength Gear ',sbg)

    yp = 0.484-(2.87/zp)
    print( 'Y_p ', yp)

    yg = 0.484-(2.87/zg)
    print( 'Y_g ',yg)

    b = sbp * yp
    print( 'Sigma_p * Y_p',b)
    a = sbg * yg
    print( 'Sigma_g * Y_g', a)


    if  a>b:
        print("pinion is weak")
        sigma_b_Y=b
        nopin=p
    else:
        print("gear is weak")
        sigma_b_Y=a
        nopin=g

    #Failure criteria

    #Bending
    sb = sigma_b_Y*10 # *Mn * 10Mn
    print("Sb :",sb," Mn_pow_2")

    #Wear
    dp=nopin                       #Mn excluded
    print("dp: ",dp," * Mn")
    q=(2*g)/(p+g)
    print("q:",q)
    bhn_by_100=(bhn/100)
    sq_bhn_by_100=pow(bhn_by_100,2)
    k=0.16*sq_bhn_by_100
    print("K",k)
    sw=(dp*10*q*k)                  #Mn excluded
    print("Sw: ",sw," Mn_pow_2")

    #result
    if sb>sw:
        print("Wear failure")
        fc=sw
    else:
        print("Bending failure")
        fc=sb


    #By velocity Factor Approach



    power=float(input("Power (watt) : "))
    rpm=float(input("Speed in RPM : "))
    pi=22/7
    v=(pi*dp*rpm)/60000
    print("v :",v ," * Mn m/s")
    pt=power/v
    print("Pt : ",pt,("/Mn"))
    vel=float(input("Assume velocity in m/s : "))
    cs=float(input("Input C_s : "))
    cv=5.6/(5.6*math.sqrt(vel))
    print("C_v is : ",cv)
    peff=(cs*pt)/cv
    print("Peff : ",peff," / Mn")

    fos=float(input("Input FOS : "))
    fract=(peff*fos)/fc
    mn=pow(fract,0.3333)

    print("Mn : ", mn)
    m=float(input("Enter M_n :"))
    fc=fc*m*m
    print("Failure Stress is : ",fc)
    pt=pt/m
    print("Pt is : ",pt)
    v=v*m
    print("v is : ",v)
    peff=peff/m
    print("peff is : ",peff)
    dp=p*m
    print("dp is : ",dp)
    dg=g*m
    print("dg is : ",dg)

    c=float(input("Input C : "))
    print("C : ",c)

    grade=int(input("Enter Grade of m/c (4 or 8) : "))
    print("For grade ",grade, ", \n")



    if grade==4:
        eg=(3.2+0.25*(m+0.25*pow(m*g,0.5)))*0.001   #grade4
        print("eg : ",eg)
        ep=(3.2+0.25*(m+0.25*pow(m*p,0.5)))*0.001   #grade4
        print("ep : ",ep)
    else:
            
        eg=(16+1.25*(m+0.25*pow(m*g,0.5)))*0.001   #grade8
        print("eg : ",eg)
        ep=(16+1.25*(m+0.25*pow(m*p,0.5)))*0.001   #grade8
        print("ep : ",ep)

    
    if a<b:
        e=eg
    else:
        e=ep

    print("e : ",e)


    #Buckingham Equation


    num=21*v*(c*e*10*m*ca2+pt)*ca
    print("num is : ",num)
    den=21*v+pow((c*e*10*m*ca2+pt),0.5)
    print("den is : ",den)
    pdyn=num/den
    print("pdyn is : ",pdyn)
    peff=pt*cs+pdyn
    print("peff is : ",peff)

    newfos=fc/peff
    print("Final Fos is : ",newfos)

print("\n\n\nFinal Gear Parameters : \n")
print("dp is : ",dp)
print("dg is : ",dg)
print("b is : ",10*m)
print("Addendum dia. of pinion is : ",(dp+m))
print("Deddendum dia. of pinion is : ",(dp-1.25*m))
print("Addendum dia. of gear is : ",(dg+m))
print("Deddendum dia. of gear is : ",(dg-1.25*m))
print("\n\nResults by Shaiman\n\n")


