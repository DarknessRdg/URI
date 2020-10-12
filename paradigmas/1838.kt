mport java.util.*

class Requisicao(
        val inicio: Int,
        val fim: Int
) {
    val duracao = fim - inicio
}

val input = Scanner(System.`in`)

fun main(args: Array<String>) {
    val n = input.nextInt()
    input.nextLine()

    val list = mutableListOf<Requisicao>()
    for (i in 1..n) {
        list.add(Requisicao(
                input.nextInt(),
                input.nextInt()
        ))
    }

    println(contar(list))
}

fun contar(rq: List<Requisicao>): Int {
    val ordenado = rq.sortedWith(
            compareBy({ it.inicio }, { it.fim })
    )

    val dp = Array(ordenado.size) { 0 }

    for ((index, req) in ordenado.withIndex()) {

        var max = 0
        for (i in index-1 downTo 0) {
            if (dp[i] > max && ordenado[index].inicio >= ordenado[i].fim) {
                max = dp[i]
            }
        }

        dp[index] += max + req.duracao
    }

    return dp.max() ?: 0
}
