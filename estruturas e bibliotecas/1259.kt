import java.util.*


val input = Scanner(System.`in`)


fun main(array: Array<String>) {

    val entradas = mutableListOf<Int>()
    for (i in 1..input.nextInt())
        entradas.add(input.nextInt())

    for (i in ordList(entradas))
        println(i)
}


fun ordList(entradas: List<Int>): List<Int> {
    val par = entradas.filter { it % 2 == 0 }
    val impar = entradas.filter { it % 2 != 0 }


    return par.sorted() + impar.sortedDescending()
}
