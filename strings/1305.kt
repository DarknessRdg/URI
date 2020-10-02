import java.io.EOFException
import java.util.*
import kotlin.NoSuchElementException


fun main(args: Array<String>) {
    val input = Scanner(System.`in`)
    while (true) {
        try {

            val num = input.nextLine()
            val cutoff = input.nextLine()

            println(arredondar(num, cutoff))
        } catch (end: EOFException) {
            break
        } catch (end: NoSuchElementException) {
            break
        }
    }
}


fun arredondar(number: String, cutoff: String): Int {
    var number = cleanString(number)
    var cutoff = cleanString(cutoff)

    var (num, decimal) = number.split('.')
    decimal = "0.${decimal}"

    var numInt = try {
        num.toInt()
    } catch (_: NumberFormatException) {
        0
    }

    if (decimal.toDouble() >= cutoff.toDouble())
        numInt++

    return numInt
}


fun cleanString(string: String): String {
    var value = if (string.indexOf('.') == -1)
        "${string}.0"
    else
        string

    var dot = value.indexOf('.')

    return when (dot) {
        value.length-1 -> "${value}0"
        0 -> "0${value}"
        -1 -> "0.0"
        else -> value
    }
}
