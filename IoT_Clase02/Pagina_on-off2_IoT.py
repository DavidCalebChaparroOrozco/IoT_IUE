from machine import Pin,ADC
import network
import socket
import time

led=Pin(2,Pin.OUT)

ssid='IUEINALAMBRICA'
pw=''

#volumen=ADC(Pin (13))
volumen=ADC(Pin (13))

volumen.atten(ADC.ATTN_11DB)

WLAN=network.WLAN(network.STA_IF)
WLAN.active(True)
WLAN.connect(ssid,pw)

while not WLAN.isconnected():
    print("Conectando...")
    
estado=WLAN.ifconfig()
print(estado)
    
def pagina():
    html= """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <title>IoT David Caleb Orozco - Juan Durango</title>
</head>

<body>
    <main>
        <a class="logotipo" id="logotipo">
            <div class="texto-animado" id="logo">David Caleb Orozco - Juan Durango</div>
            <p class="subtitulo">Hello World, here Caleb</p>
        </a>
    </main>
    <article>
        <h1></h1>
    </article>
</body>
<a href="/on"> <button class="button">¡ On !</button></a>
<a href="/off"><button class="button">¡ Off !</button></a>

</html>

<script>
    class TextoAnimado {
	constructor(id, objetivo){
		this.texto = document.getElementById(id);
		this.objetivo = document.getElementById(objetivo);
		this.letras = this.texto.innerText.split("");
		
		this.texto.innerText = '';

		this.letras.forEach((letra) => {
			let caracter = letra === ' ' ? '&nbsp;' : letra;

			this.texto.innerHTML = this.texto.innerHTML + `
				<div>
					<span>${caracter}</span>
					<span class="segunda-linea">${caracter}</span>
				</div>
			`;
		});

		this.objetivo.addEventListener('mouseenter', () => {
			let cuenta = 0;

			const intervalo = setInterval(() => {
				if(cuenta < this.texto.children.length){
					this.texto.children[cuenta].classList.add('animacion');
					cuenta += 1;
				} else {
					clearInterval(intervalo);
				}
			}, 30);
		});

		this.objetivo.addEventListener('mouseleave', () => {
			let cuenta = 0;

			const intervalo = setInterval(() => {
				if(cuenta < this.texto.children.length){
					this.texto.children[cuenta].classList.remove('animacion');
					cuenta += 1;
				} else {
					clearInterval(intervalo);
				}
			}, 30);
		});
		
	}
}

new TextoAnimado('logo', 'logotipo');
</script>


<style>
    :root {
	--logotipo: #1a1a1a;
	--profesion: #f2f2f2;
	--primario: #2e5fff;
}

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

a {
	text-decoration: none;
	color: #fff;
	outline: none;
}

main {
	width: 90%;
	margin: auto;
	max-width: 800px;
	min-height: 100vh;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
}

.logotipo {
	padding: 10px;
	border: 5px solid var(--logotipo);
	color: var(--logotipo);
}

.logotipo .subtitulo {
	text-align: center;
	color: var(--profesion);
	background: var(--logotipo);
	padding: 12px 20px;
	transition: .5s ease all;
	font-size: 36px;
	font-family: 'Noto Sans', sans-serif;
	text-transform: uppercase;
	letter-spacing: 2px;
}

.logotipo:hover .subtitulo {
	background: var(--primario);
}

.texto-animado {
	display: flex;
	justify-content: center;
	overflow: hidden;
}

.texto-animado > div {
	display: flex;
	flex-direction: column;
	position: relative;
	transition: .3s ease all;
}

.texto-animado > div.animacion {
	transform: translateY(-100px);
}

.texto-animado > div span {
	font-size: 100px;
	font-weight: normal;
	line-height: 100px;
}

.texto-animado .segunda-linea {
	position: absolute;
	top: 100px;
}

@media screen and (max-width: 600px){
	.texto-animado > div span {
		font-size: 50px;
		line-height: 50px;
	}

	.texto-animado .segunda-linea {
		top: 50px;
	}

	.texto-animado > div.animacion {
		transform: translateY(-50px);
	}

	.logotipo .subtitulo {
		font-size: 20px;
	}
}

:root {
  --fuenteHeading: "PT Sans", sans-serif;
  --fuenteParrafos: "Open Sans", sans-serif;
  --primario: #1c9b71;
  --gris: #e1e1e1;
  --blanco: #ffffff;
  --negro: #000000;
  --color-texto: #2e5fff;
  --logotipo: #6246ff;
  --profesion: #f2f2f2;
}

body {
  margin: 0;
  padding: 0;
  background: var(--negro);
  display: flex;
  justify-content: center;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
}
.slidershow {
  width: 700px;
  height: 400px;
  overflow: hidden;
}
.middle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.navigation {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
}
.bar {
  width: 50px;
  height: 10px;
  border: 2px solid var(--logotipo);
  margin: 6px;
  cursor: pointer;
  transition: 0.4s;
}
.bar:hover {
  background: var(--negro);
}

input[name="r"] {
  position: absolute;
  visibility: hidden;
}

.slides {
  width: 500%;
  height: 100%;
  display: flex;
}

.slide {
  width: 20%;
  transition: 0.6s;
}
.slide img {
  width: 100%;
  height: 100%;
}

#r1:checked ~ .s1 {
  margin-left: 0;
}
#r2:checked ~ .s1 {
  margin-left: -20%;
}
#r3:checked ~ .s1 {
  margin-left: -40%;
}
#r4:checked ~ .s1 {
  margin-left: -60%;
}
#r5:checked ~ .s1 {
  margin-left: -80%;
}

/* Header */
.webp .header {
  background-image: url(../img/banner.webp);
}

.no-webp .header {
  background-image: url(../img/banner.jpg);
}

.header {
  height: 60rem;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  width: 100%;
}

.header__texto {
  text-align: center;
  color: var(--blanco);
  margin-top: 5rem;
}

@media (min-width: 768px) {
  .header__texto {
    margin-top: 15rem;
  }
}

.logo {
  color: var(--blanco);
}

.logo__nombre {
  font-weight: 400;
}

.logo__bold {
  font-weight: 700;
}

.barra {
  padding-top: 4rem;
}

@media (min-width: 768px) {
  .barra {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}

/* Globales */
.contenedor {
  max-width: 120rem;
  width: 90%;
  margin: 0 auto;
}

/* Utilidades */
.no-margin {
  margin: 0;
}

.no-padding {
  padding: 0;
}

.centrar-texto {
  text-align: center;
}

/* Glowing */
.glowing {
  position: relative;
  min-width: 750px;
  height: 750px;
  margin: -150px;
  transform-origin: right;
  animation: colorChange 5s linear infinite;
}

.glowing:nth-child(even) {
  transform-origin: left;
}

@keyframes colorChange {
  0% {
    filter: hue-rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    filter: hue-rotate(360deg);
    transform: rotate(360deg);
  }
}

.glowing span {
  position: absolute;
  top: calc(80px * var(--i));
  left: calc(80px * var(--i));
  bottom: calc(80px * var(--i));
  right: calc(80px * var(--i));
}

.glowing span:before {
  content: "";
  position: absolute;
  top: 50%;
  left: -8px;
  width: 15px;
  height: 15px;
  background: #f00;
  border-radius: 50%;
}

.glowing span:nth-child(3n + 1):before {
  background: rgba(134, 255, 0, 1);
  box-shadow: 0 0 20px rgba(134, 255, 0, 1), 0 0 40px rgba(134, 255, 0, 1),
    0 0 60px rgba(134, 255, 0, 1), 0 0 80px rgba(134, 255, 0, 1),
    0 0 0 8px rgba(134, 255, 0, 1);
}

.glowing span:nth-child(3n + 2):before {
  background: rgba(255, 214, 0, 1);
  box-shadow: 0 0 20px rgba(255, 214, 0, 1), 0 0 40px rgba(255, 214, 0, 1),
    0 0 60px rgba(255, 214, 0, 1), 0 0 80px rgba(255, 214, 0, 1),
    0 0 0 8px rgba(255, 214, 0, 1);
}

.glowing span:nth-child(3n + 3):before {
  background: rgba(0, 226, 255, 1);
  box-shadow: 0 0 20px rgba(0, 226, 255, 1), 0 0 40px rgba(0, 226, 255, 1),
    0 0 60px rgba(0, 226, 255, 1), 0 0 80px rgba(0, 226, 255, 1),
    0 0 0 8px rgba(0, 226, 255, 1);
}

.glowing span:nth-child(3n + 1) {
  animation: animate 10s alternate infinite;
}
.glowing span:nth-child(3n + 2) {
  animation: animate-reverse 3s alternate infinite;
}
.glowing span:nth-child(3n + 3) {
  animation: animate 8s alternate infinite;
}

@keyframes animate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes animate-reverse {
  0% {
    transform: rotate(360deg);
  }
  100% {
    transform: rotate(0deg);
  }
}

.glowing-grid {
    display: grid;
    grid-template-columns: 3;
}

.button {
        font-family: "Open Sans", sans-serif;
        font-size: 16px;
        letter-spacing: 2px;
        text-decoration: none;
        text-transform: uppercase;
        color: #000;
        cursor: pointer;
        border: 3px solid;
        padding: 0.25em 0.5em;
        box-shadow: 1px 1px 0px 0px, 2px 2px 0px 0px, 3px 3px 0px 0px, 4px 4px 0px 0px, 5px 5px 0px 0px;
        position: relative;
        user-select: none;
        -webkit-user-select: none;
        touch-action: manipulation;
    }

    .button:active {
        box-shadow: 0px 0px 0px 0px;
        top: 5px;
        left: 5px;
    }

    @media (min-width: 768px) {
        .button {
            padding: 0.25em 0.75em;
        }
    }
    
    body {
	font-family: 'Bebas Neue', cursive;
	background-image: url('https://fondosmil.com/fondo/54333.jpg');
	background-repeat: no-repeat;
	background-size: cover;
}
</style>
"""
    
    return html

elservidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

elservidor.bind(('',80))
elservidor.listen()

while True:
    variable=int(volumen.read())
    print(variable)
    conex,addr=elservidor.accept()
    request=conex.recv(1024)
    request=str(request)
    if request.find('/on')==6:
        print ('entró')
        led.on()
        #time.sleep(1)
   # else:
        #request.find ('/off')
        #led.off()
    Web=pagina()
    conex.send('HTTP/1.1 200 OK\n')
    conex.send('Content-Type:text/html\n')
    conex.send('Connection:close\n\n')
    conex.sendall(Web)
    conex.close()
    print(volumen)