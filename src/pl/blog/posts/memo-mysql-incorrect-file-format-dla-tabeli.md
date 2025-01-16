---
title: "memo: mysql + Incorrect file format dla tabeli"
date: 2009-08-10T12:56:57
tags: ["memo", "mysql"]
---
Gdy zwykły **repair** nie pomaga można zarzucić:

```sql
repair table TABLENAME use_frm
```
