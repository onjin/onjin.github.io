---
title: "memo: mysql + Incorrect file format dla tabeli"
date: 2009-08-10T12:56:57
slug: blog20090810memo-mysql-incorrect-file-format-dla-tabeli
tags: ["memo", "mysql"]
---
Gdy zwykły <strong>repair</strong> nie pomaga można zarzucić:

{{< highlight sql >}}
    repair table TABLENAME use_frm
{{< /highlight >}}
