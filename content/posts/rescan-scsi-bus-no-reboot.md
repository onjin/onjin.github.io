---
title: "Rescan SCSI bus (no reboot)"
date: 2012-07-05T08:16:42
slug: blog20120705rescan-scsi-bus-no-reboot
tags: ["linux","tools"]
cover: /img/cover-servers1.jpg
---


Just self memo. How to attach new SCSI disk without reboot (debian):

{{< highlight bash >}}

    # check what hosts do you have
    ls /sys/class/scsi_host
    host0 host1 host2 host3

    # change 'host0' to 'host1' or any next number that you need
    echo "- - -" > /sys/class/scsi_host/host0/scan

{{< /highlight >}}

# and done


{{< highlight bash >}}
    fdisk -l
{{< /highlight >}}
