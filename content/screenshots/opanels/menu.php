<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>jsdom::menu</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<style type="text/css" media="screen">
<!--
    @import url(../global.css);

    .panels_menu a {
        color: #eee;
        text-decoration: none;
        background: #666;
        padding: 0px 5px;
        margin: 0px 2px;
        border: solid 1px #333;
     }
    .panels_menu a:hover { background: #ccc; color: #f33; border-bottom: solid 1px #ccc; }
    .panels_menu a.active { background: #eee; color: #333;  border-bottom: solid 1px #eee; }
    .subpanel {
        <?php if($_GET['js'] == 1) {?>display: none;<?php } ?>
        border: solid 1px #333;
        padding: 10px;
        margin: 0 0 10px;
    }
-->
</style>
<script type="text/javascript" src="opanels.js"></script>

</head>
<body <?php if($_GET['js'] == 1){ ?>onload="preparePanels()"<?php } ?>>
<h1>panele JavaScript</h1>
<?php
if(isset($_POST['submit']) ) {
    print '<h3>dane z formularza</h3>';
    print '<pre>';
    print_r($_POST);
    print '</pre>';
    print '<hr/>';
}
?>
<p class="footer"><strong>widok: <a href="menu.php?js=1">z preparePanels()</a> | <a href="menu.php">bez JS</a></strong> :: <a href="http://onjin.net/index.php/2006/02/09/skracanie-formularzy-java-script/">powrót do opisu</a></p>
<div id="info">
     <p>Funkcja <code>preparePanels</code> z pliku <a href="opanels.js">opanels.js</a> odnajduje wszystkie elementy <em>DIV</em> przypisane do klasy <em>CSS</em> <strong>subpanel</strong>. Pobiera wartość ich atrybutu <em>title</em> jako nazwy zakładek. Następnie ukrywa wszystkie takie <em>DIV'y</em> oprócz pierwszego i wyświetla nad nim stworzone zakładki.</p>
     <p>Wywołanie funkcji <code>preparePanels</code> powinno się odbyć po załadowaniu kodu strony czyli np <code>&lt;body onLoad="preparePanels();"&gt;</code>.</p>
     <p><strong>Nowość</strong>: każda zakładka otrzymuje teraz <em>ID</em> o wartości <em>'menu_'+ID odpowiedniego DIV'a</em>. Możliwe więc teraz jest samodzielne aktywowanie zakładek. Np. aktywacja DIV'a o ID  <a href="#" onclick="activMenu(document.getElementById('menu_p_newsletter'));">p_newsletter</a> wymaga kodu <em>[activMenu(document.getElementById('menu_p_newsletter')]</em>.</p>
</div>
<h3>moje konto</h3>
<div id="panele">
<form method="post" action="menu.php<?php if($_GET['js']) { print '?js=1'; }?>">
    <div class="subpanel" id="p_dane_os" title="dane osobowe">
        <h3>dane osobowe</h3>
        <table>
        <tr>
            <td>Imię</td>
            <td><input type="text" name="name" value="Marek" /></td>
        </tr>
        <tr>
            <td>Nazwisko</td>
            <td><input type="text" name="last_name" value="Wywiał" /></td>
        </tr>
        <tr>
            <td>Strona WWW</td>
            <td><input type="text" name="website" value="http://onjin.net/" /></td>
        </tr>
        </table>
    </div>
    
    <div class="subpanel" id="p_opcje" title="opcje powiadomień">
        <h3>opcje powiadomień</h3>
        <fieldset><legend>opcje powiadomień</legend>
        <label><input type="checkbox" name="SMSon" />powiadomienia SMS o poczcie</label><br/>
        <label><input type="checkbox" name="EMAILon" />powiadomienia e-mailem o SMS'ach</label>
        </fieldset>
    </div>
    
    <div class="subpanel" id="p_newsletter" title="newsletter">
        <h3>newsletter</h3>
        <fieldset><legend>newsletter</legend>
        <label><input type="checkbox" name="NEWS1" />chce otrzymywać newsletter #1</label><br/>
        <label><input type="checkbox" name="NEWS2" />chce otrzymywać newsletter #2</label>
        </fieldset>
    </div>
    <input type="submit" name="submit" value="zatwierdź" />
</form>
</div><!-- end id="panele" -->
<p>Funkcja testowana była tylko pod Firefox 1.5, Opera 8.5 oraz IE 6.0. Po szczegóły zapraszam do źródeł tego przykładu lub ew. mail me.</p>
<p>CSS oczywiście jest minimalny, tylko dla prezentacji sposobu użycia.</p>

</body>
</html>
