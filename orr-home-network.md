**Thu Dec 30 13:55:46 PST 2010*8

Reconfiguring Moms home network after the verizon upgrade.
So she has a verizon device managing her internet connection.

Sat Dec 29 11:26:51 PST 2012

After Mom got her ipad, I set up a new wifi router in the front room.
netgear wndr3700v3

wireless 2.4G
ssid: quiltingbee
passphrase:  zelyanitsa

wireless 5G
ssid: quiltingbee5
same passphrase

guest network is shut off

The router is at ip address: 192.168.5.1
the admin password to the router is: mx8kgv2GUlCA

password
security question 1: name of the first school I attended?
South Bay Christian

q2: what is my best friend's first name?
John

----

**Fri Dec 26 12:35:49 PST 2014**

Mom got a new router from verizon.  I set it up.

The router is an: ActionTec MI424WR rev 1

Admin interface on the router was initially configured as:

username: admin
password: W!^@=!j8

but that password did not work at all.  So I called verizon tech support.

the Verizon tech reset the password to:
password: orr1home

but that failed.  So he agreed to ship out a new router.

wireless access on the ActionTec router:
ssid: TNQTD
password: BKRQSVBW34LWFLKJ


discover the IP address where the 2 wifi routers are now:

    vega-> fping -g 192.168.1.1/24
    192.168.1.1 is alive                router
    192.168.1.3 is alive                vega
    192.168.1.11 is alive               front room wndr3700; mac: 20:E5:2A:25:1F:C4
    192.168.1.4 is alive
    192.168.1.100 is alive
    192.168.1.101 is alive

The front room wndr3700

ip addr:  192.168.1.11
username: admin
password: mx8kgv2GUlCA

the back room router was showing weird results from ping, and not responding as it should
I conclude it died.

When the new router comes in, I need to replace the current model with the new one.

then configure the ssid to quiltingbee etc.
then configure the printer to talk via the quiltingbee network.
