import java.util.*
import kotlin.NoSuchElementException

val input = Scanner(System.`in`)

var contCaracteres = 0
var contLinhasPag = 0
var primeiraPalavra = true

fun main(args: Array<String>) {
    while (true) {
        try {
            val qnt = input.nextInt()
            val linhas = input.nextInt()
            val carct = input.nextInt()
            input.nextLine()

            val string = input.nextLine()

            println(contar(qnt, linhas, carct, string))
        } catch (_: NoSuchElementException) {
            break
        }
    }
}

fun contar(
        qntPalavras: Int,
        maxLinhasPag: Int,
        maxCaracteresLinha: Int,
        texto: String
): Int {
    contCaracteres = 0
    contLinhasPag = 0
    primeiraPalavra = true

    val palavras = texto.split(" ")

    for (p in palavras){
        val size = p.length

        outrasPalavras(maxCaracteresLinha, size)

        if (primeiraPalavra)
            primeiraPalavra(size)
    }

    var pages = contLinhasPag / maxLinhasPag
    if (contLinhasPag % maxLinhasPag != 0)
        pages++

    return pages
}

fun primeiraPalavra(
        size: Int
) {
    primeiraPalavra = false
    contCaracteres = size
    contLinhasPag++
}

fun outrasPalavras(
        maxCaracteresLinha: Int,
        size: Int
) {
    val qntAdd = contCaracteres + size + 1

    if (qntAdd > maxCaracteresLinha || primeiraPalavra) {
        primeiraPalavra = true
        return
    }

    contCaracteres = qntAdd
}
