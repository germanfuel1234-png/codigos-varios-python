<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tabla de Multiplicar</title>
</head>
<body>
    <h1>Tabla de Multiplicar</h1>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" ) {
            $numero = intval($_POST['numero']);
        
            echo "<h2>Tabla de Multiplicar de $numero</h2>";
            echo "<ul>";
            for ($i = 1; $i <= 10; $i++) {
                $resultado = $numero * $i;
                echo "<li>$numero x $i = $resultado</li>";
            }
            echo "</ul>";
        } else {
            echo "<p>Por favor, ingrese un número en el formulario.</p>";
        }
    ?>
    <a href="index.html">Volver</a>          
</body>
</html>