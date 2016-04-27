import boto.ec2
import optparse

parser = optparse.OptionParser()
parser.add_option('-r','--region',help='List the security group', dest='region', default ='us-east-1')
(opts, args) = parser.parse_args()
conn = boto.ec2.connect_to_region(opts.region)
reservations = conn.get_all_reservations()
instances = [i for r in reservations for i in r.instances]
for instance in instances:
    if instance.state.lower() != 'terminated' or instance.state.lower() != 'stopped':
     	name = instance.tags['Name'].lower()
     	ips = instance.ip_address
    	print " %s   \t  ---->   \t  %s " % ( name, ips )
