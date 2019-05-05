import socket

def port_service(lower, upper):
    i = lower
    while i <= upper:
        try:
            s = socket.getservbyport(i)
            print("port: {} service: {}".format(i, s))
            i += 1
        except OSError:
            i += 1
    print("Port service list complete for range {} to {}".format(lower, upper))
            
    
if __name__ == '__main__':
    choice = input("Enter your own port range? > ")
    if "y" in choice:
        lowbound = input("Enter your lower bound > ")
        upbound = input("Enter your upper bound > ")
        try:
            port_service(int(lowbound), int(upbound))
        except OverflowError:
            print("You have entered a port outside of the acceptable range 0-65535.")
        except ValueError:
            print("You have entered a non-integer port.")
    else:
        port_service(0, 200)