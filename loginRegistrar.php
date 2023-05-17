<?php

include("conexion.php");

$nombre = $_POST["usuario"];
$pass   = $_POST["pass"];
$email =$_POST["email"];
$telefono = $_POST["telefono"];
$nombreAux;
$nombreAdmin== "Martha";
$passAdmin=="12345678";
//Login
if(isset($_POST["btningresar"]))
{
	
	$query = mysqli_query($conn,"SELECT * FROM consumer WHERE nameConsumer = '$nombre' AND password='$pass'");
	$nr = mysqli_num_rows($query);
	if($nombre=="Martha" and $pass=="12345678"){
		echo "<script> alert('Bienvenido Administrador $nombreAdmin'); window.location='loginAdmin.html' </script>";	
	}
	
	if($nr==1)
	{
		echo "<script> alert('Bienvenido $nombre'); window.location='loginUsuario.html' </script>";	
		
	}else
	{
		echo "<script> alert('Usuario no existe'); window.location='index.html' </script>";
	}

}


//Registrar
if(isset($_POST["btnregistrar"]))
{
	$sqlgrabar = "INSERT INTO consumer(nameConsumer, emailConsumer, password, telefono) values ('$nombre','$email','$pass','$telefono')";
	
	if(mysqli_query($conn,$sqlgrabar))
	{
		echo "<script> alert('Usuario registrado con exito: $nombre'); window.location='index.html' </script>";
	}else 
	{
		echo "Error: ".$sql."<br>".mysql_error($conn);
	}
}

?>