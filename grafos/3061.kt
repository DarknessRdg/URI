import java.util.*

val input = Scanner(System.`in`)


fun main(args: Array<String>) {
    val n = input.nextInt()
    val m = input.nextInt()

    val matrix = Array(n) { Array(m) { 0 } }
    val visitados = Array(n) { Array(m) { false } }

    for (i in 0 until n)
        for (j in 0 until m)
            matrix[i][j] = input.nextInt()

    println(dfs(matrix, n, m, visitados))
}


fun dfs(
        matrix: Array<Array<Int>>,
        n: Int,
        m: Int,
        v: Array<Array<Boolean>>
): Int {
    var  cont = 0
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (matrix[i][j] == 1) {
                cont++
                clear(matrix, i, j, v)
            }
        }
    }

    return cont
}


fun clear(
        matrix: Array<Array<Int>>,
        _i: Int,
        _j: Int,
        visitados: Array<Array<Boolean>>
) {
    val stack = Stack<Pair<Int, Int>>()

    stack.push(Pair(_i, _j))


    while (!stack.empty()) {
        val (i, j) = stack.pop()!!

        visitados[i][j] = true

        if (matrix[i][j] == 1) {
            matrix[i][j] = 0

            if (ok(matrix, i+1, j, visitados))
                stack.push(Pair(i+1, j))

            if (ok(matrix, i-1, j, visitados))
                stack.push(Pair(i-1, j))

            if (ok(matrix, i, j+1, visitados))
                stack.push(Pair(i, j+1))

            if (ok(matrix, i, j-1, visitados))
                stack.push(Pair(i, j-1))
        }
    }
}


fun ok(
        matrix: Array<Array<Int>>,
        i: Int,
        j: Int,
        visitados: Array<Array<Boolean>>
): Boolean {
    if (i < 0 || i > matrix.size-1)
        return false
    if (j < 0 || j > matrix[i].size-1)
        return false
    return !visitados[i][j]
}
