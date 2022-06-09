def compoundinterest(p,r,t):
	ci=p*(pow((1 + r / 100), t))
	return ci;
p=float(input("Enetr a principle amount:"));
r=float(input("Enter a rate of interest:"));
t=float(input("Enter the number of years:"));
ci=compoundinterest(p,r,t);
print("Compound interest :{}".format(ci));
