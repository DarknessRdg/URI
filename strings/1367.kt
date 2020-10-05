import java.util.*


const val CORRECT = "correct"


fun main(args: Array<String>) {

    val input = Scanner(System.`in`)

    var n = input.nextInt()

    while (n != 0) {
        input.nextLine()
        val submissoes = mutableListOf<String>()

        for (i in 1..n)
            submissoes.add(input.nextLine())

        val (s, p) = contar(submissoes)
        println("${s} ${p}")

        n = input.nextInt()
    }
}

fun contar(submissoes: List<String>): List<Int> {
    val problemas = mutableMapOf<String, Int>()
    val correctProblems = mutableSetOf<String>()

    for (instance in submissoes) {
        val (code, tempoInstance, status) = instance.split(" ")
        val tempo = tempoInstance.toInt()

        val correct = status == CORRECT
        val prevTemp = problemas[code] ?: 0

        if (correct && !correctProblems.contains(code)) {
            correctProblems.add(instance.substring(0, 1))
            problemas[code] = prevTemp + getTempoParaAdd(tempo, correct)
        } else if (!correct)
            problemas[code] = prevTemp + getTempoParaAdd(tempo, correct)
    }

    return listOf(
            qntProblemas(correctProblems),
            somarTempos(problemas, correctProblems)
    )
}

fun somarTempos(problemas: MutableMap<String, Int>,
                toAdd: MutableSet<String>): Int {

    var sum = 0
    toAdd.forEach {
        sum += problemas[it]!!
    }
    return sum
}

fun getTempoParaAdd(tempo: Int, correct: Boolean) = if (correct) tempo else 20

fun qntProblemas(problemas: MutableSet<String>) = problemas.size
