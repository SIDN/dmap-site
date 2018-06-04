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
startv4= set()
nsv6= set()
ipv4= set()
ipv6 = set()
startv6= set()
nsv4 = set()

# send queries now
cursor.execute("select smtp_hosts from crawl_result_smtp   where crawl_run=67 and ip_version=4 and crawl_status=0" )

result = cursor.fetchall()
#print(result)
# now the data structure is a bit nexted
# result is a list

for k in result:

    # each elemtent in a list is a tuple
    for y in k:
        # each y now is another list
        if y is not None:

            w=json.loads(y)


            #w is a list of individual MX servers

            if w is not None:
                #l is each individual MX
                for l in w:

                    nsv4.add(l['name'].lower())

                # each ns may have multipel addresses, so we need to loop once more

                    for t in l['smtpHostIPs']:
                        ipv4.add(t['ip'])
                        if t['startTlsEnabled']==True:
                            startv4.add(l['name'].lower())

cursor.close()

print("IPv4 Stats:\n")
print("Unique SMTP V4: " + str(len(nsv4)))
print("Unique IPv4: " + str(len(ipv4)))
print("Unique STARTLS: " + str(len(startv4)))


#ipv6 now


cursorv6=connection.cursor()
cursorv6.execute("select smtp_hosts from crawl_result_smtp   where crawl_run=67 and ip_version=6 and crawl_status=0")

result = cursorv6.fetchall()
#print(result)
# now the data structure is a bit nexted
# result is a list

for k in result:

    # each elemtent in a list is a tuple
    for y in k:
        # each y now is another list
        if y is not None:

            w=json.loads(y)

            if w is not None:
                for l in w:

                    nsv6.add(l['name'].lower())

                # each ns may have multipel addresses, so we need to loop once more

                    for t in l['smtpHostIPs']:
                        ipv6.add(t['ip'])
                        if t['startTlsEnabled']==True:
                            startv6.add(l['name'].lower())

cursor.close()

print("\nIPv6 Stats:\n")
print("Unique SMTP V6: " + str(len(nsv6)))
print("Unique IPv6: " + str(len(ipv6)))
print("Unique STARTLS: " + str(len(startv6)))

cursorv6.close()
connection.close()
