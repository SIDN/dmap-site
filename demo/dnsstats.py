#Unique  ASes IPs, Unique ASes
#we use python to help in handling the json fields stored on postgres

import json
import psycopg2
import sys

def connect():

    conn_string = "host='94.198.159.199' port=5432 dbname='crawldbrsc' user='giovane' "
    # connect
    conn = psycopg2.connect(conn_string)
    #print(conn)
    # create a and return
    return  conn



# main code
connection=connect()
# connect
cursor = connection.cursor()

# create set for resulst
asv4= set()
nsv6= set()
ipv4= set()
ipv6 = set()
asv6= set()
nsv4 = set()
outfile=open('/tmp/listipv4.csv','w')
# send queries now
cursor.execute("select dns_ns from crawl_result_dns   where crawl_run=67 and ip_version=4 and crawl_status=0 "  )

result = cursor.fetchall()
#print(result)
# now the data structure is a bit nexted
# result is a list

for k in result:

    # each elemtent in a list is a tuple
    for y in k:
        # each y now is another list
        if y is not None:

            for w in y:
                # now, ewach w is finally a dict
                # whe then add it to the sets
                counter=0
                if w is not None:
                    nsv4.add(w['name'].lower())

                    # each ns may have multipel addresses, so we need to loop once more

                    for t in w['addresses']:
                        asv4.add(t['asn'])
                        ipv4.add(t['address'].strip())



cursor.close()

print("IPv4 Stats:\n")
print("Unique NSes V4: " + str(len(nsv4)))
print("Unique ASv4: " + str(len(asv4)))
print("Unique IPv4: " + str(len(ipv4)))


#ipv6 now


cursorv6=connection.cursor()
cursorv6.execute('select dns_ns from crawl_result_dns   where crawl_run=67 and ip_version=6 and crawl_status=0' )

result = cursorv6.fetchall()
#print(result)
# now the data structure is a bit nexted
# result is a list

for k in result:

    # each elemtent in a list is a tuple
    for y in k:
        # each y now is another list
        if y is not None:

            for w in y:
                # now, ewach w is finally a dict
                # whe then add it to the sets
                if w is not None:
                    nsv6.add(w['name'].lower())

                    # each ns may have multipel addresses, so we need to loop once more

                    for t in w['addresses']:
                        asv6.add(t['asn'])
                        ipv6.add(t['address'])


print("\nIPv6 Stats:\n")
print("Unique NSes V6: " + str(len(nsv6)))
print("Unique ASv6: " + str(len(asv6)))
print("Unique IPv6: " + str(len(ipv6)))
cursorv6.close()
connection.close()
