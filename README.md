# Proyecto 03

## Ransomware de Encriptación

**Estudiantes:** Esteban Alvarado, Martín Calderón, Olman Castro, Lucía M. Golcher
***

### Dependencias 📦

Antes de poder correr este programa, debe instalar las siguientes dependencias:

```sh
sudo apt update
sudo apt install python3 \ 
                python3-pip
pip3 install psutil
```

> ⚠️ **Debe saber que este programa encripta archivos con una llave aleatoria, no corra el riesgo de utilizar archivos importantes. Este programa se realizó con fines académicos y no debe utilizarse para causar daño a otros.**

### ¿Cómo correr el programa?

```sh
python3 src/ransomware.py <path-to-file> <key-size>
```

Si lo desea, puede correr el script de ejemplo `run.sh` que ejecuta el programa para 6 valores de longitud de la llave sobre un archivo de prueba.

***

<p align="center">
<img src="https://static.platzi.com/media/achievements/badge-introduccion-seguridad-informatica-905ce3cb-b80b-48a6-97ae-d438567a1d24.png" width="75"/>
</p>
