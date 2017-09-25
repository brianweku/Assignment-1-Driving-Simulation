answer='yes'

while answer == "yes":
#given:
    vi=0
    t=int(input("input time: "))
    a=int(input("input acceleration: "))
    distance=int(input("input distance: "))
#formula:
    d=vi*t+ (0.5*a)*((t**2))
    v=vi+a*t

    for i in range(t+1):
        d=vi*i+ 0.5*a*i**2
        f=int(d/10)
        print("Duration: "+str(i)+ " Distance: "+"*"*f)
    if v > 60:
        print("The person went over the speed limit.(Max speed was "+str(v)+" m/s.)")
    else:
        print("The person did not go over the speed limit.(Max speed was "+str(v)+" m/s.)")

    if distance > d:
        print("The person did not reach the destination.(reached "+str(d)+" m.)")
    if distance <= d:
        print("The person reached the destinantion.(reached "+str(d)+" m.)")
    answer=input("continue or not(yes/no): ")
print("thankyou")
