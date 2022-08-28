# Gather

Gather is a meeting app focused on time management discipline.


## Install Requirements

```
pip install requirements.txt

```


## Django Admin details

username: akinwumi@gmail.com
password: kal



## Create a meeting

To create a meeting, users needs to be logged in, click on HOST in the navbar or go to meetings on the user dashboard.

Only registered users can create a meeting. Meetings must be unique, hence the generation of meeting IDs automatically. This meeting Id will be the gateway for guests and users to join.


### It is important to change the timezone to your location as the default is set to "Africa/Lagos"


## Join a meeting

All that is required to start a meeting is the meeting ID that will be shared by the host after creating a meeting and the name of the guest. You need not bother about name if you are a registered user.

A meeting link is also generated, this is the fastest way to join a meeting.



#### meeting do not start until the time set

#### Meetings ends immediately the time hits duration set by the host, all users would be logged out of the meeting automatically