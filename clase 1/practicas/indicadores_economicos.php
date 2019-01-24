    <?php
    $JsonSource = "http://indicadoresdeldia.cl/webservice/indicadores.json";
    $json = json_decode(file_get_contents($JsonSource));
    echo $json->santoral->ayer;
    echo $json->santoral->hoy;
    echo $json->santoral->maniana;
    echo $json->moneda->dolar;
    echo $json->moneda->euro;
    echo $json->indicador->uf;
    echo $json->indicador->ipc
    echo $json->indicador->utm;
    echo $json->bolsa->ipsa;
    echo $json->bolsa->igpa;
    echo $json->bolsa->inter10;
    echo $json->bolsa->banca;
    echo $json->bolsa->commodities;
    echo $json->bolsa->const_inmob;
    echo $json->bolsa->industrial;
    echo $json->bolsa->retail;
    echo $json->bolsa->consumo;
    echo $json->bolsa->utilities;
    ?>