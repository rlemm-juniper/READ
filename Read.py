from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable

dev = Device('192.168.0.1')
dev.open()
route_table = RouteTable(dev)
route_table.get()
print route_table.keys()

dev.close()

