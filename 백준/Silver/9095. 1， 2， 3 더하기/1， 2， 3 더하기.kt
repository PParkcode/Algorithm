fun main() {

    val br = System.`in`.bufferedReader()
    val sb = StringBuilder()

    val times = br.readLine().toInt()

    var num: Int
    repeat(times) {
        num = br.readLine().toInt()
        println(solution(num))
    }


}

fun solution(num: Int): Int {
    val dp = IntArray(12)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    if (num < 4) {
        return dp[num]
    }
    for (i in 4..num) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    }
    return dp[num]
}
