# Week 1

## IP Address

165.132.126.159 is a IPv4 32 bit (4 byte) address format each byte are seperate by `.`.

8 bits is composed of `00000000` ~ `11111111` = `0` ~ `255`

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|

*note: 8 bits = 1 byte = 1 octet*

### IP Address of the PC

`165.132.126.159` (Decimal form) is equal to `10100101.10000100.01111110.10011111` (Binary form)

### IP Address Assignments

Ip address are assign to each interface -> Computer or smartphone may have multiple interfaces and therefore may need multiple IP address. For example, Smartphone can have 2G, 3G, Wifi and bluetooth.

### Subnet Mask

Subnet Mask is used to **mask (filter)** the IP address to esily determine if the packet belongs to this subnet or not. 

The subnet Mask can be used to find the Subnet size. in the example below the number of IP address in this subnet is `1024 = 2^10` (this is from 10 zeros). But not all addresses can be used for Clients?
```
255.255.252.0 = 11111111.11111111.11111100.00000000
```

The internet is divided into Subnets and Subnets are divided into smaller Subnets.

Subnet Mask is based on the size of the Subnet the Client is connected to.

IPv4 Subnet Mask is formed by 32 bits
* 1s or 0s in sequence, from Left(MSB) to Right(LSB) -> Most to Least significant Bit

### Default Gateway

Defaut Gateway is the dedicated Inter Router that will send and recieve all Internet IP packet for this PC. PC will access the internet through this gateway (recieve and send all IP packet)

### DNS (Domain Name server)

DNS is a converts hostnames into IP address. For example, `www.facebook.com` (hostname) -> `173.252.110.27` (IP address)


## DHCP (Dynamic Host Configuration Protocal)

DHCP enable a computer to automatically contact the local DHCP Server and request for an IP address and networking parameters to connect to the internet.





##
