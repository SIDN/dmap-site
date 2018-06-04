# Unique  ASes IPs, Unique ASes
# we use python to help in handling the json fields stored on postgres

import json
import psycopg2
import sys


def connect():
    conn_string = "host='94.198.159.199' port=5432 dbname='crawldbrsc' user='giovane' "
    # connect
    conn = psycopg2.connect(conn_string)
    # print(conn)
    # create a and return
    return conn


# main code
connection = connect()
# connect
cursor = connection.cursor()

# create set for resulst
asv4 = set()
nsv6 = set()
ipv4 = set()
ipv6 = set()
asv6 = set()
nsv4 = set()
outfile = open('/tmp/listipv4.csv', 'w')
# send queries now
cursor.execute("select domainname, dns_ns from crawl_result_dns   where crawl_run=67 and ip_version=4 and crawl_status=0")

result = cursor.fetchall()
# print(result)
# now the data structure is a bit nexted
# result is a list
counterDict=dict()

for k in result:

    # each elemtent in a list is a tuple
    counter = 0
    tempSet=set()
    counterDict[k[0]] = tempSet
    if k[1] is not None:

        for y in k[1]:
            # each y now is another list
            if y is not None:


                if y is not None:
                    nsv4.add(y['name'].lower())

                    # each ns may have multipel addresses, so we need to loop once more

                    for t in y['addresses']:
                        asv4.add(t['asn'])
                        ipv4.add(t['address'].strip())
                        tempV=counterDict[k[0]]
                        tempV.add(t['address'].strip())
                        counterDict[k[0]]=tempV

        outfile.write(k[0]+","+str(len(counterDict[k[0]]))+ "\n")
cursor.close()

print("IPv4 Stats:\n")
print("Unique NSes V4: " + str(len(nsv4)))
print("Unique ASv4: " + str(len(asv4)))
print("Unique IPv4: " + str(len(ipv4)))

# ipv6 now
outfile.close()

connection.close()
