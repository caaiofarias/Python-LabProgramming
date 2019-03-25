pi = 3.14
while True:
    try:
        vol = float(input())
        raio = float(input())/2
        area = pi*(raio**2)
        altura = vol/area
        print("ALTURA = %.2f"%(altura))
        print("AREA = %.2f"%(area))
    except:
        break
