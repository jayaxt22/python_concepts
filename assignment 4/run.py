runs=int(input("enter runs= "))
over,decover= map(int,input("enter time in hour and minutes = ").split("."))
balls=over*6+decover

rr= runs/(balls/6)

print("totalballs=",balls,"\n runrate",rr)