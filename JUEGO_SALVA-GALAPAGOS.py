import pilasengine

pilas = pilasengine.iniciar()
puntaje = pilas.actores.Puntaje(-280, 200, color=pilas.colores.blanco)
sonido_de_musica = pilas.sonidos.cargar('fondo.wav')
sonido_de_musica.reproducir(repetir = True)


class AnclaEnemiga(pilasengine.actores.Actor):

    def iniciar(self):

        self.imagen = "anclaa.png"
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-200, 200)
        self.y = 290
        self.velocidad = 1

    def actualizar(self):
        self.rotacion += 4
        self.y -= self.velocidad


        if self.y < -300:
            self.eliminar()


fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('f.jpg')
fondo.escala=[0.5]
enemigos = pilas.actores.Grupo()
def crear_enemigo():
    actor = AnclaEnemiga(pilas)
    enemigos.agregar(actor)
pilas.tareas.siempre(0.1, crear_enemigo)


class Tortuga(pilasengine.actores.Actor):
 def iniciar(self):
        self.imagen = "galapagos.png"
 def actualizar(self):

     if self.pilas.control.izquierda:

        self.x -= 5
        self.espejado = True
     if self.pilas.control.derecha:
        self.x += 5
        self.espejado = False
     if self.pilas.control.arriba:
        self.y += 5
        self.espejado = True
     if self.pilas.control.abajo:
        self.y -= 5
        self.espejado = False

tortuga = Tortuga(pilas)
class Municion(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "burbuja.png"
pilas.actores.vincular(Municion)


tortuga.aprender('LimitadoABordesDePantalla')
tortuga.aprender('disparar', angulo_salida_disparo=90, municion = 'Municion')
tortuga.decir("Ayudame a acabar con estas anclas!")


def cuando_toca (protagonista, item):
    protagonista.eliminar()
    protagonista.decir("Hicimos lo que pudimos!!!\nGAME OVER")
    sonido_de_musica.detener()
pilas.colisiones.agregar(tortuga, enemigos, cuando_toca)

def eliminar_enemigo(disparo, enemigo):
    enemigo.eliminar()
    disparo.eliminar()
    puntaje.aumentar()         

pilas.colisiones.agregar('Municion', 'AnclaEnemiga', eliminar_enemigo)
pilas.avisar(u"Mueva la tortuga con el teclado y dispare con ESPACIO ")
pilas.ejecutar()

