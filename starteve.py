from eve import Eve
import sys

if __name__ == '__main__':
    
    app = Eve()
    app.run(host=sys.argv[1], port=sys.argv[2]) # Command to start Eve Server:
                                                # python3 startEve.py 192.168.1.232 5000
                                                # python3 startEve.py $host $port