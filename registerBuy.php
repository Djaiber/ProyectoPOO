<?php

include("conexion.php");
include ("loginRegistrar.php");

$buyCode = $_POST["buyCode"];

//como traigo esos valores idCliente y nameConsumer
if(isset($_POST["btnRegisterBuy"]))
{
	$sqlgrabar = "INSERT INTO registershopping(nameConsumer, shoppingCode) values ('$nombreAux','$buyCode')";
	
	if(mysqli_query($conn,$sqlgrabar))
	{
		echo "<script> alert('Compra registrada con exito $nombreAux!'); window.location='loginUsuario.html' </script>";
	}else 
	{
		echo "Error: ".$sql."<br>".mysql_error($conn);
	}
}


?>