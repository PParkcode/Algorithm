import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.*


fun main(){
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))


    val fn= br.readLine()!!.toInt()
    val flist= hashSetOf<Int>()
    br.readLine()!!.split(" ").map{flist.add(it.toInt())}

    val sn= br.readLine()!!.toInt()
    val slist= br.readLine()!!.split(" ").map{it.toInt()}

    val answer= mutableListOf<Int>()

    for(i in slist){
        if(flist.contains(i)){
            //answer.add(1)
            bw.write("1\n")
        }
        else{
           // answer.add(0)
            bw.write("0\n")
        }
    }

    bw.flush()
    bw.close()
}