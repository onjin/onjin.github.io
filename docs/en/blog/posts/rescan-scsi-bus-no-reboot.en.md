---
title: "Rescan SCSI bus (no reboot)"
date: 2012-07-05T08:16:42
slug: blog20120705rescan-scsi-bus-no-reboot
tags: ["linux","tools"]
---


Just self memo. How to attach new SCSI disk without reboot (debian):

```bash

# check what hosts do you have
ls /sys/class/scsi_host
host0 host1 host2 host3

# change 'host0' to 'host1' or any next number that you need
echo "- - -" > /sys/class/scsi_host/host0/scan

```

**and done ...**


```bash
$ fdisk -l
```
