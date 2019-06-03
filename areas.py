def areacirculo():
    try:
        radio=float(input('¿Radio del círculo?'))
        PI=3.14159
        area=PI*radio**2
        print('El área del círculo es=',area)
    except:
        print('Error,has introducido algún valor no numérico')

areacirculo()
