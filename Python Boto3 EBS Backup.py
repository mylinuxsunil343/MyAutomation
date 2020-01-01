import boto3
import collections
import datetime

ec = boto3.client('ec2')

reservations = ec.describe_instances(
        Filters=[
            {'Name': 'tag-key', 'Values': ['Name', 'sunil']},
        ]
    ).get(
        'Reservations', []
    )

instances = sum(
        [
            [i for i in r['Instances']]
            for r in reservations
        ], [])

print ("Found %d instances that need backing up" % len(instances))
to_tag = collections.defaultdict(list)

for instance in instances:
        try:
            retention_days = [
                int(t.get('Value')) for t in instance['Tags']
                if t['Key'] == 'Retention'][0]
        except IndexError:
            retention_days = 2
for dev in instance['BlockDeviceMappings']:
        if dev.get('Ebs', None) is None:
                continue
        dev_name = dev['DeviceName']
        if dev_name=='/dev/sdf':
            vol_id = dev['Ebs']['VolumeId']
            print ("Found EBS volume %s, device name :%s on instance %s" % (
                vol_id, dev_name, instance['InstanceId']))

today = datetime.date.today()
today = today.strftime('%m_%d_%Y')
for names in instance['Tags']:
    if names['Key']=='Name':
        snap_name = names['Value']+ '_' + str(today)
print ("Found EBS volume %s, device name :%s on instance %s to be and snap name to be %s" % (
                vol_id, dev_name, instance['InstanceId'], snap_name))
snap = ec.create_snapshot(
                VolumeId=vol_id,
            )

to_tag[retention_days].append(snap['SnapshotId'])

print ("Retaining snapshot %s of volume %s from instance %s for %d days" % (
     snap['SnapshotId'],
                vol_id,
                instance['InstanceId'],
                retention_days,
))


for retention_days in to_tag.keys():
        delete_date = datetime.date.today() + datetime.timedelta(days=retention_days)
delete_fmt = delete_date.strftime('%Y-%m-%d')
print ("Will delete %d snapshots on %s" % (len(to_tag[retention_days]),
delete_fmt))
ec.create_tags(
            Resources=to_tag[retention_days],
            Tags=[
                {'Key': 'DeleteOn', 'Value': delete_fmt},
                {'Key': 'Name', 'Value': snap_name}
            ]
        )

