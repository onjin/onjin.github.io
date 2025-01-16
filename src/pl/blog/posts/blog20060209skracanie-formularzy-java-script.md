---
title: "skracanie formularzy + java script"
date: 2006-02-09T08:28:54
tags: ["www", "html", "javascript"]
---
Długie formularze, podzielone na kilka sekcji ciągnące się w dół strony, nie są zbyt czytelne. Formularz taki można zmodyfikować dzieląć go na klikalne etapy lub wizualne zakładki. Ale jeżeli mamy wiele takich formularzy napisanych na dodatek w samym HTML'u ?

<img src="/pl/assets/screenshots/opanels/normal.jpg" width="273" height="334" alt="widok normalny">

Możemy to sobie uprościć za pomocą JavaScript. Odpowiednia funkcja wywołana po załadowaniu się strony [<em>body onLoad="funkcja();"</em>] może wyszukać sekcje naszego formularza i zwinąć je do ciekawszych wizualnie zakładek.

<img src="/pl/assets/screenshots/opanels/panels.jpg" width="316" height="200" alt="widok z zakładkami">

Żeby funkcja wiedziała co jest sekcją, należy je odpowiednio oznaczyć np. poprzez odpowiednią klasę <em>CSS</em> 'subpanel'



Druga ważna rzecz, skrypt musi wiedzieć jak nazwać zakładki. Do tego wykorzystałem atrybut <em>title</em>. Nasz kod wygląda teraz tak:



```html

<div class="subpanel" title="zakładka 1">
    <h2>sekcja 1</h2>
</div>

<div class="subpanel" title="zakładka 2">
    <h2>sekcja 2</h2>
</div>

```


Teraz za pomocą JavaScript możemy odnaleźć wszystkie znaczniki <em>DIV</em>.


```javascript

if (!document.getElementsByTagName
    || !document.createElement
    || !document.appendChild) return;


/* pobieramy wszystkie div'y */

var divs = document.getElementsByTagName("div");

```



Następnie przygotowywujemy dodatkowy element <em>DIV</em>, w którym umieścimy stworzone zakładki.



```javascript

/*  nr. pierwszego div'a z klasą subpanel */

var firstDiv = -1;



/* tworzymy div na nasze menu */

var menu = document.createElement("div");

menu.className = "panels_menu";

menu.setAttribute("id","panels_menu");

```



Pozostaje nam przejść się pętlą po wszystkich znalezionych <em>DIV</em>'ach i wybrać te, które posiadają klasę 'subpanel'. Z każdego z nich pobieramy wartość atrybutu <em>title</em> i naszym 'menu' tworzymy odpowiedni odnośnik:



```javascript

var source = divs[i].getAttribute("title");

if (!source) continue;

var link = document.createElement("a");

link.setAttribute("href","#"+source);
link.setAttribute("onclick","activMenu(this); ");
link.onclick = new Function('activMenu(this);'); // dla IE
link.setAttribute("id","menu_"+divs[i].id); // dla wywołań zewnętrznych
link.appendChild(document.createTextNode(source));

```



Aktywujemy pierwszą naszą zakładkę i dodajemy je do naszego nowego menu:



```javascript

if(firstDiv == -1) firstDiv = i;

if(i == firstDiv) {
    divs[i].style.display='block';
    link.setAttribute('class','active');
}

/* dodajemy odnośnik do menu */

menu.appendChild(link);

link.className = "active"; // dla IE

```



A po zakończeniu całej pętli wklejamy nasze zakładki przed pierwszego <em>DIV</em>'a z klasą 'subpanel':



```javascript

/* wklejamy stworzone menu nad pierwszym div'em */

divs[firstDiv].parentNode.insertBefore(menu,divs[firstDiv]);

```



Tyle w temacie stworzenia zakładek. Pozostaje nam stworzyć funkcję <em>activeMenu(this)</em>, którą wywołujemy po kliknięciu w odpowiednią zakładkę.



```javascript

function activMenu(menu) {
  menubox = document.getElementById('panels_menu');
  links = menubox.childNodes;

  /* ustalamy clasę 'active' dla naszego
    odnośnika, a reszcie null */
  for(x=0;x<links.length x if links menu.classname="active" menu.blur var divs='document.getElementsByTagName("div");' chowamy wszystkie div pr aktualnego for i="0;" menu.innerhtml else return false ca zwie drobny>CSS:
```

```css
   .panels_menu a {
        color: #eee;
        text-decoration: none;
        background: #666;
        padding: 0px 5px;
        margin: 0px 2px;
        border: solid 1px #333;
     }
    .panels_menu a:hover {
        background: #ccc;
        color: #f33;
        border-bottom: solid 1px #ccc;
    }
    .panels_menu a.active {
        background: #eee;
        color: #333;
        border-bottom: solid 1px #eee;
    }
    .subpanel {
                border: solid 1px #333;
        padding: 10px;
        margin: 0 0 10px;
    }
```



Wystarczy teraz do <em>&lt;body&gt;</em> dodać <strong>onLoad="preparePanels()"</strong> i to już wszystko.



Poniżej jest pełen kod funkcji preparePanels():

```javascript

function preparePanels() {
  if (!document.getElementsByTagName
    || !document.createElement
    || !document.appendChild) return;
  /* pobieramy wszystkie div'y */
  var divs = document.getElementsByTagName("div");

  /* nr. pierwsze div'a z klasą subpanel */
  var firstDiv = -1;

  /* tworzymy div na nasze menu */
  var menu = document.createElement("div");
  menu.className = "panels_menu";
  menu.setAttribute("id","panels_menu");

  for (var i=0; i<divs.length i je klasa div to subpanel to:
  if firstdiv="i;" sprawdzamy istnienie atrybutu
  var source='divs[i].getAttribute("title");'
  continue chowamy divs tworzymi odno do w naszym menu link='document.createElement("a");' link.setattribute link.appendchild jest pierwszym go aktywujemy dodajemy menu.appendchild wklejamy stworzone nad dzia przyk znajduje si href="http://onjin.net/misc/opanels/menu.php">tutaj. Odnośniki w lewym górnym rogu strony uruchamiają wersję kolejno z i bez preparePanels().



```
Jeżeli komuś się ta wiedza przyda, to miło mi będzie :)</divs.length></links.length></body></html>
