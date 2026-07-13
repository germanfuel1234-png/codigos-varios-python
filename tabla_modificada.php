<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {    
    $numero = intval($_POST['numero']);
    $i = intval($_POST['numero2']);
    echo "<h2>Tabla de Multiplicar de $numero</h2>";
    echo "<ul>";
    for ($f = 1; $f <= $i; $f++) {
        $resultado = $numero * $f;
        echo "<li>$numero x $f = $resultado</li>";
        }
        echo "</ul>";
        } 
else {
    echo "<p>Por favor, ingrese un número en el formulario.</p>";
     }
?>
<a href="index.html">Volver</a>          