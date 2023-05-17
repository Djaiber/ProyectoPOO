<?php

include("conexion.php");

$code = $_POST["code"];
$value = $_POST["value"];

//Registrar
if(isset($_POST["btnReceipt"]))
{
	$sqlgrabar = "INSERT INTO receipt(codeReceipt, valueReceipt) values ('$code','$value')";
	
	if(mysqli_query($conn,$sqlgrabar))
	{
		echo "<script> alert('Compra registrada con exito $code!'); window.location='loginAdmin.html' </script>";
	}else 
	{
		echo "Error: ".$sql."<br>".mysql_error($conn);
	}
}


?>