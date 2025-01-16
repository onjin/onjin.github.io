/* activMenu(Object menu)
   - nadaje objektowi 'menu' klasę active, pozostałym null
   - zmienia wartość stylu odpowiedniego 'div' display: block; 
     pozostałym display: none; [dotyczy div'ów z klasą 'subpanel']
*/
function activMenu(menu) {
    menubox = document.getElementById('panels_menu');
    links = menubox.childNodes;

    /* ustalamy clasę 'active' dla naszego odnośnika, a reszcie null */
    for(x=0;x<links.length; x++) {
        if(links[x].nodeName.indexOf('A') != -1) {
            links[x].className=null;
        }
    }
    menu.className='active';
    menu.blur();


    var divs = document.getElementsByTagName("div");
    /* chowamy wszystkie div'y prócz aktualnego */
    for (var i=0; i<divs.length; i++) {
        if(divs[i].className == 'subpanel') {
            if(divs[i].getAttribute("title") == menu.innerHTML) {
                divs[i].style.display = 'block';
            } else {
                divs[i].style.display = 'none';
            }
        }
    }
    return false;
}

/* preparePanels()
   - odnajduje wszystkie div'y z klasą 'subpanel' i ukrywa wszystkie prócz pierwszego
   - nad tym pierwszym wyświetla odnośniki do wszystkich ukrytych div'ów
*/
function preparePanels() {
    if (!document.getElementsByTagName || !document.createElement || !document.appendChild) return;
    /* pobieramy wszystkie div'y */
    var divs = document.getElementsByTagName("div");

    /* zmienna przechowująca nr. pierwsze div'a z klasą subpanel */
    var firstDiv = -1;

    /* tworzymy div na nasze menu */
    var menu = document.createElement("div");
    menu.className = "panels_menu";
    menu.setAttribute("id","panels_menu");

    for (var i=0; i<divs.length; i++) {
        /* jeśli klasa div'a to subpanel to czynimy co należy */
        if(divs[i].className == 'subpanel') {
            if(firstDiv == -1) firstDiv = i;

            /* sprawdzamy istnienie atrybutu 'title' */
            var source = divs[i].getAttribute("title");
            if (!source) continue;

            /* chowamy div'a */
            divs[i].style.display='none';

            /* tworzymi odnośnik do div'a w naszym menu */
            var link = document.createElement("a");
            link.setAttribute("href","#"+source);
            link.setAttribute("onclick","activMenu(this); ");
            link.setAttribute("id","menu_"+divs[i].id);
            link.onclick = new Function('activMenu(this);');
            link.appendChild(document.createTextNode(source));

            /* jeśli div jest pierwszym to go aktywujemy */
            if(i == firstDiv) {
                divs[i].style.display='block';
                link.setAttribute('class','active');
                link.className = "active";
            }

            /* dodajemy odnośnik do menu */
            menu.appendChild(link);




        }
    }
    /* wklejamy stworzone menu nad pierwszym div'em */
    divs[firstDiv].parentNode.insertBefore(menu,divs[firstDiv]);
}


