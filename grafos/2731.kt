import java.util.*

val input = Scanner(System.`in`)


class Aresta(
        val verticeFinal: Verticie,
        val peso: Int
) {
    override fun toString() = "v${verticeFinal.id}($peso)"
}


class Verticie(val id: Int) {
    val estradas = mutableListOf<Aresta>()
    var tempo = Int.MAX_VALUE / 2
    var pai: Verticie? = null
    var aberto = true

    fun addAresta(vertice: Verticie,  peso: Int) {
        val aresta = Aresta(vertice, peso)
        estradas.add(aresta)
    }

    override fun toString() = id.toString()

    override fun hashCode() = id

    override fun equals(other: Any?): Boolean {
        if (other is Verticie)
            return id == other.id
        return true
    }
}


class Grafo{
    var qntAresta = 0
    private set

    val vertices = mutableMapOf<Int, Verticie>()

    fun add(value1: Int, value2: Int, peso: Int) {
        val vertice1 =  vertices[value1] ?: Verticie(value1)
        val vertice2 =  vertices[value2] ?: Verticie(value2)

        vertice1.addAresta(vertice2, peso)
        vertice2.addAresta(vertice1, peso)

        vertices[value1] = vertice1
        vertices[value2] = vertice2

        qntAresta += 2
    }
}


class Dijkstra(
        grafo: Grafo,
        origem: Int
) {
    private val priority: Comparator<Verticie> = compareBy { it.tempo }
    private val queueDistancias = PriorityQueue<Verticie>(priority)

    init {
        grafo.vertices[origem]!!.tempo = 0
        queueDistancias.add(grafo.vertices[origem]!!)
        main()
    }

    fun main() {
        while (!queueDistancias.isEmpty()) {
            val atual = queueDistancias.poll()

            for (aresta in atual.estradas) {
                if (aresta.verticeFinal.aberto) {
                    val dist = aresta.peso + atual.tempo

                    if (dist < aresta.verticeFinal.tempo) {
                        aresta.verticeFinal.tempo = dist
                        aresta.verticeFinal.pai = atual
                        queueDistancias.add(aresta.verticeFinal)
                    }
                }
            }
            atual.aberto = false
        }
    }
}

fun questao(entradas: Int) {
    val grafo = Grafo()

    for (i in 1..entradas) {
        val v1 = input.nextInt()
        val v2 = input.nextInt()
        val peso = input.nextInt()

        grafo.add(v1, v2, peso)
    }

    val origem = 1
    Dijkstra(grafo, origem)

    val lugar = input.nextInt()

    var vertice = grafo.vertices[lugar]
    val tempo = vertice!!.tempo

    if (tempo <= 2 * 60)
        print("Will not be late. Travel time - $tempo - best way -")
    else
        print("It will be ${tempo - 120} minutes late. Travel time - $tempo - best way -")

    while (vertice is Verticie) {
        print(" ${vertice.id}")
        vertice = vertice.pai
    }
    println()
}


fun main(args: Array<String>) {
    var cidades = input.nextInt()
    var entradas = input.nextInt()

    while (cidades != 0 && entradas != 0) {
        questao(entradas)

        cidades = input.nextInt()
        entradas = input.nextInt()
    }
}
