__author__ = 'tianjiwei'

# ==========================================
# To generate the graph of the user
# ==========================================

import csv
import networkx as nx
import matplotlib.pyplot as plt

#to get the list of macaddress where the status is "ASSOCIATED"
reader = csv.reader(open('./b.csv', 'r'))
mac = []  # the list of the macaddress; as nodes

reader.next()

try:
	for week, status, asstime, period, location, duration, client_mac, null in reader:
		if client_mac not in mac:
			mac.append(client_mac)
except Exception:
	print 'error'

#print(mac)
print(len(mac))

#to generate the graph, the nodes are from the list(mac)
g = nx.Graph()
g.add_nodes_from(mac)

#to draw the network
nx.draw_random(g, node_size=5)
#nx.draw(g, node_size=5)

plt.show()
