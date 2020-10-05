import java.util.*
import kotlin.NoSuchElementException


val input = Scanner(System.`in`)

var countLoop = 0


fun main(array: Array<String>) {

    while(true) {
        try {
            core()
            countLoop++
        } catch (_: NoSuchElementException) {
            break
        }
    }
}

fun core() {
    val entrada = input.nextLine()

    val cont = contar(entrada)

    if (countLoop != 0)
        println()

    for ((k, v) in cont.entries)
        println("${k.toInt()} $v")
}


fun contar(entrada: String): SortedMap<Char, Int> {
    val cont = mutableMapOf<Char, Int>()

    for (letra in entrada) {
        val prev = cont[letra] ?: 0
        cont[letra] = prev + 1
    }

    return cont.toSortedMap(
            compareBy<Char> { cont[it] }.thenByDescending { it }
    )
}
