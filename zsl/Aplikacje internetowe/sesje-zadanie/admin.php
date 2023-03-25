<?php 
session_start();

if(isset($_SESSION['zalogowany']) && $_SESSION['zalogowany'] == 1){

?>
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Dodawanie:</h2>
    <form action="admin.php" method="POST">
        Nazwa: <input type="text" name="nazwa" required><br>
        <input type="submit" value="Dodaj">
    </form>
    <?php 
        if(isset($_POST['nazwa'])){
            $conn0 = new mysqli('localhost','root','','baza2');
            $result0 = $conn0->query("SELECT * FROM przedmioty");
            $j=0;
            while($row0 = $result0->fetch_assoc()){
                if($row0['nazwa'] == $_POST['nazwa']){
                    $j++;
                }
            }
            if($j==0){
                $nazwa = $_POST['nazwa'];
                $conn = new mysqli('localhost','root','','baza2');
                $q = "INSERT INTO przedmioty(nazwa)
                VALUES
                ('$nazwa')";
                $conn->query($q);
                $conn->close();
                header('location: admin.php');
            } else {
                echo "Podany przedmiot jest już w bazie danych";
            }
        }
    ?>
    <br><hr><br>
    <?php 
        $conn1 = new mysqli('localhost','root','','baza2');
        if(isset($_GET['action']) && isset($_GET['id'])){
            $action = $_GET['action'];
            $id = $_GET['id'];
            if($action = "delete"){
                $conn1->query("DELETE FROM przedmioty WHERE `id` = $id");
            }
            header("location: admin.php");
        }
        $conn1->close();

        $conn2 = new mysqli('localhost','root','','baza2');
        $result = $conn2->query("SELECT * FROM przedmioty");
        echo "<table border>";
        $i = 1;
        echo "<tr><th>ID</th><th>Nazwa</th></tr>";
        while($row = $result->fetch_assoc()){
            echo "<tr><td>".$i."</td><td>".$row['nazwa']."</td><td><a href='?action=delete&id=".$row['id']."'>usuń</a></td></tr>";
            $i++;
        }
        echo "</table>";
        $conn2->close();
    ?>
</body>
</html>
<?php 
} else {
    echo "Strona dostępna tylko dla administratorów!";
}
?>