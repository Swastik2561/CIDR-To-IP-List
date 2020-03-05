from netaddr import IPNetwork
import sys

def main():
    if(len(sys.argv) != 2):
        print("USAGE: python cidrtoip.py <Filename>\n")
        exit(0)
    else:
        try:
            f = open(str(sys.argv[1]),"r")
            iplist = f.read().split("\n")
            iplist.pop()
            #print(iplist)
            for iprange in iplist:
                for ip in IPNetwork(str(iprange)):
                    print('%s' % ip)
        except:
            print("Filename Not found\nPlease place the file in the current directory\n")
main()
