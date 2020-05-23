import sys
p_h1=0.1
p_h2=0.2
p_h3=0.4
p_h4=0.2
p_h5=0.1
p_C_h1=1
p_L_h1=0
p_C_h2=0.75
p_L_h2=0.25
p_C_h3=0.5
p_L_h3=0.5
p_C_h4=0.25
p_L_h4=0.75
p_C_h5=0
p_L_h5=1
string=sys.argv[1]
P_H1_Q=[p_h1]
P_H2_Q=[p_h2]
P_H3_Q=[p_h3]
P_H4_Q=[p_h4]
P_H5_Q=[p_h5]
P_Q_next_C=[p_C_h1*p_h1+p_C_h2*p_h2+p_C_h3*p_h3+p_C_h4*p_h4+p_C_h5*p_h5]
P_Q_next_L=[p_L_h1*p_h1+p_L_h2*p_h2+p_L_h3*p_h3+p_L_h4*p_h4+p_L_h5*p_h5]
f=open("result.txt","w")
f.write("Observation sequence Q: "+string)
f.write("\n")
f.write("Length of Q: "+str(len(string)))
for i in range(0,len(string)):
	f.write("\n")
	f.write("\n")
	f.write("After Observation "+str(i+1)+" = "+string[i]+":")
	f.write("\n")
	f.write("\n")
	if(string[i]=="C"):
		pth1=p_C_h1*P_H1_Q[i]/P_Q_next_C[i]
		pth2=p_C_h2*P_H2_Q[i]/P_Q_next_C[i]
		pth3=p_C_h3*P_H3_Q[i]/P_Q_next_C[i]
		pth4=p_C_h4*P_H4_Q[i]/P_Q_next_C[i]
		pth5=p_C_h5*P_H5_Q[i]/P_Q_next_C[i]
	else:
		pth1=p_L_h1*P_H1_Q[i]/P_Q_next_L[i]
		pth2=p_L_h2*P_H2_Q[i]/P_Q_next_L[i]
		pth3=p_L_h3*P_H3_Q[i]/P_Q_next_L[i]
		pth4=p_L_h4*P_H4_Q[i]/P_Q_next_L[i]
		pth5=p_L_h5*P_H5_Q[i]/P_Q_next_L[i]
	Pt1c=p_C_h1*pth1+p_C_h2*pth2+p_C_h3*pth3+p_C_h4*pth4+p_C_h5*pth5
	Pt1l=p_L_h1*pth1+p_L_h2*pth2+p_L_h3*pth3+p_L_h4*pth4+p_L_h5*pth5
	f.write("P(h1 | Q) = "+str(pth1))
	f.write("\n")
	f.write("P(h2 | Q) = "+str(pth2))
	f.write("\n")
	f.write("P(h3 | Q) = "+str(pth3))
	f.write("\n")
	f.write("P(h4 | Q) = "+str(pth4))
	f.write("\n")
	f.write("P(h5 | Q) = "+str(pth5))
	f.write("\n")
	f.write("\n")
	f.write("Probability that the next candy we pick will be C, given Q: "+str(Pt1c))
	f.write("\n")
	f.write("Probability that the next candy we pick will be L, given Q: "+str(Pt1l))
	P_H1_Q.append(pth1)
	P_H2_Q.append(pth2)
	P_H3_Q.append(pth3)
	P_H4_Q.append(pth4)
	P_H5_Q.append(pth5)
	P_Q_next_C.append(Pt1c)
	P_Q_next_L.append(Pt1l) 
f.write("\n")