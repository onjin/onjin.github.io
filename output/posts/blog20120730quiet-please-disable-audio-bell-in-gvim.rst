.. title: quiet please !! disable audio bell in gvim
.. slug: blog20120730quiet-please-disable-audio-bell-in-gvim
.. date: 2012-07-30 21:27:26
.. tags: vim


I don't want to hear it any more, so I've put this into **.vimrc**

.. code:: vim

    " quiet pleeeeeease

    if has('autocmd')
    autocmd GUIEnter * set visualbell t_vb=
    endif
