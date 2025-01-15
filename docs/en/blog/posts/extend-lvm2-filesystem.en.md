---
title: "extend lvm2 filesystem"
date: 2012-04-27T10:30:44
slug: blog20120427extend-lvm2-filesystem
tags: ["hosting","tools"]
---

Just self memo

```bash

# Added new physical partition /dev/sda3
# create a physical volume out of it
$ pvcreate /dev/sda3


# Now, add it to the volume group
#that my logical volume is on
$ vgextend VolGroup00 /dev/sda3


# Now that the volume group has more
# disk space, the logical volume can grow
$ lvextend -L+11G /dev/VolGroup00/LogVol00


# Ok, last of all, I want to filesystem to
# recognize that more space is available
$ fsadm resize /dev/VolGroup00/LogVol00

# sweet, I have more space now
$ df -h
```
