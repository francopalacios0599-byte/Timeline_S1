import streamlit as st
st.set_page_config(page_title="Sesion 2 | ISIL", layout="centered")
st.title("Evolución de Equipos de Cómputo | Timeline")
st.write("Autores: Franco Palacios, Sebastian Gamarra, Daniel Garcia, Gabriel Chipana | ISIL")
st.write("Interactúa con la barra deslizante para explorar los hitos más importantes en la historia de la IA.")
# URLs de imágenes en GitHub
base_url = "https://raw.githubusercontent.com/francopalacios0599-byte/Timeline_S1/main/timeline_images/"
imagenes = {
1: base_url + "Timeline1.png",
2: base_url + "Timeline2.png",
3: base_url + "Timeline3.png",
4: base_url + "Timeline4.png",
5: base_url + "Timeline5.png"
}
# Slider
opcion = st.slider(
"Selecciona un punto del timeline",
min_value=1,
max_value=5,
value=1,
step=1
)
# Mostrar imagen según slider
st.image(imagenes[opcion], use_container_width=True)

if opcion == 1:
  st.info("""
    **Periodo 1: Las Primeras Computadoras Electrónicas (Años 40 - 50)**  
    En este período, las computadoras eran máquinas masivas que ocupaban habitaciones enteras. Estaban construidas con miles de tubos de vacío, lo que las hacía muy grandes, costosas y propensas a fallas.
    
    **Recursos Computacionales:**  
    • Hardware: Tubos de vacío, relés electromecánicos, tambores magnéticos.  
    • Velocidad: Medida en milisegundos por operación.  
    • Memoria: Muy limitada, apenas unos pocos KB.  
    • Programación: En lenguaje máquina o ensamblador, usando tarjetas perforadas.  

    **Aplicaciones Soportadas:**  
    • Cálculos científicos y militares (trayectorias, descifrado de códigos).  
    • Procesamiento de datos para censos o contabilidad.  
    • Simulaciones básicas.
    """)
if opcion == 2:
    st.info("""
    ### **Periodo 2: La Era de los Transistores y los Mainframes (Años 50 - 60)**  
    La invención del transistor revolucionó la computación, reemplazando los voluminosos tubos de vacío. Esto permitió computadoras más pequeñas, rápidas y fiables, dando origen a los mainframes.

    **Recursos Computacionales:**  
    • Hardware: Transistores discretos, memorias de núcleo magnético, cintas magnéticas y discos para almacenamiento masivo.  
    • Velocidad: Medida en microsegundos por operación.  
    • Memoria: Cientos de KB a pocos MB.  
    • Programación: FORTRAN y COBOL; surgen los primeros sistemas operativos.  

    **Aplicaciones Soportadas:**  
    • Procesamiento bancario y de seguros.  
    • Gestión de inventarios y nóminas.  
    • Análisis científicos y de ingeniería.  
    • Sistemas de reservación aérea.
    """)
if opcion == 3:
    st.info("""
    ### **Periodo 3: Los Circuitos Integrados y las Minicomputadoras (Años 60 - 70)**  
    Los circuitos integrados permitieron miniaturizar componentes y aumentar la potencia de cómputo, dando paso a las minicomputadoras.

    **Recursos Computacionales:**  
    • Hardware: Circuitos integrados SSI/MSI; procesadores de 8 a 16 bits.  
    • Velocidad: Medida en nanosegundos por operación.  
    • Memoria: Varios MB.  
    • Programación: Sistemas multiusuario como UNIX; surge el lenguaje C.  

    **Aplicaciones Soportadas:**  
    • Control industrial.  
    • Sistemas departamentales.  
    • Investigación científica y simulaciones.  
    • Edición de texto y desarrollo de software.  
    • Primeros videojuegos.
    """)
if opcion == 4:
    st.info("""
    ### **Periodo 4: La Computadora Personal y el Microprocesador (Años 70 - 90)**  
    El microprocesador permitió que la computación llegara a hogares y oficinas, dando inicio a la era de la PC.

    **Recursos Computacionales:**  
    • Hardware: Microprocesadores de 8, 16 y 32 bits; RAM en MB; discos duros; pantallas a color.  
    • Velocidad: Medida en MHz.  
    • Memoria: Cientos de KB a decenas de MB.  
    • Programación: Sistemas operativos gráficos (Windows, Mac OS); lenguajes orientados a objetos.  

    **Aplicaciones Soportadas:**  
    • Procesadores de texto, hojas de cálculo, bases de datos personales.  
    • Diseño gráfico y publicación de escritorio.  
    • Videojuegos avanzados.  
    • Navegación temprana por Internet (finales de los 90).  
    • Desarrollo de software.
    """)
if opcion == 5:
    st.info("""
    ### **Periodo 5: La Era de la Computación Ubicua e Internet (Años 2000 - Actualidad)**  
    La computación está presente en todos los dispositivos: móviles, nube, IA y entornos conectados.

    **Recursos Computacionales:**  
    • Hardware: CPUs multinúcleo de 64 bits, GPUs, RAM de GB a TB, SSD, móviles, dispositivos IoT.  
    • Velocidad: Medida en GHz, MOPS y FLOPS.  
    • Memoria: GB en móviles; TB y PB en servidores.  
    • Programación: iOS, Android, desarrollo web, Python para IA, contenedores y APIs.  

    **Aplicaciones Soportadas:**  
    • Redes sociales y streaming.  
    • Apps móviles de todo tipo.  
    • IA y Machine Learning (voz, imagen, chatbots, autos autónomos).  
    • Realidad Virtual y Aumentada.  
    • Computación en la nube (SaaS, PaaS, IaaS).  
    • IoT y domótica.  
    • Big Data y análisis masivo.
    """)

