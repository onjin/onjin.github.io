---
title: "quiet please !! disable audio bell in gvim"
date: 2012-07-30T21:27:26
slug: blog20120730quiet-please-disable-audio-bell-in-gvim
tags: ["vim"]
cover: /img/cover-code-editor.jpg
---

I don't want to hear it any more, so I've put this into **.vimrc**

{{< highlight vim >}}

  " quiet pleeeeeease

  if has('autocmd')
    autocmd GUIEnter * set visualbell t_vb=
  endif
{{< /highlight >}}
